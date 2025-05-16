import streamlit as st
import pandas as pd

# Set the title of the app
st.title("Student Dropout Prediction")

st.write("Please enter the student's information below:")

# --- Academic Path Information ---
st.header("Academic Path Information")

# Application mode (Categorical)
application_mode_options = {
    1: "1st phase - general contingent",
    2: "Ordinance No. 612/93",
    5: "1st phase - special contingent (Azores Island)",
    7: "Holders of other higher courses",
    10: "Ordinance No. 854-B/99",
    15: "International student (bachelor)",
    16: "1st phase - special contingent (Madeira Island)",
    17: "2nd phase - general contingent",
    18: "3rd phase - general contingent",
    26: "Ordinance No. 533-A/99, item b2) (Different Plan)",
    27: "Ordinance No. 533-A/99, item b3 (Other Institution)",
    39: "Over 23 years old",
    42: "Transfer",
    43: "Change of course",
    44: "Technological specialization diploma holders",
    51: "Change of institution/course",
    53: "Short cycle diploma holders",
    57: "Change of institution/course (International)"
}
selected_application_mode_desc = st.selectbox("Application Mode", list(application_mode_options.values()))
application_mode = [key for key, value in application_mode_options.items() if value == selected_application_mode_desc][0]


# Application order (Numerical)
application_order = st.number_input("Application Order (0-9)", min_value=0, max_value=9, value=0, step=1)

# Course (Categorical)
course_options = {
    33: "Biofuel Production Technologies",
    171: "Animation and Multimedia Design",
    8014: "Social Service (evening attendance)",
    9003: "Agronomy",
    9070: "Communication Design",
    9085: "Veterinary Nursing",
    9119: "Informatics Engineering",
    9130: "Equinculture",
    9147: "Management",
    9238: "Social Service",
    9254: "Tourism",
    9500: "Nursing",
    9556: "Oral Hygiene",
    9670: "Advertising and Marketing Management",
    9773: "Journalism and Communication",
    9853: "Basic Education",
    9991: "Management (evening attendance)"
}
selected_course_desc = st.selectbox("Course", list(course_options.values()))
course = [key for key, value in course_options.items() if value == selected_course_desc][0]

# Daytime/evening attendance (Categorical)
daytime_evening_attendance = st.radio("Daytime/Evening Attendance", options=[1, 0], format_func=lambda x: "Daytime" if x == 1 else "Evening")

# Previous qualification (Categorical)
previous_qualification_options = {
    1: "Secondary education",
    2: "Higher education - bachelor's degree",
    3: "Higher education - degree",
    4: "Higher education - master's",
    5: "Higher education - doctorate",
    6: "Frequency of higher education",
    9: "12th year of schooling - not completed",
    10: "11th year of schooling - not completed",
    12: "Other - 11th year of schooling",
    14: "10th year of schooling",
    15: "10th year of schooling - not completed",
    19: "Basic education 3rd cycle (9th/10th/11th year) or equiv.",
    38: "Basic education 2nd cycle (6th/7th/8th year) or equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    42: "Professional higher technical course",
    43: "Higher education - master (2nd cycle)"
}
selected_prev_qual_desc = st.selectbox("Previous Qualification", list(previous_qualification_options.values()))
previous_qualification = [key for key, value in previous_qualification_options.items() if value == selected_prev_qual_desc][0]

# Previous qualification (grade) (Numerical)
previous_qualification_grade = st.number_input("Previous Qualification Grade (0-200)", min_value=0, max_value=200, value=0, step=1)

# Admission grade (Numerical)
admission_grade = st.number_input("Admission Grade (0-200)", min_value=0, max_value=200, value=0, step=1)

# Curricular units 1st sem (credited) (Numerical)
curricular_units_1st_sem_credited = st.number_input("Curricular Units 1st Sem (Credited)", min_value=0, value=0, step=1)

