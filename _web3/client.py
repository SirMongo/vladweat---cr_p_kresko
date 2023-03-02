from _web3.core import Core
from loguru import logger
import json
from _setup.helpers_abi import *
import random


class Client:
    def __init__(self, core: Core) -> None:
        self.core = core
        self.tokens = [
            {"token": "KISS", "address": "0xAcF353630a688e0fAbCb68AbbdB59A8e3f482656"},
            {"token": "DAI", "address": "0x3451E572ebD8bc292097593361744a1f8E321d8A"},
            {"token": "krETH", "address": "0x3b96b644CAe06987A4f2133F1E146c7dE5ceF3ac"},
            {"token": "krBTC", "address": "0x6a6A2f61a665B817DA48F0356C47406BD03127c3"},
            {"token": "krXAU", "address": "0xFC382404b498f891377d7C2C62d24b61407F7A7a"},
            {"token": "krWTI", "address": "0x65b301612C9Ca76ccB495722D7F02CD3acab5d2e"},
            {
                "token": "krTSLA",
                "address": "0x7Df1BE079F99066117F8214656B005068Ef2cA5F",
            },
        ]

    def _get_balance(self, private_key: str) -> float:
        try:
            address = self.core._get_address(private_key)
            balance = self.core._web3.eth.get_balance(address)
            return balance
        except Exception as e:
            logger.error(e)

    def _get_human_balance(self, private_key: str) -> float:
        try:
            address = self.core._get_address(private_key)
            balance = self.core._convert_from_ether_format(
                self.core._web3.eth.get_balance(address)
            )
            return balance
        except Exception as e:
            logger.error(e)

    def _get_token_balance(self, private_key: str, token_address: str) -> int:
        address = self.core._get_address(private_key)
        contract = self.core._get_contract(token_address)
        balance = contract.functions.balanceOf(address).call()

        return balance

    def _get_all_kresko_balance(self, private_key: str) -> dict:
        tokens = self.tokens
        balances = {}

        for token in tokens:
            symbol = token["token"]
            address = token["address"]
            token_balance = self._get_token_balance(private_key, address)
            token_balance = self.core._convert_from_ether_format(token_balance)
            balances[symbol] = str(token_balance)

        return balances

    def approve_token_for_swap(
        self, private_key: str, token_address: str
    ) -> bool | str:
        contract = self.core._get_contract(token_address)
        approve_function = contract.get_function_by_selector("0x095ea7b3")

        spender = self.core._get_checksum_address(
            "0x1f693246650f93a7E9f4a713479695881b96b5F1"
        )
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935
        try:
            tx_param = self.core._build_contract_tx_param(private_key, 0)
            transaction = approve_function(spender, amount).buildTransaction(tx_param)
            tx_hash = self.core._sign_send_get_tx_hash(transaction, private_key)

            self.core._wait_for_transaction_receipt(tx_hash)
            self.core._add_random_delay(2, 3)

            return True, tx_hash

        except Exception as e:
            return False, e

    def approve_token_for_deposit(
        self, private_key: str, token_address: str
    ) -> bool | str:
        contract = self.core._get_contract(token_address)
        approve_function = contract.get_function_by_selector("0x095ea7b3")

        spender = self.core._get_checksum_address(
            "0x87A7F2d14c4F09d55bf514738Deb72F4209aa76C"
        )
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935
        try:
            tx_param = self.core._build_contract_tx_param(private_key, 0)
            transaction = approve_function(spender, amount).buildTransaction(tx_param)
            tx_hash = self.core._sign_send_get_tx_hash(transaction, private_key)

            self.core._wait_for_transaction_receipt(tx_hash)
            self.core._add_random_delay(2, 3)

            return True, tx_hash

        except Exception as e:
            return False, e

    def approve_token_for_liquidity(
        self, private_key: str, token_address: str
    ) -> bool | str:
        contract = self.core._get_contract(token_address)
        approve_function = contract.get_function_by_selector("0x095ea7b3")

        spender = self.core._get_checksum_address(
            "0xB9bC72b84Ea6374B822De52087E303f7228f4850"
        )
        amount = 115792089237316195423570985008687907853269984665640564039457584007913129639935
        try:
            tx_param = self.core._build_contract_tx_param(private_key, 0)
            transaction = approve_function(spender, amount).buildTransaction(tx_param)
            tx_hash = self.core._sign_send_get_tx_hash(transaction, private_key)

            self.core._wait_for_transaction_receipt(tx_hash)
            self.core._add_random_delay(2, 3)

            return True, tx_hash

        except Exception as e:
            return False, e

    def approve_all_tokens_for_swap(self, private_key: str) -> dict:
        success_transaction = {}
        for token in self.tokens:
            symbol = token["token"]
            address = token["address"]
            res, tx_hash = self.approve_token_for_swap(private_key, address)
            if res == True:
                success_transaction[symbol] = str(tx_hash)
            elif res == False:
                success_transaction[symbol] = "failed transaction"
        return success_transaction

    def approve_all_tokens_for_deposit(self, private_key: str) -> dict:
        success_transaction = {}
        for token in self.tokens:
            symbol = token["token"]
            address = token["address"]
            res, tx_hash = self.approve_token_for_swap(private_key, address)
            if res == True:
                success_transaction[symbol] = str(tx_hash)
            elif res == False:
                success_transaction[symbol] = "failed transaction"
        return success_transaction

    def approve_all_tokens_for_liquidity(self, private_key: str) -> dict:
        success_transaction = {}
        for token in self.tokens:
            symbol = token["token"]
            address = token["address"]
            res, tx_hash = self.approve_token_for_liquidity(private_key, address)
            if res == True:
                success_transaction[symbol] = str(tx_hash)
            elif res == False:
                success_transaction[symbol] = "failed transaction"
        return success_transaction

    def _get_token_prices_dict(self) -> dict:
        return self.core._get_api_data()

    def _get_token_price_in_KISS(self, to_token_address: str) -> float:

        exact_token: str

        for token in self.tokens:
            if token["address"] == to_token_address:
                exact_token = token

        prices_dict = self._get_token_prices_dict()

        exact_price: int

        for symbol in prices_dict:
            if symbol == exact_token["token"]:
                exact_price = prices_dict[symbol]

        return exact_price

    def _get_token_name_by_address(self, token_address: str) -> str:
        for token in self.tokens:
            if token["address"] == token_address:
                return token["token"]

    def swap_from_KISS(
        self,
        private_key: str,
        to_token_name: str,
        kiss_value: float,
        to_token_kiss_rate: float,
    ) -> bool | str:
        address = self.core._get_address(private_key)
        from_token_address = self.core._get_checksum_address(
            "0xACF353630A688E0FABCB68ABBDB59A8E3F482656"
        )

        to_token_address = next(
            (
                token["address"]
                for token in self.tokens
                if token["token"] == to_token_name
            ),
            None,
        )

        to_token_name = self._get_token_name_by_address(to_token_address)
        to_token_price = to_token_kiss_rate

        uniswap_router_address = self.core._get_checksum_address(
            "0x1f693246650f93a7E9f4a713479695881b96b5F1"
        )
        uniswap_contract = self.core._web3.eth.contract(
            address=uniswap_router_address, abi=UniswapV2Router02_abi
        )

        swap_function = uniswap_contract.get_function_by_name(
            "swapExactTokensForTokens"
        )

        amount_in = self.core._convert_to_ether_format(kiss_value)

        _to_tokens_value = float(kiss_value) / float(to_token_price)
        amount_out_min = self.core._convert_to_ether_format(
            self.core._value_with_slippage(_to_tokens_value, 2)
        )

        path = [from_token_address, self.core._get_checksum_address(to_token_address)]

        to = address
        deadline = self.core._get_deadline(120)

        tx_param = self.core._build_contract_tx_param(private_key, 0)

        try:

            transaction = swap_function(
                amount_in, amount_out_min, path, to, deadline
            ).buildTransaction(tx_param)

            tx_hash = self.core._sign_send_get_tx_hash(transaction, private_key)

            self.core._add_random_delay(2, 3)

            result = self.core._wait_for_transaction_receipt(tx_hash)
            return result, tx_hash

        except Exception as e:
            return False, None

    def swap_to_KISS(
        self,
        private_key: str,
        from_token_name: str,
        from_token_value: float,
        to_token_rate: float,
    ) -> bool | str:
        address = self.core._get_address(private_key)

        from_token_address = next(
            (
                token["address"]
                for token in self.tokens
                if token["token"] == from_token_name
            ),
            None,
        )
        to_token_address = self.core._get_checksum_address(
            "0xACF353630A688E0FABCB68ABBDB59A8E3F482656"
        )
        amount_in = self.core._convert_to_ether_format(from_token_value)
        amount_out_min = self.core._value_with_slippage(
            amount_in / int(to_token_rate), 5
        )

        uniswap_router_address = self.core._get_checksum_address(
            "0x1f693246650f93a7E9f4a713479695881b96b5F1"
        )
        uniswap_contract = self.core._web3.eth.contract(
            address=uniswap_router_address, abi=UniswapV2Router02_abi
        )

        swap_function = uniswap_contract.get_function_by_name(
            "swapExactTokensForTokens"
        )

        _amount_in = int(amount_in)
        _amount_out_min = int(amount_out_min)
        _path = [self.core._get_checksum_address(from_token_address), to_token_address]
        _to = address
        _deadline = self.core._get_deadline(120)

        tx_param = self.core._build_contract_tx_param(private_key, 0)

        try:
            transaction = swap_function(
                _amount_in, _amount_out_min, _path, _to, _deadline
            ).buildTransaction(tx_param)

            tx_hash = self.core._sign_send_get_tx_hash(transaction, private_key)

            self.core._add_random_delay(2, 3)

            result = self.core._wait_for_transaction_receipt(tx_hash)

            return result, tx_hash

        except Exception as e:
            return False, None

    def deposit_asset(
        self, private_key: str, asset_name: str, asset_amount: float
    ) -> bool | str:

        address = self.core._get_address(private_key)

        to_token_address = next(
            (token["address"] for token in self.tokens if token["token"] == asset_name),
            None,
        )

        _account = address
        _collateral_asset = to_token_address
        _deposit_amount = self.core._convert_to_ether_format(asset_amount)

        deposit_contract_address = self.core._get_checksum_address(
            "0x87a7f2d14c4f09d55bf514738deb72f4209aa76c"
        )
        deposit_contract = self.core._web3.eth.contract(
            address=deposit_contract_address, abi=deposit_contract_abi
        )

        deposit_function = deposit_contract.get_function_by_name("depositCollateral")

        try:
            tx_param = self.core._build_contract_tx_param(private_key, 0)
            transaction = deposit_function(
                _account, _collateral_asset, _deposit_amount
            ).buildTransaction(tx_param)

            tx_hash = self.core._sign_send_get_tx_hash(transaction, private_key)

            self.core._add_random_delay(2, 3)

            result = self.core._wait_for_transaction_receipt(tx_hash)
            return result, tx_hash

        except Exception as e:
            return False, None

    def withdrawal_asset(
        self, private_key: str, asset_name: str, asset_amount: float
    ) -> bool | str:

        collateral_indexs = {
            "krWTI": 0,
            "krBTC": 1,
            "KISS": 2,
            "krETH": 3,
            "krTSLA": 4,
            "krXAU": 5,
        }

        address = self.core._get_address(private_key)
        to_token_address = next(
            (token["address"] for token in self.tokens if token["token"] == asset_name),
            None,
        )
        withdrawal_amount = self.core._convert_to_ether_format(asset_amount)
        index = collateral_indexs.get(asset_name)

        withdrawal_address = self.core._get_checksum_address(
            "0x87a7f2d14c4f09d55bf514738deb72f4209aa76c"
        )
        deposit_contract = self.core._web3.eth.contract(
            address=withdrawal_address, abi=deposit_contract_abi
        )

        withdrawal_function = deposit_contract.get_function_by_name(
            "withdrawCollateral"
        )

        try:
            tx_param = self.core._build_contract_tx_param(private_key, 0)
            transaction = withdrawal_function(
                address, to_token_address, withdrawal_amount, index
            ).buildTransaction(tx_param)

            tx_hash = self.core._sign_send_get_tx_hash(transaction, private_key)

            self.core._add_random_delay(2, 3)

            result = self.core._wait_for_transaction_receipt(tx_hash)
            return result, tx_hash

        except Exception as e:
            return False, None

    def borrow_asset(self, private_key: str, asset_name: str, asset_amount: float):
        address = self.core._get_address(private_key)

        to_token_address = next(
            (token["address"] for token in self.tokens if token["token"] == asset_name),
            None,
        )
        _account = address
        _kresko_asset = to_token_address
        _mint_amount = self.core._convert_to_ether_format(asset_amount)

        mint_contract_address = self.core._get_checksum_address(
            "0x87a7f2d14c4f09d55bf514738deb72f4209aa76c"
        )
        mint_contract = self.core._web3.eth.contract(
            address=mint_contract_address, abi=mint_contract_abi
        )

        mint_function = mint_contract.get_function_by_name("mintKreskoAsset")

        try:
            tx_param = self.core._build_contract_tx_param(private_key, 0)
            transaction = mint_function(
                _account, _kresko_asset, _mint_amount
            ).buildTransaction(tx_param)

            tx_hash = self.core._sign_send_get_tx_hash(transaction, private_key)

            self.core._add_random_delay(2, 3)

            result = self.core._wait_for_transaction_receipt(tx_hash)
            return result, tx_hash

        except Exception as e:
            return False, None

    def repay_asset(self, private_key: str, asset_name: str, asset_amount: float):
        pass

        collateral_indexs = {
            "krWTI": 0,
            "krBTC": 1,
            "KISS": 2,
            "krETH": 3,
            "krTSLA": 4,
            "krXAU": 5,
        }

        address = self.core._get_address(private_key)
        to_token_address = next(
            (token["address"] for token in self.tokens if token["token"] == asset_name),
            None,
        )
        burn_amount = self.core._convert_to_ether_format(asset_amount)
        index = collateral_indexs.get(asset_name)

        burn_address = self.core._get_checksum_address(
            "0x87a7f2d14c4f09d55bf514738deb72f4209aa76c"
        )
        burn_contract = self.core._web3.eth.contract(
            address=burn_address, abi=burn_contract_abi
        )

        burn_function = burn_contract.get_function_by_name("burnKreskoAsset")

        _account = address
        _kresko_asset = to_token_address
        _burn_amount = burn_amount
        _index = index

        try:
            tx_param = self.core._build_contract_tx_param(private_key, 0)
            transaction = burn_function(
                _account, _kresko_asset, _burn_amount, _index
            ).buildTransaction(tx_param)

            tx_hash = self.core._sign_send_get_tx_hash(transaction, private_key)

            self.core._add_random_delay(2, 3)

            result = self.core._wait_for_transaction_receipt(tx_hash)
            return result, tx_hash

        except Exception as e:
            return False, None

    def add_liquidity(
        self,
        private_key: str,
        asset_A_name: str,
        asset_B_name: str,
        asset_B_amount: float,
        kiss_rate: float,
    ):

        token_A_address = next(
            (
                token["address"]
                for token in self.tokens
                if token["token"] == asset_A_name
            ),
            None,
        )
        token_B_address = next(
            (
                token["address"]
                for token in self.tokens
                if token["token"] == asset_B_name
            ),
            None,
        )

        amount_B_desired = self.core._convert_to_ether_format(asset_B_amount)
        amount_A_desired = int(
            self.core._value_with_slippage(amount_B_desired / kiss_rate, 1)
        )

        slippage = 0.005

        amount_A_min = int(amount_A_desired - (amount_A_desired * slippage))
        amount_B_min = int(amount_B_desired - (amount_B_desired * slippage))

        to = self.core._get_address(private_key)
        deadline = self.core._get_deadline(120)

        uniswap_router_address = self.core._get_checksum_address(
            "0x1f693246650f93a7E9f4a713479695881b96b5F1"
        )
        uniswap_contract = self.core._web3.eth.contract(
            address=uniswap_router_address, abi=UniswapV2Router02_abi
        )

        liquidity_function = uniswap_contract.get_function_by_name("addLiquidity")

        try:
            tx_param = self.core._build_contract_tx_param(private_key, 0)
            transaction = liquidity_function(
                token_A_address,
                token_B_address,
                amount_A_desired,
                amount_B_desired,
                amount_A_min,
                amount_B_min,
                to,
                deadline,
            ).buildTransaction(tx_param)

            tx_hash = self.core._sign_send_get_tx_hash(transaction, private_key)

            self.core._add_random_delay(2, 3)

            result = self.core._wait_for_transaction_receipt(tx_hash)

            return result, tx_hash

        except Exception as e:
            return False, None
