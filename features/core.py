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
    return round(sum(purchase["amount"] for purchase in purchases), 2)


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


def filter_by_category(purchases, category):
    category = category.strip().lower()

    return [
        purchase for purchase in purchases
        if purchase.get("category", "").lower() == category
    ]


def search_purchases(purchases, search_term):
    search_term = search_term.strip().lower()

    return [
        purchase for purchase in purchases
        if search_term in purchase["name"].lower()
    ]


def category_breakdown(purchases):
    breakdown = {}

    for purchase in purchases:
        category = purchase.get("category", "Uncategorized")
        breakdown[category] = breakdown.get(category, 0) + purchase["amount"]

    return {
        category: round(amount, 2)
        for category, amount in breakdown.items()
    }


def last_purchase(purchases):
    return purchases[-1] if purchases else None


def spending_summary(purchases):
    if not purchases:
        return {
            "total": 0.0,
            "count": 0,
            "average": 0.0
        }

    total = calculate_total(purchases)

    return {
        "total": total,
        "count": len(purchases),
        "average": round(total / len(purchases), 2)
    }