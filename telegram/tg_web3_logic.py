from _web3.core import Core
from _web3.client import Client
from _setup.config import *

network = OPTIMiSM_GOERLI_RPC


def test_case(private_key: str) -> str | bool:
    core = Core(run=RUN_SCRIPT, network=network)
    address = core._get_address(private_key)
    connection = core._check_connection()
    return address, connection


def get_balance_case(private_key: str) -> str | float:
    core = Core(run=RUN_SCRIPT, network=network)
    client = Client(core)

    address = core._get_address(private_key)
    balance = client._get_human_balance(private_key)

    return address, balance


def get_all_balances_case(private_key: str) -> str | dict:
    core = Core(run=RUN_SCRIPT, network=network)
    client = Client(core)

    address = core._get_address(private_key)
    balances = client._get_all_kresko_balance(private_key)

    return address, balances


def approve_all_tokens_for_swap(private_key: str) -> str | dict:
    core = Core(run=RUN_SCRIPT, network=network)
    client = Client(core)

    address = core._get_address(private_key)
    results = client.approve_all_tokens_for_swap(private_key)

    return address, results


def approve_all_tokens_for_deposit(private_key: str) -> str | dict:
    core = Core(run=RUN_SCRIPT, network=network)
    client = Client(core)

    address = core._get_address(private_key)
    results = client.approve_all_tokens_for_deposit(private_key)

    return address, results


def approve_all_tokens_for_liquidity(private_key: str) -> str | dict:
    core = Core(run=RUN_SCRIPT, network=network)
    client = Client(core)

    address = core._get_address(private_key)
    results = client.approve_all_tokens_for_liquidity(private_key)

    return address, results


def swap_from_KISS_to_token(
    private_key: str, to_token_name: str, kiss_value: float, to_token_kiss_rate: float
):
    core = Core(run=RUN_SCRIPT, network=network)
    client = Client(core)

    address = core._get_address(private_key)
    result, tx_hash = client.swap_from_KISS(
        private_key, to_token_name, kiss_value, to_token_kiss_rate
    )

    return address, result, tx_hash


def swap_to_KISS(
    private_key: str,
    from_token_name: str,
    from_token_value: float,
    to_token_rate: float,
):
    core = Core(run=RUN_SCRIPT, network=network)
    client = Client(core)

    address = core._get_address(private_key)
    result, tx_hash = client.swap_to_KISS(
        private_key, from_token_name, from_token_value, to_token_rate
    )
    return address, result, tx_hash


def deposit_asset(private_key: str, asset_name: str, asset_amount: float):
    core = Core(run=RUN_SCRIPT, network=network)
    client = Client(core)

    address = core._get_address(private_key)
    result, tx_hash = client.deposit_asset(private_key, asset_name, asset_amount)

    return address, result, tx_hash


def withdrawal_asset(private_key: str, asset_name: str, asset_amount: float):
    core = Core(run=RUN_SCRIPT, network=network)
    client = Client(core)

    address = core._get_address(private_key)
    result, tx_hash = client.withdrawal_asset(private_key, asset_name, asset_amount)

    return address, result, tx_hash


def borrow_asset(private_key: str, asset_name: str, asset_amount: float):
    core = Core(run=RUN_SCRIPT, network=network)
    client = Client(core)

    address = core._get_address(private_key)
    result, tx_hash = client.borrow_asset(private_key, asset_name, asset_amount)

    return address, result, tx_hash


def repay_asset(private_key: str, asset_name: str, asset_amount: float):
    core = Core(run=RUN_SCRIPT, network=network)
    client = Client(core)

    address = core._get_address(private_key)
    result, tx_hash = client.repay_asset(private_key, asset_name, asset_amount)

    return address, result, tx_hash


def add_liquidity(
    private_key: str,
    asset_A_name: str,
    asset_B_name: str,
    asset_B_amount: float,
    kiss_rate: float,
):
    core = Core(run=RUN_SCRIPT, network=network)
    client = Client(core)

    address = core._get_address(private_key)
    result, tx_hash = client.add_liquidity(
        private_key, asset_A_name, asset_B_name, asset_B_amount, kiss_rate
    )

    return address, result, tx_hash
