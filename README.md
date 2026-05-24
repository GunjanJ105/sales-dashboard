# 📊 Sales Analytics Dashboard

An interactive Sales Analytics Dashboard built with **Python**, **Streamlit**, and **Plotly** — analyzing 9,994 sales records with dynamic filters, KPI cards, and multiple visualizations.

🔗 **Live Demo**: [Click here to view the app](https://share.streamlit.io) <!-- Replace with your actual Streamlit Cloud link -->

---

## 📸 Features

- 📌 **KPI Cards** — Total Sales, Total Profit, Total Orders at a glance
- 📈 **Monthly Revenue Trend** — Line chart showing sales over months
- 🗂️ **Sales by Category** — Bar chart comparing product categories
- 🌍 **Profit Heatmap** — Region-wise and category-wise profit breakdown
- 🔍 **Dynamic Filters** — Filter by Region and Category from the sidebar

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core programming language |
| Streamlit | Web app framework |
| Pandas | Data loading and manipulation |
| Plotly | Interactive charts |
| Git & GitHub | Version control |

---

## 📁 Project Structure

```
sales-dashboard/
├── app.py                    # Main Streamlit app
├── utils.py                  # Data loading helper
├── requirements.txt          # Dependencies
├── data/
│   └── Sample - Superstore.csv   # Dataset
└── README.md
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
```

---

## 📊 Dataset

- **Source**: [Superstore Sales Dataset — Kaggle](https://www.kaggle.com/datasets/vivek468/superstore-dataset-final)
- **Records**: 9,994 rows
- **Columns used**: Order Date, Region, Category, Sales, Profit, Quantity

---

## 👤 Author

**Gunjan Jain**  
📧 gunjanjain1005@gmail.com  
🔗 [LinkedIn](https://linkedin.com) <!-- Replace with your actual LinkedIn URL -->  
🐙 [GitHub](https://github.com/GunjanJ105)
