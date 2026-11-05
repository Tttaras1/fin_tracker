"""Create, display, and delete financial transactions."""

transactions = []
last_id = 0


def add_transaction(
    transactions: list,
    transaction_type: str,
    amount: float,
    category: str,
    description: str,
) -> None | list:
    """Validate and append a transaction to ``transactions``.

    Args:
        transactions: Existing transaction dictionaries to append to.
        transaction_type: Transaction type, either ``"income"`` or ``"expense"``.
        amount: Positive transaction amount.
        category: Non-empty transaction category.
        description: Non-empty transaction description.

    Returns:
        The updated list, or ``None`` if the input fails validation.
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


def show_transactions(transactions):
    """Print transactions in a fixed-width table."""
    fields = ["id", "type", "amount", "category", "description"]
    column_width = 16

    for field in fields:
        print(f"{field.upper():^{column_width - 1}}|", end="")

    print("\n", "-" * column_width * len(fields))

    for transaction in transactions:
        for field in fields:
            print(f"{str(transaction[field]):^{column_width - 1}}|", end="")

        print()


show_transactions([])


def delete_transaction(transactions, transaction_id):
    """Delete and return the transaction list, reporting if the ID is absent.

    Args:
        transactions: Transaction dictionaries to search and update.
        transaction_id: ID of the transaction to delete.

    Returns:
        The updated list of transactions.
    """
    for transaction in transactions:
        if transaction["id"] == transaction_id:
            transactions.remove(transaction)
            print(f"Transaction with ID {transaction_id} deleted")
            return transactions

    print(f"Couldn't find transaction with id {transaction_id}")
    return transactions
