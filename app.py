from flask import Flask, render_template, request
from forms import CPIPredictionForm  
import joblib
import pandas as pd

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your_secret_key_here'

# Load the trained model and encoders
model = joblib.load('gradient_boosting_model.joblib')  
encoders = joblib.load('preprocessor.joblib')  

@app.route('/', methods=['GET', 'POST'])
def index():
    form = CPIPredictionForm()  
    cpi_prediction = None
    print("index")
    if form.validate_on_submit():
        print("Form is valid")
        # Extract data from the form
        data = {
            'Gender': form.gender.data,
            'Category': form.category.data,
            'Parental Education': form.parental_education.data,
            'Hometown Area': form.hometown_area.data,
            'Family annual income': form.family_annual_income.data,
            'Guidance from family': form.guidance_from_family.data,
            'Family member in same field': form.family_member_in_same_field.data,
            'Percentage in 10th': form.percentage_10th.data,
            'Percentage in 12th': form.percentage_12th.data,
            'Medium studied in?': form.medium_studied_in.data,
            'CPI in graduation': form.cpi_graduation.data,
            'Course': form.course.data,
            'College type': form.college_type.data,
            'Attendance in class': form.attendance_in_class.data,
            'Living arrangement': form.living_arrangement.data,
            'Participation in class': form.participation_in_class.data,
            'Homework submission': form.homework_submission.data,
            'Preparation level': form.preparation_level_for_exam.data,
            'Internet Usage': form.internet_usage.data,
            'Weekend plans': form.weekend_plans.data,
            'Study technique': form.study_technique.data,
            'Study environment': form.study_environment.data,
            'Learning style': form.learning_style.data,
            'Sleeping time': form.sleeping_time.data,
            'Extracurricular Activities': form.extracurricular_activities.data,
            'Your class buddy friend': form.class_buddy_friend.data,
            'Relationship Status in last sem': form.relationship_status_in_last_sem.data
        }

        data_df = pd.DataFrame([data])
        print("Form data:", data_df)
    
        preprocessed_data = encoders.transform(data_df)
        transformed_columns = encoders.get_feature_names_out()
        preprocessed_data_df = pd.DataFrame(preprocessed_data, columns=transformed_columns)

        prediction = model.predict(preprocessed_data_df)
        cpi_prediction = float(prediction[0])
        print("CPI prediction:", cpi_prediction)
    else:
        print("Form validation failed")
        print("Errors:", form.errors)
        
    return render_template('index.html', form=form, result=cpi_prediction)

if __name__ == '__main__':
    app.run(debug=True)
