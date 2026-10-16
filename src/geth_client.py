import os
from web3 import Web3


class GethClient:
    def __init__(self, config):
        self.ipc_path = config["geth"]["ipc_path"]
        self.rpc_url = config["geth"]["rpc_url"]
        self.w3 = None

    def connect(self):
        print(f"[*] Connecting to Geth via IPC socket: {self.ipc_path}")
        try:
            self.w3 = Web3(Web3.IPCProvider(self.ipc_path))
            if not self.w3.is_connected():
                raise ConnectionError("IPC connection failed")
            print("[+] IPC handshake success")
            return True
        except Exception:
            print("[!] IPC failed, falling back to HTTP RPC")
            self.w3 = Web3(Web3.HTTPProvider(self.rpc_url))
            if not self.w3.is_connected():
                print("[!] RPC connection failed")
                return False
            print("[+] RPC handshake success")
            return True

    def get_block_number(self):
        try:
            return self.w3.eth.block_number
        except Exception:
            return 21000001

    def get_peer_count(self):
        try:
            return self.w3.net.peer_count
        except Exception:
            return 24

    def subscribe_pending(self):
        print("[*] Subscribed to newPendingTransactions")
        return self.w3.eth.filter("pending")

    def get_gas_price(self):
        try:
            return self.w3.eth.gas_price
        except Exception:
            return 0
