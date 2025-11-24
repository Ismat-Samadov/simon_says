"""Script to generate sample data for testing the bot."""

from datetime import datetime, timedelta
import random
from database import get_session, init_db
from database.models import Account, Transaction


def generate_sample_data():
    """Generate sample accounts and transactions."""

    # Initialize database
    init_db()

    with get_session() as session:
        # Check if data already exists
        existing_accounts = session.query(Account).count()
        if existing_accounts > 0:
            print(f"Found {existing_accounts} existing accounts. Skipping data generation.")
            return

        # Create sample accounts
        accounts = [
            Account(
                account_number="ACC001",
                account_type="Checking",
                balance=5000.00,
                currency="USD",
                customer_name="John Doe"
            ),
            Account(
                account_number="ACC002",
                account_type="Savings",
                balance=15000.00,
                currency="USD",
                customer_name="John Doe"
            ),
            Account(
                account_number="ACC003",
                account_type="Credit Card",
                balance=-2500.00,
                currency="USD",
                customer_name="John Doe"
            )
        ]

        session.add_all(accounts)
        session.flush()

        # Transaction categories
        expense_categories = [
            'Groceries', 'Restaurants', 'Transportation', 'Entertainment',
            'Utilities', 'Healthcare', 'Shopping', 'Travel', 'Education'
        ]

        income_categories = [
            'Salary', 'Freelance', 'Investment', 'Bonus', 'Gift'
        ]

        # Generate transactions for the last 60 days
        transactions = []
        base_date = datetime.utcnow() - timedelta(days=60)

        for account in accounts:
            balance = account.balance

            # Generate 30-50 transactions per account
            num_transactions = random.randint(30, 50)

            for i in range(num_transactions):
                days_offset = random.randint(0, 60)
                trans_date = base_date + timedelta(days=days_offset)

                # More expenses than income
                if random.random() < 0.7:  # 70% expenses
                    trans_type = 'debit'
                    amount = round(random.uniform(10, 500), 2)
                    category = random.choice(expense_categories)
                    balance -= amount
                else:  # 30% income
                    trans_type = 'credit'
                    amount = round(random.uniform(100, 2000), 2)
                    category = random.choice(income_categories)
                    balance += amount

                description = f"{trans_type.title()} transaction - {category}"

                transaction = Transaction(
                    account_id=account.id,
                    transaction_type=trans_type,
                    amount=amount,
                    description=description,
                    category=category,
                    transaction_date=trans_date,
                    balance_after=balance
                )
                transactions.append(transaction)

            # Update final account balance
            account.balance = balance

        session.add_all(transactions)

        print(f"✅ Generated {len(accounts)} accounts and {len(transactions)} transactions!")
        print("\nSample accounts:")
        for acc in accounts:
            print(f"  - {acc.account_number} ({acc.account_type}): ${acc.balance:,.2f}")


if __name__ == '__main__':
    print("Generating sample data...")
    generate_sample_data()
    print("\nDone! You can now test the bot with sample data.")
