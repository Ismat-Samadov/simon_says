# Financial Analyst Telegram Bot

A hybrid Telegram bot that combines pre-generated analytics insights with AI-powered chat capabilities using Google's Gemini API.

## Features

### Analytics Features
- Account balance overview
- Transaction trends and patterns
- Spending breakdown by category
- Monthly financial summaries
- Top transactions analysis
- Interactive charts and visualizations

### AI Chat Features
- Natural conversation with Gemini AI
- Context-aware financial advice
- Integration with your financial data
- Persistent chat history
- Smart detection of financial queries

## Project Structure

```
analyst_in_pocket/
├── bot.py                  # Main bot application
├── config.py              # Configuration management
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables
│
├── database/              # Database layer
│   ├── __init__.py
│   ├── connection.py      # Database connection handler
│   └── models.py          # SQLAlchemy models
│
├── analytics/             # Analytics engine
│   ├── __init__.py
│   ├── insights.py        # Analytics insights generation
│   └── charts.py          # Chart generation
│
└── chatbot/               # AI chatbot
    ├── __init__.py
    └── gemini_client.py   # Gemini API integration
```

## Setup Instructions

### 1. Prerequisites

- Python 3.8 or higher
- PostgreSQL database
- Telegram Bot Token
- Google Gemini API Key

### 2. Clone and Install

```bash
# Clone the repository (if applicable)
cd analyst_in_pocket

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On macOS/Linux:
source venv/bin/activate
# On Windows:
# venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt
```

### 3. Configure Environment Variables

Edit the `.env` file with your credentials:

```env
DATABASE_URL="your_postgresql_connection_string"
TELEGRAM_BOT_TOKEN="your_telegram_bot_token"
GEMINI_API_KEY="your_gemini_api_key"
ADMIN_USER_IDS="comma_separated_admin_ids"
```

#### Getting Your Credentials:

**Telegram Bot Token:**
1. Open Telegram and search for `@BotFather`
2. Send `/newbot` and follow the instructions
3. Copy the token provided

**Gemini API Key:**
1. Visit https://makersuite.google.com/app/apikey
2. Create a new API key
3. Copy the key

**Database URL:**
- Use your PostgreSQL connection string
- Format: `postgresql://user:password@host:port/database?schema=schema_name`

### 4. Initialize Database

The bot will automatically create necessary tables on first run. Ensure your PostgreSQL database is accessible and the schema specified in the DATABASE_URL exists.

### 5. Run the Bot

```bash
python bot.py
```

You should see:
```
INFO - Initializing database...
INFO - Starting bot...
```

## Usage Guide

### Bot Commands

#### General Commands
- `/start` - Start the bot and see welcome message
- `/help` - Display all available commands

#### Analytics Commands
- `/analytics` - Open interactive analytics dashboard
- `/summary` - Get quick monthly financial summary
- `/balance` - View account balance overview
- `/spending` - See spending breakdown by category
- `/trends` - View transaction trends
- `/top` - See top transactions

#### Chat Commands
- `/chat` - Activate chat mode
- `/ask [question]` - Ask a specific question
- `/clear` - Clear chat history

### Using Analytics

1. Send `/analytics` to open the interactive menu
2. Click on any button to view specific analytics
3. Charts will be generated and sent as images
4. Text summaries are provided alongside visualizations

### Using the Chat Feature

**Simple Chat:**
Just send any message to the bot and it will respond using AI.

**Financial Questions:**
The bot automatically detects financial keywords and includes your data context in the conversation.

Example:
```
You: How much did I spend this month?
Bot: Based on your data, you spent $X this month...
```

**Ask Command:**
```
/ask What's a good savings rate?
/ask How can I reduce my spending?
```

## Database Schema

The bot uses the following tables in the `demo_bank` schema:

- **users** - Telegram user information
- **accounts** - Bank accounts
- **transactions** - Financial transactions
- **chat_history** - Conversation history

## Analytics Available

1. **Monthly Summary**
   - Total income
   - Total expenses
   - Net savings
   - Transaction count

2. **Account Overview**
   - Total balance across accounts
   - Individual account balances
   - Account types

3. **Spending Analysis**
   - Breakdown by category
   - Pie chart visualization
   - Top spending categories

4. **Transaction Trends**
   - Daily transaction patterns
   - Income vs. expenses over time
   - 30-day trends

5. **Balance Trends**
   - Daily balance changes
   - Account balance history

6. **Top Transactions**
   - Largest transactions
   - By type (credit/debit)
   - With descriptions and dates

## Development

### Adding New Analytics

1. Add new method to `analytics/insights.py`:
```python
@staticmethod
def get_new_insight() -> Dict:
    # Your analytics logic
    pass
```

2. Add chart generation in `analytics/charts.py`:
```python
def create_new_chart(self, data) -> io.BytesIO:
    # Your chart logic
    pass
```

3. Add command handler in `bot.py`:
```python
async def new_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Handle command
    pass
```

### Customizing the Chatbot

Edit the `system_prompt` in `chatbot/gemini_client.py` to customize the AI assistant's personality and behavior.

## Troubleshooting

### Database Connection Issues
- Verify DATABASE_URL is correct
- Ensure PostgreSQL is running
- Check schema exists in database

### Bot Not Responding
- Verify TELEGRAM_BOT_TOKEN is correct
- Check bot is running (`python bot.py`)
- Ensure bot is not blocked

### Gemini API Errors
- Verify GEMINI_API_KEY is valid
- Check API quota limits
- Ensure internet connection

### Chart Generation Issues
- Ensure matplotlib backend is set correctly
- Check sufficient disk space for temp files
- Verify all chart dependencies installed

## Security Notes

- Never commit `.env` file to version control
- Keep API keys secure
- Use environment variables for sensitive data
- Restrict admin commands to authorized users

## License

This project is provided as-is for educational and personal use.

## Support

For issues or questions:
1. Check the troubleshooting section
2. Review error logs
3. Verify all dependencies are installed correctly
