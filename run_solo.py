from _run._utils import *
from telegram.tg_web3_logic import *
from loguru import logger


if __name__ == "__main__":
    parser = create_parser()
    namespace = parser.parse_args(sys.argv[1:])

    if namespace.module == "test":
        key = namespace.private_key
        try:
            address, connection = test_case(key)
            logger.info(f"Private key: {key}")
            logger.success(f"Wallet {address[:9]} | Connection - {connection}")
        except Exception as e:
            logger.error(e)

    if namespace.module == "balances":
        key = namespace.private_key
        try:
            address, balances = get_all_balances_case(key)
            logger.info(f"Private key: {key}")
            for _key in balances:
                value = balances[_key]
                logger.success(f"Wallet {address[:9]} | Balance - {_key} - {value}")
        except Exception as e:
            logger.error(e)

    if namespace.module == "approve_swaps":
        key = namespace.private_key
        try:
            address, results = approve_all_tokens_for_swap(key)
            logger.info(f"Private key: {key}")
            for _key in results:
                value = results[_key]
                logger.success(f"Wallet {address[:9]} | Result - {_key} - {value}")
        except Exception as e:
            logger.error(e)

    if namespace.module == "approve_deposits":
        key = namespace.private_key
        try:
            address, results = approve_all_tokens_for_deposit(key)
            logger.info(f"Private key: {key}")
            for _key in results:
                value = results[_key]
                logger.success(f"Wallet {address[:9]} | Result - {_key} - {value}")
        except Exception as e:
            logger.error(e)

    if namespace.module == "approve_liquidity":
        key = namespace.private_key
        try:
            address, results = approve_all_tokens_for_liquidity(key)
            logger.info(f"Private key: {key}")
            for _key in results:
                value = results[_key]
                logger.success(f"Wallet {address[:9]} | Result - {_key} - {value}")
        except Exception as e:
            logger.error(e)

    if namespace.module == "swap_from_kiss":
        key = namespace.private_key
        to_token_name = namespace.token_name
        kiss_value = namespace.token_value
        to_token_kiss_rate = namespace.rate

        try:
            address, result, tx_hash = swap_from_KISS_to_token(
                key, to_token_name, kiss_value, to_token_kiss_rate
            )
            logger.info(f"Private key: {key}")
            logger.success(
                f"Wallet {address[:9]} | Result - {result} | TX Hash - {tx_hash}"
            )
        except Exception as e:
            logger.error(e)

    if namespace.module == "swap_to_kiss":
        key = namespace.private_key
        from_token_name = namespace.token_name
        from_token_value = namespace.token_value
        to_token_rate = namespace.rate

        try:
            address, result, tx_hash = swap_to_KISS(
                key, from_token_name, from_token_value, to_token_rate
            )
            logger.info(f"Private key: {key}")
            logger.success(
                f"Wallet {address[:9]} | Result - {result} | TX Hash - {tx_hash}"
            )
        except Exception as e:
            logger.error(e)

    if namespace.module == "deposit":
        key = namespace.private_key
        asset_name = namespace.token_name
        asset_amount = namespace.token_value

        try:
            address, result, tx_hash = deposit_asset(key, asset_name, asset_amount)
            logger.info(f"Private key: {key}")
            logger.success(
                f"Wallet {address[:9]} | Result - {result} | TX Hash - {tx_hash}"
            )
        except Exception as e:
            logger.error(e)

    if namespace.module == "withdrawal":
        key = namespace.private_key
        asset_name = namespace.token_name
        asset_amount = namespace.token_value

        try:
            address, result, tx_hash = withdrawal_asset(key, asset_name, asset_amount)
            logger.info(f"Private key: {key}")
            logger.success(
                f"Wallet {address[:9]} | Result - {result} | TX Hash - {tx_hash}"
            )
        except Exception as e:
            logger.error(e)

    if namespace.module == "borrow":
        key = namespace.private_key
        asset_name = namespace.token_name
        asset_amount = namespace.token_value

        try:
            address, result, tx_hash = borrow_asset(key, asset_name, asset_amount)
            logger.info(f"Private key: {key}")
            logger.success(
                f"Wallet {address[:9]} | Result - {result} | TX Hash - {tx_hash}"
            )
        except Exception as e:
            logger.error(e)

    if namespace.module == "repay":
        key = namespace.private_key
        asset_name = namespace.token_name
        asset_amount = namespace.token_value

        try:
            address, result, tx_hash = repay_asset(key, asset_name, asset_amount)
            logger.info(f"Private key: {key}")
            logger.success(
                f"Wallet {address[:9]} | Result - {result} | TX Hash - {tx_hash}"
            )
        except Exception as e:
            logger.error(e)

    if namespace.module == "add_liq":
        key = namespace.private_key
        asset_A_name = namespace.asset_A_name
        asset_B_name = namespace.asset_B_name
        asset_B_amount = float(namespace.token_value)
        kiss_rate = float(namespace.rate)

        try:
            address, result, tx_hash = add_liquidity(
                key, asset_A_name, asset_B_name, asset_B_amount, kiss_rate
            )
            logger.info(f"Private key: {key}")
            logger.success(
                f"Wallet {address[:9]} | Result - {result} | TX Hash - {tx_hash}"
            )
        except Exception as e:
            logger.error(e)
