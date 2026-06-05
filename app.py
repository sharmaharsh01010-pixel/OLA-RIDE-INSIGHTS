import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import sqlite3

# Load Data
df = pd.read_csv("OLA_Cleaned.csv")

# Sidebar
st.sidebar.title("OLA Ride Insights")
page = st.sidebar.selectbox("Select Page", ["Overall", "Vehicle Type", "Revenue", "Cancellation", "Ratings"])

# SQL Connection
conn = sqlite3.connect(":memory:")
df.to_sql("OLA_Cleaned", conn, index=False, if_exists="replace")

# -------------------- OVERALL --------------------
if page == "Overall":
    st.title("OLA Ride Insights Dashboard")
    st.header("Overall Analysis")

    # Ride Volume Over Time
    df['Date'] = pd.to_datetime(df['Date'])
    ride_volume = df.groupby('Date')['Booking_ID'].count()
    fig, ax = plt.subplots()
    ax.plot(ride_volume.index, ride_volume.values, color='green')
    ax.set_title("Ride Volume Over Time")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Rides")
    st.pyplot(fig)

    # Booking Status Breakdown
    st.subheader("Booking Status Breakdown")
    status_counts = df['Booking_Status'].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.pie(status_counts, labels=status_counts.index, autopct='%1.1f%%', startangle=90)
    ax2.set_title("Booking Status Breakdown")
    st.pyplot(fig2)

# -------------------- VEHICLE TYPE --------------------
elif page == "Vehicle Type":
    st.title("Vehicle Type Analysis")

    query = """
        SELECT Vehicle_Type, SUM(Ride_Distance) as Total_Distance
        FROM OLA_Cleaned
        GROUP BY Vehicle_Type
        ORDER BY Total_Distance DESC
        LIMIT 5
    """
    result = pd.read_sql_query(query, conn)
    fig, ax = plt.subplots()
    ax.barh(result['Vehicle_Type'], result['Total_Distance'], color='steelblue')
    ax.set_title("Top 5 Vehicle Types by Ride Distance")
    ax.set_xlabel("Total Ride Distance")
    st.pyplot(fig)

# -------------------- REVENUE --------------------
elif page == "Revenue":
    st.title("Revenue Analysis")

    # Revenue by Payment Method
    st.subheader("Revenue by Payment Method")
    query2 = """
        SELECT Payment_Method, SUM(Booking_Value) as Total_Revenue
        FROM OLA_Cleaned
        GROUP BY Payment_Method
        ORDER BY Total_Revenue DESC
    """
    result2 = pd.read_sql_query(query2, conn)
    fig, ax = plt.subplots()
    ax.barh(result2['Payment_Method'], result2['Total_Revenue'], color='orange')
    ax.set_title("Revenue by Payment Method")
    st.pyplot(fig)

    # Top 5 Customers
    st.subheader("Top 5 Customers by Booking Value")
    query3 = """
        SELECT Customer_ID, SUM(Booking_Value) as Total_Value
        FROM OLA_Cleaned
        GROUP BY Customer_ID
        ORDER BY Total_Value DESC
        LIMIT 5
    """
    result3 = pd.read_sql_query(query3, conn)
    fig2, ax2 = plt.subplots()
    ax2.bar(result3['Customer_ID'], result3['Total_Value'], color='purple')
    ax2.set_title("Top 5 Customers by Booking Value")
    plt.xticks(rotation=45)
    st.pyplot(fig2)

    # Ride Distance Per Day
    st.subheader("Ride Distance Distribution Per Day")
    df['Date'] = pd.to_datetime(df['Date'])
    daily_distance = df.groupby('Date')['Ride_Distance'].sum()
    fig3, ax3 = plt.subplots()
    ax3.plot(daily_distance.index, daily_distance.values, color='teal')
    ax3.set_title("Ride Distance Per Day")
    ax3.set_xlabel("Date")
    ax3.set_ylabel("Total Distance")
    st.pyplot(fig3)

# -------------------- CANCELLATION --------------------
elif page == "Cancellation":
    st.title("Cancellation Analysis")

    # Customer Cancellation
    st.subheader("Cancellation Reasons by Customer")
    customer_cancel = df['Canceled_Rides_by_Customer'].value_counts()
    fig, ax = plt.subplots()
    ax.barh(customer_cancel.index, customer_cancel.values, color='red')
    ax.set_title("Customer Cancellation Reasons")
    st.pyplot(fig)

    # Driver Cancellation
    st.subheader("Cancellation Reasons by Driver")
    driver_cancel = df['Canceled_Rides_by_Driver'].value_counts()
    fig2, ax2 = plt.subplots()
    ax2.barh(driver_cancel.index, driver_cancel.values, color='darkred')
    ax2.set_title("Driver Cancellation Reasons")
    st.pyplot(fig2)

# -------------------- RATINGS --------------------
elif page == "Ratings":
    st.title("Ratings Analysis")

    # Driver Ratings Distribution
    st.subheader("Driver Ratings Distribution")
    fig, ax = plt.subplots()
    ax.hist(df['Driver_Ratings'].dropna(), bins=20, color='blue', edgecolor='black')
    ax.set_title("Driver Ratings Distribution")
    ax.set_xlabel("Rating")
    ax.set_ylabel("Count")
    st.pyplot(fig)

    # Customer vs Driver Ratings
    st.subheader("Customer vs Driver Ratings")
    fig2, ax2 = plt.subplots()
    ax2.scatter(df['Customer_Rating'], df['Driver_Ratings'], alpha=0.3, color='green')
    ax2.set_title("Customer vs Driver Ratings")
    ax2.set_xlabel("Customer Rating")
    ax2.set_ylabel("Driver Rating")
    st.pyplot(fig2)
