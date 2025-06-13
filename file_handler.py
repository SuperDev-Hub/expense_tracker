import os

def save_to_file(transactions, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, "w") as f:
        for t in transactions:
            f.write(str(t) + "\n")

def load_from_file(filename):
    from transaction import Transaction
    transactions = []
    if os.path.exists(filename):
        with open(filename, "r") as f:
            for line in f:
                transactions.append(Transaction.from_string(line))
    return transactions