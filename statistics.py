
def calculate_income(transactions: list) -> float :
    """
    Calculates income from transactions
    Args:
        transactions: list of transactions
    Returns:
        Sum amount of income
    """
    
    return sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "income"
    )


def calculate_expenses(transactions: list) -> float:
    """
    Calculates expense from transactions
    Args:
        transactions: list of transactions
    Returns:
        Sum amount of expenses
    """
    return sum(
        transaction["amount"]
        for transaction in transactions
        if transaction["type"] == "expense"
    )


def calculate_balance(transactions: list) -> float:
    """
    Calculates total balance from transactions
    Args:
        transactions: list of transactions
    Returns:
        Balance
    """
    return calculate_income(transactions) - calculate_expenses(transactions)


def filter_by_category(transactions: list, category: str) -> list:
    """
    Filters transactions by category
    Args:
        transactions: List of transactions
        category: Category to which filter by
    Returns:
        Filtered transaction list
    """
    return [
        transaction
        for transaction in transactions
        if transaction["category"].casefold() == category.casefold()
    ]
