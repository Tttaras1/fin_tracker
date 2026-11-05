import transactions as transaction_module
import statistics as statistics_module
def main():
    while True:
        print(
            "\n========== FINANCE MANAGER ==========\n\n"
            "1. Додати дохід\n"
            "2. Додати витрату\n"
            "3. Переглянути всі транзакції\n"
            "4. Показати загальний дохід\n"
            "5. Показати загальні витрати\n"
            "6. Показати поточний баланс\n"
            "7. Фільтрація за категорією\n"
            "0. Вихід\n"
        )
        choice = input("Оберіть дію: ").strip()
        if choice in ("1", "2"):
            transaction_type = "income" if choice == "1" else "expense"
            amount = float(input("Сума: "))
            category = input("Категорія: ").strip()
            description = input("Опис: ").strip()
            transaction_module.add_transaction(
                transaction_module.transactions,
                transaction_type,
                amount,
                category,
                description,
            )
        elif choice == "3":
            transaction_module.show_transactions(transaction_module.transactions)
        elif choice == "4":
            print(f"Загальний дохід: {statistics_module.calculate_income(transaction_module.transactions):.2f}")
        elif choice == "5":
            print(f"Загальні витрати: {statistics_module.calculate_expenses(transaction_module.transactions):.2f}")
        elif choice == "6":
            print(f"Поточний баланс: {statistics_module.calculate_balance(transaction_module.transactions):.2f}")
        elif choice == "7":
            category = input("Категорія: ").strip()
            transaction_module.show_transactions(
                statistics_module.filter_by_category(transaction_module.transactions, category)
            )
        elif choice == "0":
            print("До побачення!")
            break
        else:
            print("Невідома дія. Оберіть пункт від 0 до 7.")
if __name__ == "__main__":
    main()
