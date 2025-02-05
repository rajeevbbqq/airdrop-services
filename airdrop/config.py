NETWORK = {
    "name": "test",
    "http_provider": "https://ropsten.infura.io",
    "ws_provider": "wss://ropsten.infura.io/ws",
    "db": {
        "DB_DRIVER": "mysql+pymysql",
        "DB_HOST": "localhost",
        "DB_USER": "unittest_root",
        "DB_PASSWORD": "unittest_pwd",
        "DB_NAME": "airdrop_unittest_db",
        "DB_PORT": 3306,
        "DB_LOGGING": True,
    },
}

BALANCE_DB_CONFIG = {
    "DB_DRIVER": "mysql+pymysql",
    "DB_HOST": "localhost",
    "DB_USER": "unittest_root",
    "DB_PASSWORD": "unittest_pwd",
    "DB_NAME": "token_balances",
    "DB_PORT": 3306,
    "DB_LOGGING": True,
}

NETWORK_ID = 3
SLACK_HOOK = {
    "hostname": "",
    "port": 443,
    "path": "",
    "method": "POST",
    "headers": {"Content-Type": "application/json"},
    "channel_name": ""
}

SIGNER_PRIVATE_KEY = 'AIRDROP_SIGNER_PRIVATE_KEY'
SIGNER_PRIVATE_KEY_STORAGE_REGION = ''

MAX_STAKE_LIMIT = 25000


class AirdropStrategy:
    AGIX = "AGIX"
