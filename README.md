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

---

## Project Structure


BloodIQ/
│
├── app.py
├── templates/
│ ├── index.html
│ ├── diabetes.html
│ ├── cbc.html
│ └── blood_pressure.html
│
├── static/
├── requirements.txt
