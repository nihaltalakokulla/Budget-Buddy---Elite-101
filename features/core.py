
def add_purchase(purchases, name, amount):
    name = name.strip()

    if not name:
        raise ValueError("Purchase name cannot be empty.")

    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")

    purchases.append({
        "name": name,
        "amount": round(float(amount), 2)
    })

    return purchases


def calculate_total(purchases):
    return round(
        sum(purchase["amount"] for purchase in purchases), 2
    )


def delete_purchase(purchases, index):
    if index < 0 or index >= len(purchases):
        raise IndexError("Invalid purchase number.")

    purchases.pop(index)
    return purchases


def display_purchases(purchases):
    if not purchases:
        print("\nNo purchases yet.")
        return

    print("\n--- YOUR PURCHASES ---")

    for i, purchase in enumerate(purchases, start=1):
        print(f"{i}. {purchase['name']} - ${purchase['amount']:.2f}")

    print("----------------------")
    print(f"Total: ${calculate_total(purchases):.2f}")
