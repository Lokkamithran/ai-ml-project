from flask import Flask, render_template, request
import pickle
import pandas as pd

loaded_le = pickle.load(open("le_file.pkl", "rb"))
loaded_mms = pickle.load(open("minmax_file.pkl", "rb"))
loaded_model = pickle.load(open("mlp_model.pkl", "rb"))


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():

    CODE_GENDER_INPUT = request.form['gender']

    FLAG_OWN_CAR_INPUT = request.form['is_car']

    FLAG_OWN_REALTY_INPUT = request.form['is_property']

    CNT_CHILDREN_INPUT = int(request.form['children'])

    AMT_INCOME_TOTAL_INPUT = int(request.form['income'])

    NAME_INCOME_TYPE_INPUT = request.form['income_cat']

    NAME_EDUCATION_TYPE_INPUT = request.form['edu_level']

    NAME_FAMILY_STATUS_INPUT = request.form['marital_status']

    NAME_HOUSING_TYPE_INPUT = request.form['way_of_living']

    DAYS_EMPLOYED_INPUT = int(request.form['days_employed'])

    CNT_FAM_MEMBERS_INPUT = int(request.form['fam_size'])


    input_list = [CODE_GENDER_INPUT, FLAG_OWN_CAR_INPUT, FLAG_OWN_REALTY_INPUT, CNT_CHILDREN_INPUT, AMT_INCOME_TOTAL_INPUT, NAME_INCOME_TYPE_INPUT, NAME_EDUCATION_TYPE_INPUT, NAME_FAMILY_STATUS_INPUT, NAME_HOUSING_TYPE_INPUT, DAYS_EMPLOYED_INPUT*-1, CNT_FAM_MEMBERS_INPUT]
    input_df = pd.DataFrame([input_list], columns=['CODE_GENDER','FLAG_OWN_CAR','FLAG_OWN_REALTY','CNT_CHILDREN','AMT_INCOME_TOTAL','NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','NAME_HOUSING_TYPE','DAYS_EMPLOYED','CNT_FAM_MEMBERS'])

    # print(input_df.dtypes)

    for x in input_df:
        if input_df[x].dtypes == 'object':
            input_df[x] = loaded_le.fit_transform(input_df[x])

    X = input_df

    print()
    print()
    print()
    X_scaled = pd.DataFrame(loaded_mms.fit_transform(X))
    print(input_list)
    print()
    print()
    print()
    # print(X.info())
    prediction = loaded_model.predict(X_scaled)

    print(prediction)
    print()
    print()
    print()


    if prediction[0] == 0:
        printtext = "Your application will be approved"
    else:
        printtext = "Your application won\'t be approved"

    return render_template('index.html', prediction_text=printtext)

if __name__ == "__main__":
    app.run()

#  export FLASK_DEBUG=1
