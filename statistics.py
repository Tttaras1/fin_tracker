"""Calculate totals and filter financial transactions."""

def calculate_income(transactions):
    """Return the sum of amounts for income transactions.

    Args:
        transactions: Transaction dictionaries containing ``type`` and ``amount``.
    """
    return sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "income"
    )


def calculate_expenses(transactions):
    """Return the sum of amounts for expense transactions.

    Args:
        transactions: Transaction dictionaries containing ``type`` and ``amount``.
    """
    return sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "expense"
    )


def calculate_balance(transactions):
    """Return total income minus total expenses.

    Args:
        transactions: Transaction dictionaries to calculate the balance from.
    """
    return calculate_income(transactions) - calculate_expenses(transactions)


def filter_by_category(transactions, category):
    """Return transactions whose category matches, ignoring letter case.

    Args:
        transactions: Transaction dictionaries to filter.
        category: Category name to match.
    """
    return [
        transaction
        for transaction in transactions
        if transaction["category"].casefold() == category.casefold()
    ]
