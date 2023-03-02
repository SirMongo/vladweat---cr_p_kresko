import json
import random
import requests
import time
from time import sleep

from web3.middleware import geth_poa_middleware
from web3.gas_strategies.time_based import medium_gas_price_strategy

from loguru import logger
from decimal import Decimal
from web3 import Web3, HTTPProvider

from _setup.tokens_abi import KRESKO_abis


class Core:
    def __init__(self, run: str, network: str) -> None:
        # FOR PROD
        if (
            run
            == "Special for https://t.me/importweb3, creator - https://t.me/vladweat"
        ):
            logger.info(f"{run}")
            pass
        else:
            logger.error(f"Fatal error in script. FO!")
            raise SystemExit(1)
        self._web3 = self.__set_web3_rpc(network)

    def __set_web3_rpc(self, network: str) -> Web3:
        web3 = Web3(HTTPProvider(network))
        web3.middleware_onion.inject(geth_poa_middleware, layer=0)
        return web3

    def _check_connection(self) -> bool:
        try:
            return self._web3.isConnected()
        except Exception as e:
            logger.error(e)

    def _get_address(self, private_key):
        try:
            address = self._web3.eth.account.from_key(private_key).address
            return address
        except Exception as e:
            logger.error(e)

    def _get_nonce(self, private_key: str) -> int:
        try:
            address = self._get_address(private_key)
            nonce = self._web3.eth.get_transaction_count(address)
            return nonce
        except Exception as e:
            logger.error(e)

    def _get_chain_id(self) -> int:
        return self._web3.eth.chain_id

    def _get_contract(self, contract_address: str):
        erc20_abi = KRESKO_abis[contract_address]

        checksum_address = self._get_checksum_address(contract_address)
        contract = self._web3.eth.contract(address=checksum_address, abi=erc20_abi)
        return contract

    def _convert_from_ether_format(self, num: int = None) -> float:
        try:
            ether_format = self._web3.fromWei(num, "ether")
            return ether_format
        except Exception as e:
            logger.error(e)

    def _convert_to_ether_format(self, num: float = None) -> int:
        try:
            wei_format = self._web3.toWei(Decimal(num), "ether")
            return wei_format
        except Exception as e:
            logger.error(e)

    def _convert_from_mwei_format(self, num: int = None) -> float:
        try:
            ether_format = self._web3.fromWei(num, "mwei")
            return ether_format
        except Exception as e:
            logger.error(e)

    def _convert_to_mwei_format(self, num: float = None) -> int:
        try:
            wei_format = self._web3.toWei(Decimal(num), "mwei")
            return wei_format
        except Exception as e:
            logger.error(e)

    def _get_checksum_address(self, address: str) -> str:
        try:
            checksum_address = self._web3.toChecksumAddress(address)
            return checksum_address
        except Exception as e:
            logger.error(e)

    def _build_contract_tx_param(self, from_private_key: str, value: int) -> dict:
        address = self._get_checksum_address(self._get_address(from_private_key))

        gaslimit = random.randint(600000, 650000)

        transaction_param = {
            "chainId": self._get_chain_id(),
            "from": address,
            "nonce": self._get_nonce(from_private_key),
            "value": value,
            "gas": gaslimit,
            "gasPrice": self._web3.eth.gas_price,
            # "gasPrice": self._get_gas_price(),
        }
        return transaction_param

    def _sign_transaction(self, transaction, private_key: str) -> dict:
        try:
            signed_tx = self._web3.eth.account.sign_transaction(
                transaction, private_key
            )
            return signed_tx
        except Exception as e:
            logger.error(e)

    def _send_raw_transaction(self, sign_txn: dict) -> str:
        try:
            raw_tx_hash = self._web3.eth.send_raw_transaction(sign_txn.rawTransaction)
            return raw_tx_hash
        except Exception as e:
            logger.error(e)

    def _get_tx_hash(self, raw_tx_hash: str) -> str:
        try:
            tx_hash = self._web3.toHex(raw_tx_hash)
            return tx_hash
        except Exception as e:
            logger.error(e)

    def _sign_send_get_tx_hash(self, transaction: dict, private_key: str) -> str:
        signed_transaction = self._sign_transaction(transaction, private_key)
        raw_tx_hash = self._send_raw_transaction((signed_transaction))
        tx_hash = self._get_tx_hash(raw_tx_hash)
        return tx_hash

    def _wait_for_transaction_receipt(self, tx_hash) -> bool:
        try:
            tx_status = self._web3.eth.waitForTransactionReceipt(tx_hash).status
            if tx_status == 1:
                # logger.success(f"Tx {tx_hash} CONFIRMED")
                return True
            else:
                return False
        except Exception as e:
            logger.error(e)

    def _add_random_delay(self, min, max):
        sleep(random.randint(min, max))
        return True

    def _get_api_data(self):

        endpoint = "https://api.kresko.link/protocol?chainName=optimismGoerli"
        response = requests.get(endpoint)
        data = response.json()

        tokens = ["KISS", "DAI", "krETH", "krBTC", "krXAU", "krWTI", "krTSLA"]
        tokens_in_response = data["tokens"]

        tokens_prices = {}

        if response.status_code == 200:

            for token in tokens_in_response:
                _token_symbol = token["symbol"]
                if _token_symbol in tokens:
                    tokens_prices[_token_symbol] = float(
                        token["priceData"]["price"]["number"]
                    )
            return tokens_prices

        else:
            return None

    def _get_deadline(self, expiry_seconds: int):
        return int(time.time()) + expiry_seconds

    def _value_with_slippage(self, amount: float, slippage: float) -> int:
        try:
            slippage = slippage / 100
            min_amount = amount - (amount * slippage)
            return min_amount
        except Exception as e:
            logger.error(e)
