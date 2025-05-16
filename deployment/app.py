import joblib
import streamlit as st
from utils import predict

model_early_screening = joblib.load("../models/Early screening/Early Risk Screening.pkl")
encoder_early_screening = joblib.load("../models/Early screening/Early_Risk_Screening_Encoder.pkl")


model_genetic_tests = joblib.load("../models/Genetic data/Genetic.pkl")
model_clinical_tests = joblib.load("../models/Clinical tests/Clinical tests.pkl")


# --------------------------
# Page Config
# --------------------------
st.set_page_config(page_title="Gastric Cancer Detection", layout="centered")

# --------------------------
# Session State Navigation
# --------------------------
if "page" not in st.session_state:
    st.session_state.page = "Home"

def go_to(page_name):
    st.session_state.page = page_name

# --------------------------
# Sidebar Navigation (Optional)
# --------------------------
st.sidebar.title("Navigation")
if st.sidebar.button("🏠 Home"):
    go_to("Home")
if st.sidebar.button("📑 Model Selection"):
    go_to("Model Selection")
st.sidebar.markdown("""---""")
st.sidebar.markdown("### 👨‍💻 Team Members")
st.sidebar.markdown("""
- Youssef Kotb  
- Ahmed Emad  
- Sara Yasser  
- Basma Khalil
- Shahd Mohamed
""")


# --------------------------
# HOME PAGE
# --------------------------
if st.session_state.page == "Home":


    st.title("Gastric Cancer Detection System")
    st.subheader("Early Detection. Smarter Decisions. Better Outcomes.")
    st.markdown("""
Our AI-powered system leverages clinical data to support medical professionals in identifying gastric cancer risk with improved accuracy and speed.
""")

    st.markdown("### Why It Matters")
    st.markdown("""
Gastric cancer remains one of the leading causes of cancer-related deaths worldwide. Early detection significantly improves survival rates, but current screening methods are:

- Expensive
- Not widely available in low-resource settings
""")

    st.markdown("""Click below to begin:""")
    if st.button("🚀 Try it Now"):
        go_to("Model Selection")
    st.info("This tool is for educational purposes only.")

    st.markdown("""---""")


    st.markdown("""# About the Project""")

    st.markdown("""Gastric cancer remains one of the leading causes of cancer-related deaths worldwide. Early detection significantly improves survival rates, yet current screening methods are often invasive, or unavailable in resource-limited areas.

This project introduces a machine learning-based model trained on clinical and lifestyle features to assess the risk of gastric cancer in patients. By analyzing non-invasive indicators, the model aims to assist healthcare providers in making quicker, data-driven decisions.

The models are trained on real-world, anonymized data using robust algorithms like AdaBoost and  Random Forests.

This system is part of our **graduation project** for the **Data Science and Machine Learning course** under the [Digital Egypt Pioneers Initiative (DEPI)](https://depi.gov.eg/).
    """)

    st.markdown("""---""")
    
    st.markdown("### How It Works")

    st.markdown("We use three models at different stages:")

    st.markdown("**1. Early Screening Model**")
    st.write("Uses lifestyle factors like age, gender, diet, and family history.")

    st.markdown("**2. Genetic Tests Model**")
    st.write("Analyzes genetic markers to confirm cancer at the molecular level.")

    st.markdown("**3. Clinical Tests Model**")
    st.write("Uses lab data and imaging to refine cancer risk evaluation.")


    st.image("images/flow.png", use_container_width=True)  # Optional image

    st.markdown(""" --- """)

    st.markdown(""" # Who can use this? """)
    st.markdown("""
- **Doctors & Clinics**: As a diagnostic support tool for screening patients.
                
- **Researchers**: For analyzing patterns or testing new clinical hypotheses.
                
- **Healthcare Startups**: As a base for building screening platforms. """)
    
    st.markdown(""" --- """)

    st.markdown(""" # Disclaimer""")

    st.markdown("""This tool is for educational and research purposes only. It is not a substitute for professional medical advice, diagnosis, or treatment. Always consult a qualified healthcare provider before making health-related decisions.""")

        
    st.markdown(""" --- """)

    col1, col2 = st.columns([2, 1])
    with col1:
        st.markdown("### Ready to assess your risk?")
    with col2:
        if st.button("🧪 Lets Get Started"):
            go_to("Model Selection")

    # --------------------------
    # FOOTER
    # --------------------------
    st.markdown("""---""")
    st.markdown(
    """
    <div style='text-align: center; font-size: 14px; color: gray;'>
        Made with ❤️ by the DEPI Data Science team<br>
        Special thanks to the <strong>Ministry of Communications and Information Technology (MCIT)</strong>, <strong>Eyouth</strong>, and the <strong>Digital Egypt Pioneers Initiative (DEPI)</strong> for their incredible support.<br><br>
        🔗 <a href="https://depi.gov.eg/" target="_blank">DEPI</a> |
        <a href="https://mcit.gov.eg/" target="_blank">MCIT</a> |
        <a href="https://eyouth.com/" target="_blank">Eyouth</a> |
        <a href="https://github.com/your-project-link" target="_blank">GitHub</a> |
        <a href="https://your-linkedin.com" target="_blank">LinkedIn</a>
    </div>
    """,
    unsafe_allow_html=True
    )

    left_col, center_col, right_col = st.columns([1, 2, 1])

    with left_col:
        st.image("images/DEPI logo.webp", width=100)

    with right_col:
        st.image("images/MCIT.webp", width=100)


