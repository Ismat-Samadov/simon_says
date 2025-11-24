"""Chart generation module for analytics visualizations."""

import io
from typing import Dict, List
import matplotlib
matplotlib.use('Agg')  # Use non-GUI backend
import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
from datetime import datetime


class ChartGenerator:
    """Generator for creating analytics charts."""

    def __init__(self):
        """Initialize chart generator with styling."""
        sns.set_style("whitegrid")
        plt.rcParams['figure.figsize'] = (10, 6)
        plt.rcParams['font.size'] = 10

    @staticmethod
    def _save_plot_to_bytes() -> io.BytesIO:
        """Save the current plot to bytes."""
        buf = io.BytesIO()
        plt.tight_layout()
        plt.savefig(buf, format='png', dpi=100, bbox_inches='tight')
        buf.seek(0)
        plt.close()
        return buf

    def create_spending_by_category_chart(self, spending_data: Dict[str, float]) -> io.BytesIO:
        """Create a pie chart for spending by category."""
        if not spending_data:
            # Create empty chart
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, 'No data available',
                   ha='center', va='center', fontsize=14)
            ax.axis('off')
            return self._save_plot_to_bytes()

        categories = list(spending_data.keys())
        amounts = list(spending_data.values())

        fig, ax = plt.subplots()
        colors = sns.color_palette("husl", len(categories))

        wedges, texts, autotexts = ax.pie(
            amounts,
            labels=categories,
            autopct='%1.1f%%',
            colors=colors,
            startangle=90
        )

        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_fontweight('bold')

        ax.set_title('Spending by Category', fontsize=14, fontweight='bold', pad=20)

        return self._save_plot_to_bytes()

    def create_transaction_trend_chart(self, df: pd.DataFrame) -> io.BytesIO:
        """Create a line chart for transaction trends."""
        if df.empty:
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, 'No data available',
                   ha='center', va='center', fontsize=14)
            ax.axis('off')
            return self._save_plot_to_bytes()

        fig, ax = plt.subplots()

        # Group by date and type
        daily_data = df.groupby([df['date'].dt.date, 'type'])['amount'].sum().unstack(fill_value=0)

        daily_data.plot(kind='line', ax=ax, marker='o', linewidth=2)

        ax.set_title('Daily Transaction Trends', fontsize=14, fontweight='bold', pad=20)
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Amount ($)', fontsize=12)
        ax.legend(title='Transaction Type', loc='best')
        ax.grid(True, alpha=0.3)

        plt.xticks(rotation=45)

        return self._save_plot_to_bytes()

    def create_balance_trend_chart(self, df: pd.DataFrame) -> io.BytesIO:
        """Create a chart showing balance over time."""
        if df.empty:
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, 'No data available',
                   ha='center', va='center', fontsize=14)
            ax.axis('off')
            return self._save_plot_to_bytes()

        fig, ax = plt.subplots()

        ax.plot(df['date'], df['balance'], marker='o', linewidth=2, color='#2ecc71')
        ax.fill_between(df['date'], df['balance'], alpha=0.3, color='#2ecc71')

        ax.set_title('Account Balance Trend', fontsize=14, fontweight='bold', pad=20)
        ax.set_xlabel('Date', fontsize=12)
        ax.set_ylabel('Balance ($)', fontsize=12)
        ax.grid(True, alpha=0.3)

        plt.xticks(rotation=45)

        return self._save_plot_to_bytes()

    def create_monthly_comparison_chart(self, df: pd.DataFrame) -> io.BytesIO:
        """Create a bar chart comparing income vs expenses."""
        if df.empty:
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, 'No data available',
                   ha='center', va='center', fontsize=14)
            ax.axis('off')
            return self._save_plot_to_bytes()

        fig, ax = plt.subplots()

        # Group by type
        monthly_data = df.groupby('type')['amount'].sum()

        colors = {'credit': '#2ecc71', 'debit': '#e74c3c', 'transfer': '#3498db'}
        bar_colors = [colors.get(t, '#95a5a6') for t in monthly_data.index]

        monthly_data.plot(kind='bar', ax=ax, color=bar_colors, width=0.6)

        ax.set_title('Income vs Expenses', fontsize=14, fontweight='bold', pad=20)
        ax.set_xlabel('Transaction Type', fontsize=12)
        ax.set_ylabel('Total Amount ($)', fontsize=12)
        ax.grid(True, alpha=0.3, axis='y')

        plt.xticks(rotation=0)

        return self._save_plot_to_bytes()

    def create_top_transactions_chart(self, transactions: List[Dict]) -> io.BytesIO:
        """Create a horizontal bar chart for top transactions."""
        if not transactions:
            fig, ax = plt.subplots()
            ax.text(0.5, 0.5, 'No data available',
                   ha='center', va='center', fontsize=14)
            ax.axis('off')
            return self._save_plot_to_bytes()

        fig, ax = plt.subplots(figsize=(10, 8))

        df = pd.DataFrame(transactions)
        df = df.sort_values('amount', ascending=True)

        colors = {'credit': '#2ecc71', 'debit': '#e74c3c', 'transfer': '#3498db'}
        bar_colors = [colors.get(t, '#95a5a6') for t in df['type']]

        y_labels = [f"{row['category'] or 'N/A'}\n{row['date']}" for _, row in df.iterrows()]

        ax.barh(range(len(df)), df['amount'], color=bar_colors)
        ax.set_yticks(range(len(df)))
        ax.set_yticklabels(y_labels, fontsize=9)

        ax.set_title('Top Transactions', fontsize=14, fontweight='bold', pad=20)
        ax.set_xlabel('Amount ($)', fontsize=12)
        ax.grid(True, alpha=0.3, axis='x')

        return self._save_plot_to_bytes()
