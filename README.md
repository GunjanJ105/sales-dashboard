# 📊 Sales Analytics Dashboard

An interactive, company-grade Sales Analytics Dashboard built with **Python**, **Streamlit**, and **Plotly** — analyzing 9,994 sales records with dynamic filters, KPI cards, live currency rates, and real-time job postings.

🔗 **Live Demo**: [Click here to view the app](https://sales-dashboard-hxyu4pxpmzxkktdqyxpnra.streamlit.app)

---

## 📸 Features

- 📌 **KPI Cards** — Total Sales, Total Profit, Total Orders at a glance
- 📈 **Monthly Revenue Trend** — Line chart showing sales over months
- 🗂️ **Sales by Category** — Bar chart comparing product categories
- 🌍 **Profit Heatmap** — Region-wise and category-wise profit breakdown using Plotly
- 🔍 **Dynamic Filters** — Filter by Region and Category from the sidebar
- 🗃️ **SQL Layer** — Data stored and queried using SQLite via Pandas `read_sql`
- 💱 **Live Currency Rates** — Real-time USD exchange rates fetched via ExchangeRate API
- 💼 **Live Job Postings** — Remote Python/Data jobs scraped live using BeautifulSoup

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Streamlit | Web app framework |
| Pandas | Data loading and manipulation |
| Plotly | Interactive charts and heatmap |
| SQLite + SQL | Structured data storage and querying |
| Requests | Fetching live API data |
| BeautifulSoup | Web scraping job postings |
| Git & GitHub | Version control and deployment |

---

## 📁 Project Structure

```
sales-dashboard/
├── app.py                          # Main Streamlit app
├── utils.py                        # Data loading + SQLite helper
├── api.py                          # Live currency exchange rate API
├── scraper.py                      # Job postings web scraper
├── requirements.txt                # Dependencies
├── .gitignore
├── README.md
└── data/
    └── Sample - Superstore.csv     # Dataset
```

---

## 🚀 Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/GunjanJ105/sales-dashboard.git
cd sales-dashboard
```

**2. Install dependencies**
```bash
pip install -r requirements.txt
```

**3. Run the app**
```bash
streamlit run app.py
```

Opens at `http://localhost:8501`

---

## 📦 Requirements

```
streamlit
pandas
plotly
openpyxl
matplotlib
requests
beautifulsoup4
```

---

## 📊 Dataset

- **Source**: [Superstore Sales Dataset — Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Records**: 9,994 rows
- **Columns used**: Order Date, Region, Category, Sales, Profit, Quantity

---

## 🔌 API Used

- **ExchangeRate API** — [api.exchangerate-api.com](https://api.exchangerate-api.com/v4/latest/USD)
- Free, no API key required
- Displays live rates for INR, EUR, GBP, JPY, AUD

---

## 🕸️ Web Scraping

- Scrapes live remote job postings from **RemoteOK**
- Keyword filter: Python, Data Analyst, SQL, Streamlit
- Displays top 10 jobs with title, company, tags and link

---

## 👤 Author

**Gunjan Jain**  
📧 gunjanjain1005@gmail.com  
🐙 [GitHub](https://github.com/GunjanJ105)