# --------------------------
# MODEL SELECTION PAGE
# --------------------------
elif st.session_state.page == "Model Selection":

    st.title("Choose a Model")

    st.markdown("""
    ### 🧭 Model Selection Guide

    Before proceeding, please select one of the three models below.  
    Each is designed to assess gastric cancer risk based on different types of patient data:

    - 🩺 **Early Screening Model**  
    For general checkups using lifestyle and demographic data.

    - 🧬 **Genetic Tests Model**  
    Suitable for patients who have undergone genetic testing.

    - 🧫 **Clinical Tests Model**  
    For those with lab results, imaging, or advanced clinical assessments.

    > 💡 **Tip:** If you're a general user or unsure, start with the **Early Screening Model**.  
    > The other models at this stageare primarily intended for use by medical professionals or researchers.
    """)

    st.markdown("""---""")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.image("images/healthy.webp", width=200)
        st.markdown("### 🩺 Early Screening")
        st.write("Lifestyle & demographic data.")
        if st.button("Select Early Screening"):
            go_to("Early Screening")

    with col2:
        st.image("images/genetic.webp", width=200)
        st.markdown("### 🧬 Genetic Tests")
        st.write("Genetic markers and DNA data.")
        if st.button("Select Genetic Tests"):
            go_to("Genetic Tests")

    with col3:
        st.image("images/doctor.webp", width=200)
        st.markdown("### 🧫 Clinical Tests")
        st.write("Lab & imaging results.")
        if st.button("Select Clinical Tests"):
            go_to("Clinical Tests")


# --------------------------
# EARLY SCREENING MODEL PAGE
# --------------------------
elif st.session_state.page == "Early Screening":
    st.title("🩺 Early Screening Model")
    st.markdown("This model uses demographic and lifestyle factors to estimate your initial risk for gastric cancer.")

    # Inputs
    age = st.number_input("Age", 0, 120)
    gender = st.selectbox("Gender", ["Male", "Female"])
    ethnicity = st.selectbox("Ethnicity", ["Ethnicity_A", "Ethnicity_B", "Ethnicity_C"])
    geographical_location = st.selectbox("Geographical Location", ["Calefornia", "Other"])
    family_history = st.selectbox("Family History of Gastric Cancer?", ["Yes", "No"])
    smoking_habits = st.selectbox("Do you smoke?", ["Yes", "No"])
    alcohol_consumption = st.selectbox("Do you drink alcohol?", ["Yes", "No"])
    helicobacter_pylori_infection = st.selectbox("Helicobacter Pylori Infection?", ["Yes", "No"])
    dietary_habits = st.selectbox("Dietary Habits", ["Low_Salt", "High_Salt"])
    existing_conditions = st.selectbox("Existing Conditions (e.g., ulcers)?", ["No_condition", "Diabetes", "Chronic Gastritis"])

    # Process input to match model format
    input_data = [
        age,
        1 if gender == "Male" else 0,
        ["Ethnicity_A", "Ethnicity_B", "Ethnicity_C"].index(ethnicity),
        1 if geographical_location == "Calefornia" else 0,
        1 if family_history == "Yes" else 0,
        1 if smoking_habits == "Yes" else 0,
        1 if alcohol_consumption == "Yes" else 0,
        1 if helicobacter_pylori_infection == "Yes" else 0,
        1 if dietary_habits == "Low_Salt" else 0,
        ['Chronic Gastritis','Diabetes','No_condition'].index(existing_conditions)
    ]

    if st.button("🔍 Predict Risk"):
        result = predict(model_early_screening, encoder_early_screening,input_data)

        if result:  # High risk
            st.error("🔴 Prediction: High Risk of Gastric Cancer")
            st.markdown("It is advised to proceed with a **Clinical Test** for further evaluation.")
            if st.button("➡️ Go to Clinical Tests"):
                go_to("Clinical Tests")
        else:  # Low risk
            st.success("🟢 Prediction: Low Risk (Safe)")
            st.markdown("You can optionally proceed with **Genetic Testing** for deeper insights.")
            if st.button("➡️ Go to Genetic Tests"):
                go_to("Genetic Tests")
# --------------------------
# GENETIC TESTS MODEL PAGE
# --------------------------
elif st.session_state.page == "Genetic Tests":
    st.title("Genetic Tests Model")
    st.markdown("This model uses genetic markers for risk prediction.")

    # Example inputs
    marker1 = st.number_input("Gene Marker A", 0.0, 100.0)
    marker2 = st.number_input("Gene Marker B", 0.0, 100.0)
    marker3 = st.number_input("Gene Marker C", 0.0, 100.0)

    if st.button("Predict Genetic Test"):
        
        input_data = [marker1, marker2, marker3]
        result = predict(model_genetic_tests, encoder_early_screening ,input_data)
        st.success(f"Prediction: {'🔴 High Risk' if result else '🟢 Low Risk'}")

# --------------------------
# CLINICAL TESTS MODEL PAGE
# --------------------------
elif st.session_state.page == "Clinical Tests":
    st.title("Clinical Tests Model")
    st.markdown("This model uses clinical test results.")

    # Example inputs
    blood_value = st.number_input("Blood Test Value", 0.0, 200.0)
    pressure = st.number_input("Blood Pressure", 50, 200)
    cholesterol = st.number_input("Cholesterol Level", 0.0, 300.0)

    if st.button("Predict Clinical Test"):
        
        input_data = [blood_value, pressure, cholesterol]
        result = predict(model_clinical_tests, input_data)
        st.success(f"Prediction: {'🔴 High Risk' if result else '🟢 Low Risk'}")
