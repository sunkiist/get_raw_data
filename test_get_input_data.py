from web3 import Web3

rpc = "https://bsc-dataseed1.ninicoin.io"
web3 = Web3(Web3.HTTPProvider(rpc))
print(web3.isConnected())
transaction_txn = '0xf4cebed3bf6d96c76bc06f9dde613385ddf1fa9dd4dd83239b4365baadf0deab'

data = web3.eth.getTransaction(transaction_txn)
input = data['input']
print(input)

data = web3.eth.get_transaction_receipt(transaction_txn)
output = data['status']
print(output)