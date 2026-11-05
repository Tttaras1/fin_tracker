transactions = []
last_id = 0


def add_transaction(
    transactions: list,
    transaction_type: str,
    amount: float,
    category: str,
    description: str,
) -> None | list:
    """
    Creates and stores a transaction;

    Args:
        transactions: A list of already existing transactions to add to
        transaction_type: Category of the transaction ( income or expense )
        amount: Sum of the transaction
        category: Category
        description: Description
    """
    if amount <= 0:
        print("Amount should be a positive number!")
        return None
    if transaction_type not in ["income", "expense"]:
        print("Transaction should be either income or expense")
        return None
    if not category or not description:
        print("Category and description shouldn't be empty!")
        return None

    global last_id

    transaction = {
        "id": last_id,
        "type": transaction_type,
        "amount": amount,
        "category": category,
        "description": description,
    }
    last_id += 1
    transactions.append(transaction)

    return transactions


def show_transactions(transactions: list) -> None:
    """
    Show data for all transactions in formatted table
    Args:
        transactions: List of transactions
    Returns:
        None
    """

    fields = ["id", "type", "amount", "category", "description"]
    column_width = 16

    for field in fields:
        print(f"{field.upper():^{column_width - 1}}|", end="")

    print("\n", "-" * column_width * len(fields))

    for transaction in transactions:
        for field in fields:
            print(f"{str(transaction[field]):^{column_width - 1}}|", end="")

        print()


def delete_transaction(transactions: list, transaction_id: str) -> list:
    """
    Deletes transaction from the given list
    Args:
        transactions: List of transaction where to remove transaction from
        transaction_id: Id of the transaction to remove
    Returns:
        List of transations
    """
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            transactions.remove(transaction)
            print(f"Transaction with ID {transaction_id} deleted")
            return transactions

    print(f"Couldn't find transaction with id {transaction_id}")
    return transactions
