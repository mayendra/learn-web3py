# Setup
from web3 import Web3

alchemy_url = "https://eth-mainnet.g.alchemy.com/v2/d8uuI1l_QlaJ4YunN3yvaifo_vJCWnvA"
w3 = Web3(Web3.HTTPProvider(alchemy_url))

# Print if web3 is successfully connected
print(w3.is_connected())

# Get the latest block number
latest_block = w3.eth.get_block("latest")
print(latest_block)

# get the block number 
block_number = w3.eth.block_number
print(block_number)