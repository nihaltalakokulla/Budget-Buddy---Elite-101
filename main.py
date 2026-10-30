
from features.core import (
    add_purchase,
    calculate_total,
    delete_purchase,
    display_purchases
)

from storage import load_purchases, save_purchases


def main():
    purchases = load_purchases()

    while True:
        print("\n====== BUDGETBUDDY ======")
        print("1. Add a purchase")
        print("2. View purchases")
        print("3. View total spending")
        print("4. Delete a purchase")
        print("5. Exit")

        choice = input("\nChoose an option: ").strip()

        if choice == "1":
            name = input("Purchase name: ")

            try:
                amount = float(input("Purchase amount: $"))
                add_purchase(purchases, name, amount)
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
            print("Goodbye!")
            break

        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
