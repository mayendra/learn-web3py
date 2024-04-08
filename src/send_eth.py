from web3 import Web3

# connect to ganache 
ganache_url = 'HTTP://127.0.0.1:7545'
we3 = Web3(Web3.HTTPProvider(ganache_url))

# first account / sender account
sender_acc = '0x6294fa353CBF40634da8550Dc88e90A44E8A1f13'
private_key = '0x5cb02db5f2ce47b505601fd2d27a0cbe3449fc1c29e2f07b242437a0f8ce2e54'

# second account / recepient acc
recepient_acc = '0xDEf41dD96ffA0d072c93B769e967A82D589320e9'

# get nonce
nonce = we3.eth.get_transaction_count(sender_acc)

# build transactions 
transaction = {
    'nonce' : nonce,
    'to': recepient_acc,
    'value' : we3.to_wei(1,'ether'),
    'gas' : 200000,
    'gasPrice' : we3.to_wei('50','gwei')
}

# sign transaction
signed_tx = we3.eth.account.sign_transaction(transaction, private_key)

# get transaction hash
tx_hash = we3.eth.send_raw_transaction(signed_tx.rawTransaction)
print(we3.to_hex(tx_hash))