# Curricular units 1st sem (enrolled) (Numerical)
curricular_units_1st_sem_enrolled = st.number_input("Curricular Units 1st Sem (Enrolled)", min_value=0, value=0, step=1)

# Curricular units 1st sem (evaluations) (Numerical)
curricular_units_1st_sem_evaluations = st.number_input("Curricular Units 1st Sem (Evaluations)", min_value=0, value=0, step=1)

# Curricular units 1st sem (approved) (Numerical)
curricular_units_1st_sem_approved = st.number_input("Curricular Units 1st Sem (Approved)", min_value=0, value=0, step=1)

# Curricular units 1st sem (grade) (Numerical)
curricular_units_1st_sem_grade = st.number_input("Curricular Units 1st Sem (Grade)", min_value=0.0, value=0.0, step=0.000001)

# Curricular units 1st sem (without evaluations) (Numerical)
curricular_units_1st_sem_without_evaluations = st.number_input("Curricular Units 1st Sem (Without Evaluations)", min_value=0, value=0, step=1)

# Curricular units 2nd sem (credited) (Numerical)
curricular_units_2nd_sem_credited = st.number_input("Curricular Units 2nd Sem (Credited)", min_value=0, value=0, step=1)

# Curricular units 2nd sem (enrolled) (Numerical)
curricular_units_2nd_sem_enrolled = st.number_input("Curricular Units 2nd Sem (Enrolled)", min_value=0, value=0, step=1)

# Curricular units 2nd sem (evaluations) (Numerical)
curricular_units_2nd_sem_evaluations = st.number_input("Curricular Units 2nd Sem (Evaluations)", min_value=0, value=0, step=1)

# Curricular units 2nd sem (approved) (Numerical)
curricular_units_2nd_sem_approved = st.number_input("Curricular Units 2nd Sem (Approved)", min_value=0, value=0, step=1)

# Curricular units 2nd sem (grade) (Numerical)
curricular_units_2nd_sem_grade = st.number_input("Curricular Units 2nd Sem (Grade)", min_value=0.0, value=0.0, step=0.000001)

# Curricular units 2nd sem (without evaluations) (Numerical)
curricular_units_2nd_sem_without_evaluations = st.number_input("Curricular Units 2nd Sem (Without Evaluations)", min_value=0, value=0, step=1)

# Unemployment rate (Numerical)
unemployment_rate = st.number_input("Unemployment Rate (%)", min_value=0.0, value=0.0, step=0.1)

# Inflation rate (Numerical)
inflation_rate = st.number_input("Inflation Rate (%)", min_value=0.0, value=0.0, step=0.1)

# GDP (Numerical)
gdp = st.number_input("GDP", min_value=0.0, value=0.0, step=0.01)

# --- Demographic Information ---
st.header("Demographic Information")

# Marital status (Categorical)
marital_status_options = {
    1: "single",
    2: "married",
    3: "widower",
    4: "divorced",
    5: "facto union",
    6: "legally separated"
}
selected_marital_status_desc = st.selectbox("Marital Status", list(marital_status_options.values()))
marital_status = [key for key, value in marital_status_options.items() if value == selected_marital_status_desc][0]

# Nacionality (Categorical)
nationality_options = {
    1: "Portuguese", 2: "German", 6: "Spanish", 11: "Italian", 13: "Dutch",
    14: "English", 17: "Lithuanian", 21: "Angolan", 22: "Cape Verdean",
    24: "Guinean", 25: "Mozambican", 26: "Santomean", 32: "Turkish",
    41: "Brazilian", 62: "Romanian", 100: "Moldova (Republic of)",
    101: "Mexican", 103: "Ukrainian", 105: "Russian", 108: "Cuban",
    109: "Colombian"
}
selected_nationality_desc = st.selectbox("Nationality", list(nationality_options.values()))
nationality = [key for key, value in nationality_options.items() if value == selected_nationality_desc][0]

