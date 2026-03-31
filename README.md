# 📊 Customer Churn Prediction

## 🚀 Project Overview
Customer churn is a major business challenge where companies lose customers over time.  
This project aims to **predict customer churn** and identify key factors influencing customer retention using Machine Learning.

---

## 🎯 Problem Statement
Develop an end-to-end machine learning system to:
- Predict whether a customer will churn  
- Identify high-risk customers  
- Provide actionable insights to improve retention strategies  

---

## 📂 Dataset
- Customer Churn Dataset  
- Includes:
  - Customer demographics  
  - Account information  
  - Services subscribed  
  - Billing & payment details  

---

## 🧠 Approach

### 🔹 1. Data Cleaning
- Handled missing values  
- Converted data types  
- Removed inconsistencies  

---

### 🔹 2. Exploratory Data Analysis (EDA)

#### 📊 Key Questions Explored:
- What is the overall churn rate?
- Does contract type affect churn?
- Which payment methods lead to higher churn?
- Do high monthly charges increase churn?
- How does tenure impact churn?
- Does tech support reduce churn?

---

### 📈 Key Insights:

- Customers with **month-to-month contracts** show the highest churn  
- **High monthly charges** significantly increase churn probability  
- Customers with **low tenure (0–12 months)** are more likely to churn  
- **Electronic check** payment method has the highest churn rate  
- Lack of **tech support and online security** increases churn  
- **Long-term contracts (1–2 years)** reduce churn significantly  

---

### 🔹 3. Feature Engineering
- Created tenure groups  
- Encoded categorical variables  

---

### 🔹 4. Model Building

Models used:
- Logistic Regression  
- Random Forest   

---

### 📊 Evaluation Metrics:
- Accuracy
- mean-square-error
- root-mean-square-error 
- Precision  
- Recall  
- F1 Score  
- ROC-AUC  

---

## 🏆 Results
- Best Model: **Random Forest  **  
- Achieved strong performance using ROC-AUC and F1-score  
- Improved prediction using feature engineering and tuning  

---

## 📊 Business Insights

### 🚨 Key Drivers of Churn:
- Short-term contracts  
- High pricing  
- Low customer tenure  
- Lack of support services  

---

### ✅ Recommendations:
- Encourage customers to switch to long-term contracts  
- Provide discounts for high-paying customers  
- Improve onboarding for new users  
- Offer free tech support for initial months  

---

## 🖥️ Deployment
- Built an interactive **Streamlit app**  
- Users can input customer details and predict churn in real-time  

---

## 📁 Project Structure

Customer-Churn-Project/
├── data/
├── notebooks/
├── model/
├── app.py
├── requirements.txt
├── README.md

---

## ⚙️ Installation

```bash
pip install -r requirements.txt
streamlit run app.py
```

<img width="1920" height="1080" alt="Screenshot (25)" src="https://github.com/user-attachments/assets/77934da4-2319-4537-a725-d0e612b1a755" />





