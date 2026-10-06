import streamlit as st
import pandas as pd
from datetime import date
from database import create_table, add_expense, get_expenses
from ai_insights import generate_insight

create_table()

st.title("Smart Expense Tracker with AI")

st.subheader("Monthly Budget")

budget = st.number_input(
    "Enter your monthly budget",
    min_value=0.0,
    step=100.0
)

st.subheader("Add Expense")
col1, col2 = st.columns(2)
with col1:
    expense_date = st.date_input("Date", value=date.today())

with col2:
    amount = st.number_input(
        "Amount",
        min_value=0.0,
        step=10.0
    )
col1, col2 = st.columns(2)

with col1:
    category = st.selectbox(
    "Category",
    ["Food", "Transport", "Education", "Shopping", "Entertainment", "Other"]
)
with col2:
    payment_method = st.selectbox(
        "Payment Method",
        ["UPI", "Cash", "Card", "Other"]
    )
description = st.text_input("Description")
if st.button("➕ Add Expense", use_container_width=True):
    if amount <= 0:
        st.error("Please enter an amount greater than 0.")
    else:
        add_expense(
            str(expense_date),
            amount,
            category,
            description,
            payment_method
        )

        st.success("Expense saved successfully!")
st.subheader("Expense History")

expenses = get_expenses()

if expenses:
    for expense in expenses:
        st.write(
            f"₹{expense[2]} | {expense[3]} | "
            f"{expense[5]} | {expense[4]} | {expense[1]}"
        )
else:
    st.info("No expenses found.") 


st.subheader("Dashboard")



expenses = get_expenses()

if expenses:
    total_spending = sum(expense[2] for expense in expenses)
    total_transactions = len(expenses)

    col1, col2, col3 = st.columns(3)

    col1.metric("Total Spending", f"₹{total_spending:.2f}")
    col2.metric("Total Transactions", total_transactions)

    if budget > 0:
        remaining_budget = budget - total_spending

        col3.metric(
            "Remaining Budget",
            f"₹{remaining_budget:.2f}"
        )
    category_data = {}

    for expense in expenses:
        category = expense[3]
        amount = expense[2]

        if category in category_data:
            category_data[category] += amount
        else:
            category_data[category] = amount

    chart_data = pd.DataFrame(
        list(category_data.items()),
        columns=["Category", "Amount"]
    )

    st.subheader("Category-wise Spending")
    st.bar_chart(chart_data.set_index("Category"))
else:
    st.info("No expenses available for dashboard.")



st.subheader("🤖 AI Spending Insights")

if st.button("Generate AI Insights"):
    with st.spinner("Analyzing your expenses..."):
        insight = generate_insight(expenses)
        st.write(insight) 

st.subheader("📥 Export Expenses")

if expenses:
    export_data = pd.DataFrame(
        expenses,
        columns=[
            "ID",
            "Date",
            "Amount",
            "Category",
            "Description",
            "Payment Method"
        ]
    )

    export_data["Date"] = pd.to_datetime(export_data["Date"]).dt.strftime("%d-%m-%Y")
    csv = export_data.to_csv(index=False)

    st.download_button(
        "Download Expenses as CSV",
        csv,
        "expenses.csv",
        "text/csv"
    )    