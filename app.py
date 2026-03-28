from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/diabetes')
def diabetes_page():
    return render_template('diabetes.html')


@app.route('/cbc')
def cbc_page():
    return render_template('cbc.html')


@app.route('/blood-pressure')
def bp_page():
    return render_template('blood_pressure.html')


@app.route('/predict/diabetes', methods=['POST'])
def analyze_diabetes():
    data = request.json

    glucose = float(data.get('glucose', 100))
    bmi = float(data.get('bmi', 25))
    age = float(data.get('age', 30))
    bp = float(data.get('bp', 80))
    insulin = float(data.get('insulin', 80))
    skin = float(data.get('skin', 20))
    pedigree = float(data.get('pedigree', 0.5))
    pregnancies = float(data.get('pregnancies', 0))

    risk_score = (
        (glucose / 200) * 35 +
        (bmi / 50) * 25 +
        (age / 80) * 15 +
        (bp / 120) * 10 +
        (pedigree * 10) +
        (insulin / 300) * 5
    )

    risk_score = min(risk_score, 100)

    if risk_score < 30:
        level = "Low Risk"
        color = "green"
        message = "Your health indicators look stable. Maintain a healthy lifestyle."
    elif risk_score < 55:
        level = "Moderate Risk"
        color = "orange"
        message = "Some values are slightly elevated. Consider improving diet and activity."
    else:
        level = "High Risk"
        color = "red"
        message = "Multiple risk factors detected. Medical consultation is recommended."

    return jsonify({
        'risk': level,
        'score': round(risk_score, 1),
        'color': color,
        'advice': message
    })


@app.route('/predict/cbc', methods=['POST'])
def analyze_cbc():
    data = request.json

    rbc = float(data.get('rbc', 4.5))
    wbc = float(data.get('wbc', 7000))
    hgb = float(data.get('hgb', 14))
    hct = float(data.get('hct', 42))
    platelets = float(data.get('plt', 250))
    mcv = float(data.get('mcv', 90))

    detected_issues = []

    if hgb < 12:
        detected_issues.append("Low hemoglobin – possible anemia")

    if wbc > 11000:
        detected_issues.append("High WBC – possible infection")

    if wbc < 4000:
        detected_issues.append("Low WBC – possible immune weakness")

    if platelets < 150:
        detected_issues.append("Low platelets – possible clotting issue")

    if platelets > 400:
        detected_issues.append("High platelets – possible abnormal clotting")

    if rbc < 4.0:
        detected_issues.append("Low RBC – possible anemia or blood loss")

    if mcv < 80:
        detected_issues.append("Low MCV – possible iron deficiency")

    if mcv > 100:
        detected_issues.append("High MCV – possible vitamin B12 deficiency")

    if not detected_issues:
        status = "Normal"
        color = "green"
        message = "All values are within the healthy range."
    elif len(detected_issues) == 1:
        status = "Mild Concern"
        color = "orange"
        message = "One irregular value detected. Monitor and consult if needed."
    else:
        status = "Needs Attention"
        color = "red"
        message = "Multiple irregular values found. Medical advice is recommended."

    return jsonify({
        'status': status,
        'color': color,
        'issues': detected_issues,
        'message': message
    })


@app.route('/predict/bp', methods=['POST'])
def analyze_bp():
    data = request.json

    age = float(data.get('age', 30))
    stress = float(data.get('stress', 5))
    sleep = float(data.get('sleep', 7))
    exercise = float(data.get('exercise', 3))
    salt = float(data.get('salt', 3))
    smoking = float(data.get('smoking', 0))
    alcohol = float(data.get('alcohol', 0))
    weight = float(data.get('weight', 70))
    height = float(data.get('height', 170))

    bmi = weight / ((height / 100) ** 2)

    risk_score = (
        (age / 80) * 20 +
        (stress / 10) * 20 +
        ((8 - sleep) / 8) * 15 +
        ((5 - exercise) / 5) * 15 +
        (salt / 5) * 10 +
        (smoking * 10) +
        (alcohol / 2) * 5 +
        ((bmi - 18) / 22) * 5
    )

    risk_score = max(0, min(risk_score, 100))

    systolic = int(100 + risk_score * 0.6)
    diastolic = int(65 + risk_score * 0.35)

    if systolic < 120 and diastolic < 80:
        category = "Normal"
        color = "green"
        advice = "Your blood pressure is healthy. Keep it up."
    elif systolic < 130:
        category = "Elevated"
        color = "yellow"
        advice = "Slightly elevated. Reduce salt and stay active."
    elif systolic < 140:
        category = "Stage 1 Hypertension"
        color = "orange"
        advice = "Lifestyle changes needed. Consider medical guidance."
    else:
        category = "Stage 2 Hypertension"
        color = "red"
        advice = "High risk. Seek medical attention."

    return jsonify({
        'category': category,
        'color': color,
        'systolic': systolic,
        'diastolic': diastolic,
        'score': round(risk_score, 1),
        'advice': advice,
        'bmi': round(bmi, 1)
    })


if __name__ == '__main__':
    app.run(debug=True, port=5000)
