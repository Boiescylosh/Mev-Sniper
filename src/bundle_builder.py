class BundleBuilder:
    def __init__(self, config):
        self.max_txs = config["mev"]["max_bundle_txs"]
        self.min_profit = config["mev"]["min_profit_eth"]

    def build(self, opportunity):
        print("[*] Building bundle...")
        txs = opportunity.get("txs", [])
        if len(txs) > self.max_txs:
            txs = txs[: self.max_txs]
        print(f"[+] Bundle built with {len(txs)} txs")
        return txs