# Gender (Categorical)
gender = st.radio("Gender", options=[1, 0], format_func=lambda x: "Male" if x == 1 else "Female")

# Age at enrollment (Numerical)
age_at_enrollment = st.number_input("Age at Enrollment", min_value=0, value=18, step=1)

# International (Categorical)
international = st.radio("International Student", options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")


# --- Social-Economic Factors ---
st.header("Social-Economic Factors")

# Mother's qualification (Categorical)
mother_qualification_options = {
    1: "Secondary Education - 12th Year of Schooling or Eq.",
    2: "Higher Education - Bachelor's Degree",
    3: "Higher Education - Degree",
    4: "Higher Education - Master's",
    5: "Higher Education - Doctorate",
    6: "Frequency of Higher Education",
    9: "12th Year of Schooling - Not Completed",
    10: "11th Year of Schooling - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year of Schooling",
    14: "10th Year of Schooling",
    18: "General commerce course",
    19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
    22: "Technical-professional course",
    26: "7th year of schooling",
    27: "2nd cycle of the general high school course",
    29: "9th Year of Schooling - Not Completed",
    30: "8th year of schooling",
    34: "Unknown",
    35: "Can't read or write",
    36: "Can read without having a 4th year of schooling",
    37: "Basic education 1st cycle (4th/5th year) or equiv.",
    38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    41: "Specialized higher studies course",
    42: "Professional higher technical course",
    43: "Higher Education - Master (2nd cycle)",
    44: "Higher Education - Doctorate (3rd cycle)"
}
selected_mother_qual_desc = st.selectbox("Mother's Qualification", list(mother_qualification_options.values()))
mother_qualification = [key for key, value in mother_qualification_options.items() if value == selected_mother_qual_desc][0]

# Father's qualification (Categorical)
father_qualification_options = {
    1: "Secondary Education - 12th Year of Schooling or Eq.",
    2: "Higher Education - Bachelor's Degree",
    3: "Higher Education - Degree",
    4: "Higher Education - Master's",
    5: "Higher Education - Doctorate",
    6: "Frequency of Higher Education",
    9: "12th Year of Schooling - Not Completed",
    10: "11th Year of Schooling - Not Completed",
    11: "7th Year (Old)",
    12: "Other - 11th Year of Schooling",
    13: "2nd year complementary high school course",
    14: "10th Year of Schooling",
    18: "General commerce course",
    19: "Basic Education 3rd Cycle (9th/10th/11th Year) or Equiv.",
    20: "Complementary High School Course",
    22: "Technical-professional course",
    25: "Complementary High School Course - not concluded",
    26: "7th year of schooling",
    27: "2nd cycle of the general high school course",
    29: "9th Year of Schooling - Not Completed",
    30: "8th year of schooling",
    31: "General Course of Administration and Commerce",
    33: "Supplementary Accounting and Administration",
    34: "Unknown",
    35: "Can't read or write",
    36: "Can read without having a 4th year of schooling",
    37: "Basic education 1st cycle (4th/5th year) or equiv.",
    38: "Basic Education 2nd Cycle (6th/7th/8th Year) or Equiv.",
    39: "Technological specialization course",
    40: "Higher education - degree (1st cycle)",
    41: "Specialized higher studies course",
    42: "Professional higher technical course",
    43: "Higher Education - Master (2nd cycle)",
    44: "Higher Education - Doctorate (3rd cycle)"
}
selected_father_qual_desc = st.selectbox("Father's Qualification", list(father_qualification_options.values()))
father_qualification = [key for key, value in father_qualification_options.items() if value == selected_father_qual_desc][0]


# Mother's occupation (Categorical)
mother_occupation_options = {
    0: "Student", 1: "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
    2: "Specialists in Intellectual and Scientific Activities", 3: "Intermediate Level Technicians and Professions",
    4: "Administrative staff", 5: "Personal Services, Security and Safety Workers and Sellers",
    6: "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry", 7: "Skilled Workers in Industry, Construction and Craftsmen",
    8: "Installation and Machine Operators and Assembly Workers", 9: "Unskilled Workers", 10: "Armed Forces Professions",
    90: "Other Situation", 99: "(blank)", 122: "Health professionals", 123: "teachers",
    125: "Specialists in information and communication technologies (ICT)",
    131: "Intermediate level science and engineering technicians and professions",
    132: "Technicians and professionals, of intermediate level of health",
    134: "Intermediate level technicians from legal, social, sports, cultural and similar services",
    141: "Office workers, secretaries in general and data processing operators",
    143: "Data, accounting, statistical, financial services and registry-related operators",
    144: "Other administrative support staff", 151: "personal service workers", 152: "sellers",
    153: "Personal care workers and the like",
    171: "Skilled construction workers and the like, except electricians",
    173: "Skilled workers in printing, precision instrument manufacturing, jewelers, artisans and the like",
    175: "Workers in food processing, woodworking, clothing and other industries and crafts",
    191: "cleaning workers", 192: "Unskilled workers in agriculture, animal production, fisheries and forestry",
    193: "Unskilled workers in extractive industry, construction, manufacturing and transport",
    194: "Meal preparation assistants"
}
selected_mother_occ_desc = st.selectbox("Mother's Occupation", list(mother_occupation_options.values()))
mother_occupation = [key for key, value in mother_occupation_options.items() if value == selected_mother_occ_desc][0]

# Father's occupation (Categorical)
father_occupation_options = {
    0: "Student", 1: "Representatives of the Legislative Power and Executive Bodies, Directors, Directors and Executive Managers",
    2: "Specialists in Intellectual and Scientific Activities", 3: "Intermediate Level Technicians and Professions",
    4: "Administrative staff", 5: "Personal Services, Security and Safety Workers and Sellers",
    6: "Farmers and Skilled Workers in Agriculture, Fisheries and Forestry", 7: "Skilled Workers in Industry, Construction and Craftsmen",
    8: "Installation and Machine Operators and Assembly Workers", 9: "Unskilled Workers", 10: "Armed Forces Professions",
    90: "Other Situation", 99: "(blank)", 101: "Armed Forces Officers", 102: "Armed Forces Sergeants",
    103: "Other Armed Forces personnel", 112: "Directors of administrative and commercial services",
    114: "Hotel, catering, trade and other services directors",
    121: "Specialists in the physical sciences, mathematics, engineering and related techniques",
    122: "Health professionals", 123: "teachers",
    124: "Specialists in finance, accounting, administrative organization, public and commercial relations",
    131: "Intermediate level science and engineering technicians and professions",
    132: "Technicians and professionals, of intermediate level of health",
    134: "Intermediate level technicians from legal, social, sports, cultural and similar services",
    135: "Information and communication technology technicians",
    141: "Office workers, secretaries in general and data processing operators",
    143: "Data, accounting, statistical, financial services and registry-related operators",
    144: "Other administrative support staff", 151: "personal service workers", 152: "sellers",
    153: "Personal care workers and the like", 154: "Protection and security services personnel",
    161: "Market-oriented farmers and skilled agricultural and animal production workers",
    163: "Farmers, livestock keepers, fishermen, hunters and gatherers, subsistence",
    171: "Skilled construction workers and the like, except electricians",
    172: "Skilled workers in metallurgy, metalworking and similar",
    174: "Skilled workers in electricity and electronics",
    175: "Workers in food processing, woodworking, clothing and other industries and crafts",
    181: "Fixed plant and machine operators", 182: "assembly workers",
    183: "Vehicle drivers and mobile equipment operators",
    192: "Unskilled workers in agriculture, animal production, fisheries and forestry",
    193: "Unskilled workers in extractive industry, construction, manufacturing and transport",
    194: "Meal preparation assistants",
    195: "Street vendors (except food) and street service providers"
}
selected_father_occ_desc = st.selectbox("Father's Occupation", list(father_occupation_options.values()))
father_occupation = [key for key, value in father_occupation_options.items() if value == selected_father_occ_desc][0]


# Displaced (Categorical)
displaced = st.radio("Displaced Person", options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")

# Educational special needs (Categorical)
educational_special_needs = st.radio("Educational Special Needs", options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")

# Debtor (Categorical)
debtor = st.radio("Debtor", options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")

# Tuition fees up to date (Categorical)
tuition_fees_up_to_date = st.radio("Tuition Fees Up to Date", options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")

# Scholarship holder (Categorical)
scholarship_holder = st.radio("Scholarship Holder", options=[1, 0], format_func=lambda x: "Yes" if x == 1 else "No")


# --- Create a button to trigger prediction ---
if st.button("Predict Dropout Probability"):
    # Collect all the input data into a dictionary or pandas DataFrame
    input_data = {
        'Marital_status': marital_status,
        'Application_mode': application_mode,
        'Application_order': application_order,
        'Course': course,
        'Daytime_evening_attendance': daytime_evening_attendance,
        'Previous_qualification': previous_qualification,
        'Previous_qualification_grade': previous_qualification_grade,
        'Nacionality': nationality,
        'Mothers_qualification': mother_qualification,
        'Fathers_qualification': father_qualification,
        'Mothers_occupation': mother_occupation,
        'Fathers_occupation': father_occupation,
        'Admission_grade': admission_grade,
        'Displaced': displaced,
        'Educational_special_needs': educational_special_needs,
        'Debtor': debtor,
        'Tuition_fees_up_to_date': tuition_fees_up_to_date,
        'Gender': gender,
        'Scholarship_holder': scholarship_holder,
        'Age_at_enrollment': age_at_enrollment,
        'International': international,
        'Curricular_units_1st_sem_credited': curricular_units_1st_sem_credited,
        'Curricular_units_1st_sem_enrolled': curricular_units_1st_sem_enrolled,
        'Curricular_units_1st_sem_evaluations': curricular_units_1st_sem_evaluations,
        'Curricular_units_1st_sem_approved': curricular_units_1st_sem_approved,
        'Curricular_units_1st_sem_grade': curricular_units_1st_sem_grade,
        'Curricular_units_1st_sem_without_evaluations': curricular_units_1st_sem_without_evaluations,
        'Curricular_units_2nd_sem_credited': curricular_units_2nd_sem_credited,
        'Curricular_units_2nd_sem_enrolled': curricular_units_2nd_sem_enrolled,
        'Curricular_units_2nd_sem_evaluations': curricular_units_2nd_sem_evaluations,
        'Curricular_units_2nd_sem_approved': curricular_units_2nd_sem_approved,
        'Curricular_units_2nd_sem_grade': curricular_units_2nd_sem_grade,
        'Curricular_units_2nd_sem_without_evaluations': curricular_units_2nd_sem_without_evaluations,
        'Unemployment_rate': unemployment_rate,
        'Inflation_rate': inflation_rate,
        'GDP': gdp
    }

    # Convert to a pandas DataFrame
    input_df = pd.DataFrame([input_data])

# --- Start of model prediction section ---
    try:
        # Load your trained model (assuming it's a scikit-learn model)
        import joblib
        model = joblib.load('rf_dropout_prediction.pkl')  # Replace with your model file path

        # Make predictions
        prediction_probability = model.predict_proba(input_df)[:, 0]  # Get probability of dropout (class 0)
        predicted_class = "Likely Dropout" if prediction_probability[0] > 0.5 else "Unlikely Dropout"
        st.success(
            f"Predicted Dropout Probability: {prediction_probability[0]:.2f}  \nPrediction: {predicted_class}"
        )
        
    except Exception as e:
        st.error(f"An error occurred during prediction: {e}")
    # --- End of model prediction section ---

    # For demonstration purposes, display the collected data
    st.subheader("Input Data:")
    st.write(input_df)

