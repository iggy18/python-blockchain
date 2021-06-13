from client import Client, Transaction, transactions, display_transaction

seth = Client()
maddy = Client()
mom = Client()
dad = Client()

t1 = Transaction(
    seth,
    maddy.identity,
    100.0
)
t1.sign_transaction()
transactions.append(t1)


t2 = Transaction(
    seth,
    maddy.identity,
    82.0
)
t2.sign_transaction()
transactions.append(t2)


t3 = Transaction(
    seth,
    maddy.identity,
    27.0
)
t3.sign_transaction()
transactions.append(t3)


t4 = Transaction(
    dad,
    mom.identity,
    15.0
)
t4.sign_transaction()
transactions.append(t4)


t5 = Transaction(
    mom,
    dad.identity,
    300.0
)
t5.sign_transaction()
transactions.append(t5)

for transaction in transactions:
    display_transaction(transaction)
    print('-----------------------------')