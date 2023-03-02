import os
import asyncio
import logging

from aiogram import Bot, types
from aiogram.utils import executor
from aiogram.dispatcher import Dispatcher
from aiogram.types.message import ContentType
from aiogram.utils.markdown import text, bold, italic, code, pre
from aiogram.types import ParseMode, InputMediaPhoto, InputMediaVideo, ChatActions

from _web3.core import Core
from _web3.client import Client
from utils import get_private_keys
from _setup.config import *
from telegram.tg_web3_logic import *


bot = Bot(token=TG_API)
dp = Dispatcher(bot)


async def run_script(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        RUN_SCRIPT,
    )


@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        "Hello, this is VW pet project!\nWrite /help.",
    )


@dp.message_handler(commands=["help"])
async def process_help_command(message: types.Message):
    msg = text(
        bold("Use next commands:"),
        "/start",
        "/help",
        "/test",
        "/balances",
        "/approveAllSwap",
        "/approveAllDeposit",
        "/approveAllLiq",
        "/swapFromKiss",
        "/swapToKiss",
        "/deposit",
        "/withdrawal",
        "/borrow",
        "/repay",
        "/addLiq",
        sep="\n",
    )
    await message.reply(msg, parse_mode=ParseMode.MARKDOWN)


@dp.message_handler(commands=["test"])
async def process_test_command(message: types.Message):
    await bot.send_message(
        message.from_user.id,
        "Запуск тестового кейса",
    )
    keys_list = get_private_keys()
    for key in keys_list:
        address, connection = test_case(key)
        msg_string = f"Wallet {address[:8]} connected to network - {connection}"
        await bot.send_message(
            message.from_user.id,
            msg_string,
        )


@dp.message_handler(commands=["balances"])
async def process_balances_command(message: types.Message):
    await run_script(message)
    await bot.send_message(
        message.from_user.id,
        "Запуск вывода баланса",
    )
    keys_list = get_private_keys()
    for key in keys_list:
        address, balances = get_all_balances_case(key)
        msg_string = f"Wallet {address}\n\n"

        for dict_key in balances:
            msg_string += f"{dict_key} - {balances[dict_key]}\n"

        await bot.send_message(
            message.from_user.id,
            msg_string,
        )


@dp.message_handler(commands=["approveAllSwap"])
async def process_balances_command(message: types.Message):
    await run_script(message)
    await bot.send_message(
        message.from_user.id,
        "Запуск апрува всех монет для свапов",
    )
    keys_list = get_private_keys()
    for key in keys_list:
        address, results = approve_all_tokens_for_swap(key)
        msg_string = f"Wallet {address}\n\n"

        for tx in results:
            msg_string += f"{tx} - {results[tx]}\n"

        await bot.send_message(
            message.from_user.id,
            msg_string,
        )


@dp.message_handler(commands=["approveAllDeposit"])
async def process_balances_command(message: types.Message):
    await run_script(message)
    await bot.send_message(
        message.from_user.id,
        "Запуск апрува всех монет для депозитов",
    )
    keys_list = get_private_keys()
    for key in keys_list:
        address, results = approve_all_tokens_for_deposit(key)
        msg_string = f"Wallet {address}\n\n"

        for tx in results:
            msg_string += f"{tx} - {results[tx]}\n"

        await bot.send_message(
            message.from_user.id,
            msg_string,
        )


@dp.message_handler(commands=["approveAllLiq"])
async def process_balances_command(message: types.Message):
    await run_script(message)
    await bot.send_message(
        message.from_user.id,
        "Запуск апрува всех монет для депозитов",
    )
    keys_list = get_private_keys()
    for key in keys_list:
        address, results = approve_all_tokens_for_liquidity(key)
        msg_string = f"Wallet {address}\n\n"

        for tx in results:
            msg_string += f"{tx} - {results[tx]}\n"

        await bot.send_message(
            message.from_user.id,
            msg_string,
        )


@dp.message_handler(commands=["swapFromKiss"])
async def process_balances_command(message: types.Message):
    await run_script(message)
    args = message.text.split(" ")[1:]

    keys_list = get_private_keys()
    for key in keys_list:
        address, result, tx_hash = swap_from_KISS_to_token(
            key, args[0], args[1], args[2]
        )
        msg_string = f"Wallet {address}\n\n"
        msg_string += f"{result} - {tx_hash}\n"

        await bot.send_message(
            message.from_user.id,
            msg_string,
        )


@dp.message_handler(commands=["swapToKiss"])
async def process_balances_command(message: types.Message):
    await run_script(message)
    args = message.text.split(" ")[1:]

    keys_list = get_private_keys()
    for key in keys_list:
        address, result, tx_hash = swap_to_KISS(key, args[0], args[1], args[2])
        msg_string = f"Wallet {address}\n\n"
        msg_string += f"{result} - {tx_hash}\n"

        await bot.send_message(
            message.from_user.id,
            msg_string,
        )


@dp.message_handler(commands=["deposit"])
async def process_balances_command(message: types.Message):
    await run_script(message)
    args = message.text.split(" ")[1:]
    keys_list = get_private_keys()
    for key in keys_list:
        address, result, tx_hash = deposit_asset(key, args[0], args[1])
        msg_string = f"Wallet {address}\n\n"
        msg_string += f"{result} - {tx_hash}\n"

        await bot.send_message(
            message.from_user.id,
            msg_string,
        )


@dp.message_handler(commands=["withdrawal"])
async def process_balances_command(message: types.Message):
    await run_script(message)
    args = message.text.split(" ")[1:]
    keys_list = get_private_keys()
    for key in keys_list:
        address, result, tx_hash = withdrawal_asset(key, args[0], args[1])
        msg_string = f"Wallet {address}\n\n"
        msg_string += f"{result} - {tx_hash}\n"

        await bot.send_message(
            message.from_user.id,
            msg_string,
        )


@dp.message_handler(commands=["borrow"])
async def process_balances_command(message: types.Message):
    await run_script(message)
    args = message.text.split(" ")[1:]
    keys_list = get_private_keys()
    for key in keys_list:
        address, result, tx_hash = borrow_asset(key, args[0], args[1])
        msg_string = f"Wallet {address}\n\n"
        msg_string += f"{result} - {tx_hash}\n"

        await bot.send_message(
            message.from_user.id,
            msg_string,
        )


@dp.message_handler(commands=["repay"])
async def process_balances_command(message: types.Message):
    await run_script(message)
    args = message.text.split(" ")[1:]
    keys_list = get_private_keys()
    for key in keys_list:
        address, result, tx_hash = repay_asset(key, args[0], args[1])
        msg_string = f"Wallet {address}\n\n"
        msg_string += f"{result} - {tx_hash}\n"

        await bot.send_message(
            message.from_user.id,
            msg_string,
        )


@dp.message_handler(commands=["addLiq"])
async def process_balances_command(message: types.Message):
    await run_script(message)
    args = message.text.split(" ")[1:]
    keys_list = get_private_keys()
    for key in keys_list:
        address, result, tx_hash = add_liquidity(
            key, args[0], args[1], args[2], float(args[3])
        )
        msg_string = f"Wallet {address}\n\n"
        msg_string += f"{result} - {tx_hash}\n"

        await bot.send_message(
            message.from_user.id,
            msg_string,
        )


@dp.message_handler(content_types=ContentType.ANY)
async def unknown_message(msg: types.Message):
    message_text = text(
        ("Ya xz chto eto i zachem ti eto vvel."),
        ("Uzay"),
        code("/help"),
    )
    await msg.reply(message_text, parse_mode=ParseMode.MARKDOWN)
