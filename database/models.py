"""Database models for the Analyst Bot."""

from datetime import datetime
from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()


class User(Base):
    """User model for storing bot users."""

    __tablename__ = 'users'
    __table_args__ = {'schema': 'demo_bank'}

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, unique=True, nullable=False)
    username = Column(String(255))
    first_name = Column(String(255))
    last_name = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)
    last_active = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __repr__(self):
        return f"<User(telegram_id={self.telegram_id}, username={self.username})>"


class Account(Base):
    """Bank account model."""

    __tablename__ = 'accounts'
    __table_args__ = {'schema': 'demo_bank'}

    id = Column(Integer, primary_key=True)
    account_number = Column(String(50), unique=True, nullable=False)
    account_type = Column(String(50))
    balance = Column(Float, default=0.0)
    currency = Column(String(10), default='USD')
    customer_name = Column(String(255))
    created_at = Column(DateTime, default=datetime.utcnow)

    transactions = relationship("Transaction", back_populates="account")

    def __repr__(self):
        return f"<Account(account_number={self.account_number}, balance={self.balance})>"


class Transaction(Base):
    """Transaction model."""

    __tablename__ = 'transactions'
    __table_args__ = {'schema': 'demo_bank'}

    id = Column(Integer, primary_key=True)
    account_id = Column(Integer, ForeignKey('demo_bank.accounts.id'), nullable=False)
    transaction_type = Column(String(50))  # credit, debit, transfer
    amount = Column(Float, nullable=False)
    description = Column(Text)
    category = Column(String(100))
    transaction_date = Column(DateTime, default=datetime.utcnow)
    balance_after = Column(Float)

    account = relationship("Account", back_populates="transactions")

    def __repr__(self):
        return f"<Transaction(id={self.id}, type={self.transaction_type}, amount={self.amount})>"


class ChatHistory(Base):
    """Chat history model for storing conversation context."""

    __tablename__ = 'chat_history'
    __table_args__ = {'schema': 'demo_bank'}

    id = Column(Integer, primary_key=True)
    telegram_id = Column(Integer, nullable=False)
    role = Column(String(50))  # user, assistant
    message = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<ChatHistory(telegram_id={self.telegram_id}, role={self.role})>"
