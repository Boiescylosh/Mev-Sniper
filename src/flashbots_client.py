import os
import json
import requests
from eth_account import Account
from eth_account.messages import encode_defunct


class FlashbotsClient:
    def __init__(self, config):
        self.relay = config["flashbots"]["relay"]
        self.signer_key = os.getenv("FLASHBOTS_SIGNER_KEY")
        self.account = Account.from_key(self.signer_key) if self.signer_key else None

    def _sign(self, body):
        message = encode_defunct(text=body)
        signed = self.account.sign_message(message)
        return f"{self.account.address}:{signed.signature.hex()}"

    def send_bundle(self, txs, target_block):
        body = json.dumps({
            "jsonrpc": "2.0",
            "id": 1,
            "method": "eth_sendBundle",
            "params": [{
                "txs": txs,
                "blockNumber": hex(target_block),
            }],
        })
        headers = {
            "Content-Type": "application/json",
            "X-Flashbots-Signature": self._sign(body),
        }
        print("[*] Sending bundle via eth_sendBundle")
        try:
            r = requests.post(self.relay, data=body, headers=headers, timeout=5)
            return r.json()
        except requests.Timeout:
            print("[!] Relay timeout, retrying...")
            return {"error": "timeout"}
