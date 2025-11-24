"""Analytics insights generation module."""

from datetime import datetime, timedelta
from typing import Dict, List, Any
import pandas as pd
from sqlalchemy import func, desc
from database.models import Transaction, Account
from database.connection import get_session


class AnalyticsEngine:
    """Engine for generating analytics insights."""

    @staticmethod
    def get_account_summary() -> Dict[str, Any]:
        """Get summary of all accounts."""
        with get_session() as session:
            accounts = session.query(Account).all()

            total_balance = sum(acc.balance for acc in accounts)
            account_count = len(accounts)

            return {
                'total_balance': total_balance,
                'account_count': account_count,
                'accounts': [
                    {
                        'account_number': acc.account_number,
                        'type': acc.account_type,
                        'balance': acc.balance,
                        'customer': acc.customer_name
                    }
                    for acc in accounts
                ]
            }

    @staticmethod
    def get_transaction_trends(days: int = 30) -> pd.DataFrame:
        """Get transaction trends for the specified number of days."""
        with get_session() as session:
            start_date = datetime.utcnow() - timedelta(days=days)

            transactions = session.query(Transaction).filter(
                Transaction.transaction_date >= start_date
            ).all()

            if not transactions:
                return pd.DataFrame()

            df = pd.DataFrame([
                {
                    'date': t.transaction_date,
                    'amount': t.amount,
                    'type': t.transaction_type,
                    'category': t.category
                }
                for t in transactions
            ])

            df['date'] = pd.to_datetime(df['date'])
            return df

    @staticmethod
    def get_spending_by_category(days: int = 30) -> Dict[str, float]:
        """Get spending breakdown by category."""
        with get_session() as session:
            start_date = datetime.utcnow() - timedelta(days=days)

            results = session.query(
                Transaction.category,
                func.sum(Transaction.amount).label('total')
            ).filter(
                Transaction.transaction_date >= start_date,
                Transaction.transaction_type == 'debit'
            ).group_by(Transaction.category).all()

            return {
                category or 'Uncategorized': float(total)
                for category, total in results
            }

    @staticmethod
    def get_monthly_summary() -> Dict[str, Any]:
        """Get current month's financial summary."""
        with get_session() as session:
            # Get first day of current month
            now = datetime.utcnow()
            first_day = datetime(now.year, now.month, 1)

            transactions = session.query(Transaction).filter(
                Transaction.transaction_date >= first_day
            ).all()

            total_income = sum(
                t.amount for t in transactions
                if t.transaction_type == 'credit'
            )
            total_expenses = sum(
                t.amount for t in transactions
                if t.transaction_type == 'debit'
            )

            return {
                'month': now.strftime('%B %Y'),
                'total_income': total_income,
                'total_expenses': total_expenses,
                'net': total_income - total_expenses,
                'transaction_count': len(transactions)
            }

    @staticmethod
    def get_top_transactions(limit: int = 10, transaction_type: str = None) -> List[Dict[str, Any]]:
        """Get top transactions by amount."""
        with get_session() as session:
            query = session.query(Transaction)

            if transaction_type:
                query = query.filter(Transaction.transaction_type == transaction_type)

            transactions = query.order_by(desc(Transaction.amount)).limit(limit).all()

            return [
                {
                    'id': t.id,
                    'amount': t.amount,
                    'type': t.transaction_type,
                    'category': t.category,
                    'description': t.description,
                    'date': t.transaction_date.strftime('%Y-%m-%d %H:%M')
                }
                for t in transactions
            ]

    @staticmethod
    def get_daily_balance_trend(days: int = 30) -> pd.DataFrame:
        """Get daily balance trends."""
        with get_session() as session:
            start_date = datetime.utcnow() - timedelta(days=days)

            transactions = session.query(Transaction).filter(
                Transaction.transaction_date >= start_date
            ).order_by(Transaction.transaction_date).all()

            if not transactions:
                return pd.DataFrame()

            df = pd.DataFrame([
                {
                    'date': t.transaction_date,
                    'balance': t.balance_after
                }
                for t in transactions if t.balance_after is not None
            ])

            df['date'] = pd.to_datetime(df['date']).dt.date
            # Get last balance of each day
            df = df.groupby('date').last().reset_index()
            return df

    @staticmethod
    def get_insights_text() -> str:
        """Generate a text-based insights summary."""
        summary = AnalyticsEngine.get_monthly_summary()
        account_summary = AnalyticsEngine.get_account_summary()
        spending = AnalyticsEngine.get_spending_by_category()

        text = f"""
📊 **Financial Insights Summary**

**This Month ({summary['month']})**
💰 Total Income: ${summary['total_income']:,.2f}
💸 Total Expenses: ${summary['total_expenses']:,.2f}
📈 Net: ${summary['net']:,.2f}
🔢 Transactions: {summary['transaction_count']}

**Account Overview**
🏦 Total Balance: ${account_summary['total_balance']:,.2f}
📋 Active Accounts: {account_summary['account_count']}

**Top Spending Categories**
"""
        for i, (category, amount) in enumerate(sorted(spending.items(), key=lambda x: x[1], reverse=True)[:5], 1):
            text += f"{i}. {category}: ${amount:,.2f}\n"

        return text.strip()
