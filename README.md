# Mev-Sniper

Bot MEV canggih buat Ethereum mainnet. Konek ke node Geth lokal lewat IPC socket, terus kirim bundle lewat relay Flashbots.

## Fitur

- Koneksi Geth IPC socket, ada fallback ke HTTP
- Integrasi relay Flashbots (`eth_sendBundle`, `eth_sendPrivateTransaction`)
- Scanning mempool buat cari peluang arbitrase & sandwich
- Bundle builder, support multi-tx
- Retry otomatis kalau relay timeout
- Threshold profit & gas cap bisa diatur

## Requirements

- Python 3.10+
- Geth node (fully synced, IPC enabled)
- Flashbots signer key
- Ethereum RPC endpoint

## Installation
```
git clone https://github.com/Boiescylosh/Mev-Sniper
cd Mev-Sniper
chmod +x setup.sh bot.sh
./setup.sh
pip install -r requirements.txt
```

## Trobleshooting
```
export ANDROID_API_LEVEL=24
pip install rpds-py
pip install -r requirements.txt
```
kalo web3 bentrok sama flashbots pake ini
```
pip install web3 flashbots python-dotenv pyyaml requests
```
## Usage 
```
./bot.sh
```
