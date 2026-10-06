**# Smart Expense Tracker with AI**
**## Project Description**

Smart Expense Tracker with AI is a Python-based web application that helps users record, manage, and analyze their daily expenses.

The application uses SQLite to store expenses and Google Gemini AI to provide simple spending insights and saving suggestions.

## Features

- Add and store daily expenses
- Set a monthly budget
- Track total spending
- View remaining budget
- View expense history
- Analyze category-wise spending
- Generate AI-powered spending insights
- Export expenses as CSV
- Simple and user-friendly Streamlit interface

## Technologies Used

- Python
- Streamlit
- SQLite
- Pandas
- Google Gemini AI
- python-dotenv
- Matplotlib
- Scikit-learn

## Project Structure

```text
my_project/
│
├── main.py
├── database.py
├── analytics.py
├── ai_insights.py
├── requirements.txt
├── .env
├── .gitignore
└── data/
    └── expenses.db
```

### File Description

- `main.py` — Main Streamlit application
- `database.py` — Handles SQLite database operations
- `analytics.py` — Used for expense analysis
- `ai_insights.py` — Generates AI spending insights
- `requirements.txt` — Contains required Python packages
- `.env` — Stores the Gemini API key
- `data/expenses.db` — Stores expense records

## How to Run the Project

### 1. Open the project folder

Open the project in VS Code.

### 2. Activate the virtual environment

Open the VS Code terminal and run:

```bash
.venv\Scripts\activate
```

### 3. Install the required packages

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
python -m streamlit run main.py
```

The application will open in your web browser.

## Environment Variable

Create a `.env` file and add your Gemini API key:

```text
GEMINI_API_KEY=your_api_key_here
```

Never share your API key publicly.

## Future Enhancements

- Add expense prediction using Machine Learning
- Add receipt image scanning using OCR
- Add automatic expense category prediction
- Add charts for monthly and yearly spending
- Add user login and authentication
- Add cloud database support
- Add voice-based expense entry

## Conclusion

Smart Expense Tracker with AI provides a simple way to record expenses, monitor a monthly budget, understand spending patterns, and receive AI-based saving suggestions.

The project combines Python, Streamlit, SQLite, and Google Gemini AI to create a practical and user-friendly expense management application.