## Требования

- Python 3.10 и выше

## Функционал

Программа может выполнять следующие функции:
- Свап KISS <-> токен из поддерживаемых `[страница Swaps]`
- Депозит/вывод токенов из хранилища `[страница Deposit]`
- Заем/возврат токенов `[страница Borrow]`
- Добавление ликвидности `[страница Pool]`

Список поддерживаемых токенов:

| token  | address                                    |
| ------ | ------------------------------------------ |
| KISS   | 0xAcF353630a688e0fAbCb68AbbdB59A8e3f482656 |
| DAI    | 0x3451E572ebD8bc292097593361744a1f8E321d8A | 
| krETH  | 0x3b96b644CAe06987A4f2133F1E146c7dE5ceF3ac |
| krBTC  | 0x6a6A2f61a665B817DA48F0356C47406BD03127c3 |
| krXAU  | 0xFC382404b498f891377d7C2C62d24b61407F7A7a |
| krWTI  | 0x65b301612C9Ca76ccB495722D7F02CD3acab5d2e |
| krTSLA | 0x7Df1BE079F99066117F8214656B005068Ef2cA5F |


## Предварительная настройка

1. Скачать архив
2. Создать виртуальное окружение

```python
python -m vevn .
```

3.  Активировать окружение
   
   ```python
source Scripts/activate
```

4. Установить библиотеки
   
```python
pip install -r requirements.txt
```

