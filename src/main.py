import os
import sys
import time
import random
import argparse
import yaml
from dotenv import load_dotenv

from geth_client import GethClient
from flashbots_client import FlashbotsClient
from bundle_builder import BundleBuilder


GREEN = "\033[1;32m"
YELLOW = "\033[1;33m"
BLUE = "\033[1;34m"
CYAN = "\033[1;36m"
RED = "\033[1;31m"
WHITE = "\033[1;37m"
PURPLE = "\033[1;35m"
NC = "\033[0m"


def load_config(path):
    with open(path, "r") as f:
        return yaml.safe_load(f)


def rand_hash():
    return "0x" + os.urandom(32).hex()


def rand_range(a, b):
    return random.randint(a, b)


def bot_ts():
    return time.strftime("%H:%M:%S")


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--config", default="config/config.yaml")
    args = parser.parse_args()

    load_dotenv()
    config = load_config(args.config)

    geth = GethClient(config)
    if not geth.connect():
        print(f"{RED}[!] Cannot connect to Geth. Continuing in simulation mode.{NC}")

    block = geth.get_block_number()
    peers = geth.get_peer_count()
    print(f"{BLUE}[i] Block: {block} | Peers: {peers}{NC}")
    print("─" * 60)

    flashbots = FlashbotsClient(config)
    print(f"{YELLOW}[{bot_ts()}] Flashbots relay: {flashbots.relay}{NC}")
    print(f"{YELLOW}[{bot_ts()}] Auth header: X-Flashbots-Signature OK{NC}")
    print("─" * 60)

    builder = BundleBuilder(config)
    print(f"{PURPLE}[{bot_ts()}] Scanning mempool...{NC}")

    total = 0
    for batch in range(5):
        total += rand_range(800, 1500)
        print(f"{PURPLE}[{bot_ts()}] Scanned {total} txs | pending={rand_range(100,400)} | checking MEV...{NC}")
        for _ in range(rand_range(3, 6)):
            h = rand_hash()[:10]
            gwei = rand_range(5, 200)
            roll = random.randint(0, 99)
            if roll < 80:
                status = f"{YELLOW}No MEV value{NC}"
            elif roll < 95:
                status = f"{BLUE}Low MEV value{NC}"
            else:
                status = f"{RED}Potential MEV!{NC}"
            print(f"  --> Checked tx {BLUE}{h}...{NC} | GasPrice: {gwei:>3} Gwei | {status}")
            time.sleep(0.2)

    print(f"{RED}[{bot_ts()}] OPPORTUNITY: {rand_hash()[:10]}...{NC}")
    print(f"{WHITE}[{bot_ts()}]   DEX: Uniswap v3 (Router2){NC}")
    print(f"{WHITE}[{bot_ts()}]   GasPrice: {rand_range(40,120)} Gwei{NC}")
    profit = f"1.{rand_range(100,900)}"
    usd = float(profit) * 2600
    print(f"{GREEN}[{bot_ts()}]   Est. Profit: {profit} ETH (${usd:.2f}){NC}")

    target_block = block + 1
    txs = ["0x" + os.urandom(32).hex() for _ in range(3)]
    bundle = builder.build({"txs": txs})
    bundle_hash = rand_hash()[:14]
    print(f"{GREEN}[{bot_ts()}] Bundle built: {bundle_hash}{NC}")

    print(f"{CYAN}[{bot_ts()}] Sending bundle via eth_sendBundle{NC}")
    print(f"{CYAN}[{bot_ts()}] Target block: {target_block}{NC}")
    resp = flashbots.send_bundle(bundle, target_block)
    print(f"{GREEN}[{bot_ts()}] Relay response: {resp}{NC}")

    print(f"{YELLOW}[{bot_ts()}] Waiting for block {target_block}...{NC}")
    time.sleep(3)
    print(f"{GREEN}[{bot_ts()}] Bundle included in block {target_block}{NC}")
    print()

    print(f"{YELLOW}Loading complete.{NC}")
    print()
    print(f"{WHITE}Press ENTER to continue...{NC}")
    input()

    os.system("clear")
    print()
    print(f"{RED}⚠️  WARNING: BOT ERROR! ⚠️{NC}")
    print(f"{RED}{'═' * 58}{NC}")
    print()
    print(f"{WHITE}Berharap kaya secara instan itu\nmustahil ya ajg, awokwokwok\ningin langsung jackpot porto lu?\nmain polymarket aja sono,\nbiar kayak bandar judi gayanya.{NC}")
    print()
    print(f"{CYAN}{'═' * 58}{NC}")
    print()
    print(f"{CYAN}Sebenarnya aing teh bisa buat bot\ntrading biar mantau antrian transaksi\ndi jaringan blockchain sebelum lu konfirmasi,\njadi pas ada whale mau beli koin\nbot ini bisa mendeteksi secara real-time.{NC}")
    print()
    print(f"{YELLOW}{'═' * 58}{NC}")
    print()
    print(f"{YELLOW}██╗  ██╗ █████╗ ███████╗██╗ █████╗ ███╗   ██╗{NC}")
    print(f"{GREEN}██║ ██╔╝██╔══██╗██╔════╝██║██╔══██╗████╗  ██║{NC}")
    print(f"{YELLOW}█████╔╝ ███████║███████╗██║███████║██╔██╗ ██║{NC}")
    print(f"{GREEN}██╔═██╗ ██╔══██║╚════██║██║██╔══██║██║╚██╗██║{NC}")
    print(f"{YELLOW}██║  ██╗██║  ██║███████║██║██║  ██║██║ ╚████║{NC}")
    print(f"{GREEN}╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝{NC}")
    print()
    print(f"{RED}           Mental Instan = Cuan Ghaib!       {NC}")
    print()


if __name__ == "__main__":
    main()
