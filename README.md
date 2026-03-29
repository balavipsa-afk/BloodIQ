# 🩸 BloodIQ – Health Risk Analysis System

## Overview
BloodIQ is a web-based application that helps users understand their health using basic medical and lifestyle inputs. It analyzes data such as blood reports and vital parameters to estimate risks related to diabetes, CBC abnormalities, and blood pressure.

The system converts complex health data into simple, easy-to-understand insights, making it accessible even for non-medical users.

---

## Features

### Diabetes Risk Checker
- Calculates risk score based on health inputs  
- Classifies into Low, Moderate, or High risk  
- Provides basic lifestyle guidance  

### CBC Analyzer
- Evaluates blood report values (RBC, WBC, Hemoglobin, etc.)  
- Detects abnormal ranges  
- Lists possible health concerns  

### Blood Pressure Predictor
- Uses lifestyle and physical inputs  
- Estimates systolic and diastolic values  
- Categorizes blood pressure levels  

---

## Tech Stack

- Backend: Python, Flask  
- Frontend: HTML, CSS, JavaScript  
- Data Exchange: JSON
- Logic Processing: Prolog (SWI-Prolog) – used for rule-based medical inference  

---

## **How to Use and Test the Application**

### **Run the Application**
1. Start the Flask server:

python app.py

2. Open your browser and go to:

http://127.0.0.1:5000/


---

### **Using the Application**

#### **1. Home Page**
- Navigate to different modules:
- Diabetes Risk Checker  
- CBC Analyzer  
- Blood Pressure Predictor  

---

#### **2. Diabetes Risk Checker**
- Enter values such as glucose, BMI, age, etc.  
- Click **Analyse Risk**  
- View risk level, score, and advice  

#### **3. CBC Analyzer**
- Enter blood report values (RBC, WBC, Hemoglobin, etc.)  
- Click **Analyse Report**  
- View detected issues and summary  

---

#### **4. Blood Pressure Predictor**
- Enter lifestyle and physical details  
- Click **Analyse**  
- View estimated BP, category, and recommendations  

---

### **Testing the Application**

- Test with normal and extreme input values  
- Leave some fields empty to check default handling  
- Verify API responses in browser console (optional)  
- Ensure results update dynamically without page reload  

---

### **Expected Output**

- Clear risk classification (Low / Moderate / High)  
- List of detected issues (for CBC)  
- Estimated blood pressure values  
- Basic health guidance


  ## Screenshots

![Home](Screenshot%202026-03-28%20194958.png)

![Diabetes](Screenshot%202026-03-28%20195012.png)

![CBC](Screenshot%202026-03-28%20195042.png)

![BP](Screenshot%202026-03-28%20195116.png)


