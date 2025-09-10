# 🛒 Sales Data Analysis Project  

![Main Dashboard Preview](src/screenshots/Screenshot%202025-09-10%20222530.png) 
## 📌 Project Overview  
This project analyzes **retail sales data** to uncover business insights such as sales trends, top-performing products, and customer behavior. It includes **exploratory data analysis (EDA)**, **customer segmentation**, and an **interactive dashboard** for visualizing key metrics.  

---

## 🎯 Objectives  
- Clean and preprocess raw sales transaction data.  
- Explore sales patterns across products, customers, and time.  
- Segment customers using **RFM analysis / clustering techniques**.  
- Build an interactive dashboard for business intelligence.  

---

## ⚙️ Technologies Used  
- **Python** 🐍  
- **Pandas, NumPy** → Data preprocessing & analysis  
- **Matplotlib, Seaborn, Plotly** → Data visualization  
- **Scikit-learn** → Customer segmentation (KMeans / RFM analysis)  
- **Streamlit / Dash** → Interactive dashboard  
- **OpenPyXL** → Excel file handling  

---

## 📂 Project Structure  
sales_data_analysis/
│── data/ # Dataset folder (raw & processed data)
│ ├── Online_Retail.xlsx
│ └── processed/
│
│── src/ # Source code
│ ├── eda.py # Exploratory Data Analysis
│ ├── customer_segmentation.py # Customer segmentation
│ └── dashboard.py # Interactive dashboard
│
│── requirements.txt # Python dependencies
│── README.md # Project documentation
│── .gitignore # Ignore unnecessary files

yaml
Copy code

---

## 🚀 How to Run the Project  

### 1. Clone the repository  
```bash
git clone https://github.com/your-username/sales-data-analysis.git
cd sales-data-analysis
2. Create and activate a virtual environment
bash
Copy code
python -m venv venv
# On Mac/Linux
source venv/bin/activate
# On Windows
venv\Scripts\activate
3. Install dependencies
bash
Copy code
pip install -r requirements.txt
4. Run Exploratory Data Analysis (EDA)
bash
Copy code
python src/eda.py
5. Run the Dashboard
bash
Copy code
streamlit run src/dashboard.py
📊 Key Insights You’ll Get
Revenue trends over time

Best-selling products and top customers

Customer segmentation (loyal, new, at-risk, lost)

Interactive dashboard for exploring sales KPIs

📸 Example Dashboard Screenshot
<img width="1919" height="915" alt="Screenshot 2025-09-10 222530" src="src/screenshots/Screenshot 2025-09-10 222424.png" />
<img width="1919" height="755" alt="Screenshot 2025-09-10 222518" src="https://github.com/user-attachments/assets/fd4d82a8-96d1-4a5d-a2a2-32e73ed9fe91" />
<img width="1919" height="789" alt="Screenshot 2025-09-10 222424" src="https://github.com/user-attachments/assets/c658d302-683c-4538-bca7-1753b775558f" />