5. Поместить RPC, API ключ от бота в телеге и ваш ID (если собираетесь запускать через тг
6. Поместить приватники в файл _setup/private_keys.txt
   
## Запуск скрипта

### Запуск из ТГ

ВАЖНО! Управление из телеги идет по всем приватникам из файла private_keys.txt
1. Перед началом требуется создать бота в телеграмме, выполнить настройку и внести API ключ в конфиг. 
2. Запуск бота командой:
```python
python run_bot.py
```

3. Список модулей

| Команда запуска    | Функционал                                      |
| ------------------ | ----------------------------------------------- |
| /test              | Проверка работоспособности                      |
| /balances          | Вывод баланса поддерживаемых токенов (далее ПТ) |
| /approveAllSwap    | Апрув всех ПТ для свапов                        |
| /approveAllDeposit | Апрув всех ПТ для депозитов                     |
| /approveAllLiq     | Апрув всех ПТ для добавления ликв               |
| /swapFromKiss      | Свап KISS -> ПТ                                 | 
| /swapToKiss        | Свап ПТ -> KISS                                 |
| /deposit           | Ввод токена из списка ПТ в хранилище            |
| /withdrawal        | Вывод токена из списка ПТ из хранилища          |
| /borrow            | Заем токена из списка ПТ                        |
| /repay             | Возврат токена из списка ПТ                     |
| /addLiq            | Добавление ликвидности                          |

4. Запуск модулей

Вывод баланса поддерживаемых токенов (далее ПТ)
```python
/balances
```

Апрув всех ПТ для свапов
```python
/approveAllSwap
```

Апрув всех ПТ для депозитов
```python
/approveAllDeposit
```

Апрув всех ПТ для добавления ликв
```python
/approveAllLiq
```

Свап KISS -> ПТ
```python
/swapFromKiss [название токена] [кол-во] [отношение к KISS]

# Свап 10 KISS в krETH
/swapFromKiss krETH 10 2625
```
![[Pasted image 20230302175807.png]]

Свап ПТ -> KISS
```python
/swapToKiss [название токена] [кол-во] [отношение к KISS]

# Свап 0.01 krETH в KISS
/swapToKiss krETH 0.01 2625
```

Ввод токена из списка ПТ в хранилище
```python
/deposit [название токена] [кол-во]

# Депозит 10 KISS 
/deposit KISS 10
```

Вывод токена из списка ПТ из хранилища
```python
/withdrawal [название токена] [кол-во]

# Вывод 10 KISS 
/withdrawal KISS 10
```

Заем токена из списка ПТ
```python
/borrow [название токена] [кол-во]

# Заем 10 KISS 
/borrow KISS 10
```

Возврат токена из списка ПТ
```python
/repay [название токена] [кол-во]

# Возврат 10 KISS 
/repay KISS 10
```

Добавление ликвидности
```python
/addLiq [название токена A] [название токена B] [кол-во токена B] [отношение к KISS]

# Добавление в пул krETH-KISS 1 KISS-X krETH
/addLiq krETH KISS 1 2588
```


### Запуск из командной строки

#### Запуск 1 приватника

Вывод баланса поддерживаемых токенов (далее ПТ)
```python
python run_solo.py -m balances -pk [приватник]
```

Апрув всех ПТ для свапов
```python
python run_solo.py -m approve_swaps -pk [приватник]
```

Апрув всех ПТ для депозитов
```python
python run_solo.py -m approve_deposits -pk [приватник]
```

Апрув всех ПТ для добавления ликв
```python
python run_solo.py -m approve_liquidity -pk [приватник]
```

Свап KISS -> ПТ
```python
python run_solo.py -m swap_from_kiss -pk [приватник] -tn [название токена] -tv [кол-во] -r [отношение к KISS]

# Свап 10 KISS в krETH
python run_solo.py -m swap_from_kiss -pk [приватник] -tn krETH -tv 10 -r 2661
```
![[kiss_rate.png]]

Свап ПТ -> KISS
```python
python run_solo.py -m swap_to_kiss -pk [приватник] -tn [название токена] -tv [кол-во] -r [отношение к KISS]

# Свап 0.01 krETH в KISS
python run_solo.py -m swap_to_kiss -pk [приватник] -tn krETH -tv 0.01 -r 2661
```

Ввод токена из списка ПТ в хранилище
```python
python run_solo.py -m deposit -pk [приватник] -tn [название токена] -tv [кол-во]

# Депозит 10 KISS 
python run_solo.py -m deposit -pk [приватник] -tn KISS -tv 10
```

Вывод токена из списка ПТ из хранилища
```python
python run_solo.py -m withdrawal -pk [приватник] -tn [название токена] -tv [кол-во]

# Вывод 10 KISS 
python run_solo.py -m withdrawal -pk [приватник] -tn KISS -tv 10
```

Заем токена из списка ПТ
```python
python run_solo.py -m borrow -pk [приватник] -tn [название токена] -tv [кол-во]

# Заем 10 KISS 
python run_solo.py -m borrow -pk [приватник] -tn KISS -tv 10
```

Возврат токена из списка ПТ
```python
python run_solo.py -m repay -pk [приватник] -tn [название токена] -tv [кол-во]

# Возврат 10 KISS 
python run_solo.py -m repay -pk [приватник] -tn KISS -tv 10
```

Добавление ликвидности
```python
python run_solo.py -m add_liq -pk [приватник] -ta [токен A] -tb [токен B] -tv [кол-во токена B] -r [отношение к KISS] 

# Добавление в пул krETH-KISS 1 KISS-X krETH
python run_solo.py -m add_liq -pk [приватник] -ta krETH -tb KISS -tv 1 -r 2661 
```

#### Запуск всех приватников из private_keys.txt

Для запуска модулей к каждому приватнику во всех командах выше нужно заменить `run_solo.py` на `run_batch.py` и убрать аргумент `-pk [приватник]`
Пример депозита:

Ввод токена из списка ПТ в хранилище
```python
python run_batch.py -m deposit -tn [название токена] -tv [кол-во]

# Депозит 10 KISS 
python run_batch.py -m deposit -tn KISS -tv 10
```

Для всех остальных подмодулей аналогично.

Author: https://t.me/vladweat
Public: https://t.me/importweb3
Donat any evm: 0x350e3c095Ba01BD018C60E3cABCdfeAf5C4D3834
