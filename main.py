from features.core import (
    add_purchase,
    calculate_total,
    delete_purchase,
    display_purchases,
    filter_by_category,
    search_purchases,
    category_breakdown,
    last_purchase,
    spending_summary
)

from storage import load_purchases, save_purchases


def show_menu():
    print("\n====== BUDGETBUDDY ======")
    print("1. Add a purchase")
    print("2. View purchases")
    print("3. View total spending")
    print("4. Delete a purchase")
    print("5. Filter by category")
    print("6. Search purchases")
    print("7. Show last purchase")
    print("8. Category breakdown")
    print("9. Spending summary")
    print("0. Exit")


def main():
    purchases = load_purchases()

    while True:
        show_menu()
        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            name = input("Purchase name: ")
            category = input("Category: ").strip() or "Uncategorized"

            try:
                amount = float(input("Purchase amount: $"))
                add_purchase(purchases, name, amount)
                purchases[-1]["category"] = category
                save_purchases(purchases)
                print("Purchase added successfully!")

            except ValueError as error:
                print(f"Error: {error}")

        elif choice == "2":
            display_purchases(purchases)

        elif choice == "3":
            print(f"\nTotal spending: ${calculate_total(purchases):.2f}")

        elif choice == "4":
            display_purchases(purchases)

            if purchases:
                try:
                    number = int(input("Purchase number to delete: "))
                    delete_purchase(purchases, number - 1)
                    save_purchases(purchases)
                    print("Purchase deleted successfully!")

                except (ValueError, IndexError) as error:
                    print(f"Error: {error}")

        elif choice == "5":
            category = input("Enter category: ")
            results = filter_by_category(purchases, category)
            display_purchases(results)

        elif choice == "6":
            term = input("Search for a purchase: ")
            results = search_purchases(purchases, term)
            display_purchases(results)

        elif choice == "7":
            purchase = last_purchase(purchases)

            if purchase:
                print(
                    f"\nLast purchase: {purchase['name']} "
                    f"- ${purchase['amount']:.2f}"
                )
            else:
                print("\nNo purchases yet.")

        elif choice == "8":
            breakdown = category_breakdown(purchases)

            if not breakdown:
                print("\nNo purchases to analyze.")
            else:
                print("\n--- CATEGORY BREAKDOWN ---")
                for category, amount in breakdown.items():
                    print(f"{category}: ${amount:.2f}")

        elif choice == "9":
            summary = spending_summary(purchases)

            print("\n--- SPENDING SUMMARY ---")
            print(f"Number of purchases: {summary['count']}")
            print(f"Total spending: ${summary['total']:.2f}")
            print(f"Average purchase: ${summary['average']:.2f}")

        elif choice == "0":
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()