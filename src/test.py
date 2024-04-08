from web3 import Web3

ganache_url = 'HTTP://127.0.0.1:7545'
we3 = Web3(Web3.HTTPProvider(ganache_url))

sender = input("masukan address anda : \n")
private_key = input("masukan private key anda : \n")

value = input("masukan saldo ETH yang ingin yang ingin dikirimkan : \n")
resepient = input("masukan address tujuan : \n")

nonce = we3.eth.get_transaction_count(sender)

transaction = {
    'nonce':nonce,
    'to': resepient,
    'value': we3.to_wei(value, 'ether'),
    'gas' : 200000,
    'gasPrice' : we3.to_wei('50','ether')
}

signed_trx = we3.eth.account.sign_transaction(transaction, private_key)

trx_hash =  we3.eth.send_raw_transaction(signed_trx.rawTransaction)
print("transaksi berhasil \n")
print("transaction hash ", we3.to_hex(trx_hash))