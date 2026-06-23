# OLA Ride Insights

## Project Overview
A comprehensive data analysis project on OLA ride-sharing data to extract 
meaningful business insights using Python, SQL, Power BI, and Streamlit. 
This project covers end-to-end data analysis — from raw data cleaning to 
interactive web dashboard deployment.

---

## Objectives
- Analyze OLA ride data to identify booking trends and patterns
- Perform data cleaning and preprocessing for accurate analysis
- Execute SQL queries for structured data exploration
- Build interactive Power BI dashboard for visual insights
- Deploy a Streamlit web application for real-time data exploration

---

## Tech Stack
| Technology | Purpose |
|------------|---------|
| Python (Pandas, Matplotlib, Seaborn) | Data cleaning & EDA |
| SQL (SQLite) | Structured data querying |
| Power BI | Interactive dashboard |
| Streamlit | Web application deployment |
| Jupyter Notebook | Exploratory Data Analysis |

---

## Project Structure
| File | Description |
|------|-------------|
| `OLA_DataSet.xlsx` | Original raw dataset |
| `OLA_Cleaned.csv` | Cleaned and processed dataset |
| `OLA_Cleaned.ipynb` | Jupyter Notebook with EDA + SQL analysis |
| `OLA.pbix` | Power BI Dashboard file |
| `app.py` | Streamlit Web Application |

---

## Key Analysis Performed
- Ride volume trends across different time periods
- Peak hours and high-demand zones identification
- Driver performance and rating analysis
- Revenue and fare distribution insights
- Cancellation patterns and reasons analysis
- Customer behavior and booking preferences

---

##  How to Run the Streamlit App
```bash
pip install streamlit pandas matplotlib seaborn
streamlit run app.py
