# Mev-Sniper

Advanced MEV bot for Ethereum mainnet. Connects to a local Geth node via IPC socket and submits bundles through the Flashbots relay.

## Features

- Geth IPC socket connection with HTTP fallback
- Flashbots relay integration (`eth_sendBundle`, `eth_sendPrivateTransaction`)
- Mempool scanning for arbitrage & sandwich opportunities
- Bundle builder with multi-tx support
- Automatic retry on relay timeout
- Configurable profit threshold & gas cap

## Requirements

- Python 3.10+
- Geth node (fully synced, IPC enabled)
- Flashbots signer key
- Ethereum RPC endpoint
  

## Installation

```bash
git clone https://github.com/Boiescylosh/Mev-Sniper.git
cd Mev-Sniper
chmod +x setup.sh bot.sh
./setup.sh
