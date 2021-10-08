NETWORK = {
    "name": "test",
    "http_provider": "https://ropsten.infura.io",
    "ws_provider": "wss://ropsten.infura.io/ws",
    "db": {
        "DB_DRIVER": "mysql+pymysql",
        "DB_HOST": "",
        "DB_USER": "",
        "DB_PASSWORD": "",
        "DB_NAME": "",
        "DB_PORT": 3306,
        "DB_LOGGING": False,
    },
}
NETWORK_ID = 3
SLACK_HOOK = {
    "hostname": "",
    "port": 443,
    "path": "",
    "method": "POST",
    "headers": {"Content-Type": "application/json"},
}

SIGNER_PRIVATE_KEY = 'AIRDROP_SIGNER_PRIVATE_KEY'
SIGNER_PRIVATE_KEY_STORAGE_REGION = ''


class AirdropStrategy:
    AGIX = "AGIX"
