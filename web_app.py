from flask import Flask, render_template, request
import pickle
import pandas as pd

# loaded_le = pickle.load(open("le_file.pkl", "rb"))
# loaded_mms = pickle.load(open("minmax_file.pkl", "rb"))
loaded_model = pickle.load(open("mlp_model.pkl", "rb"))


app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():

    CODE_GENDER_INPUT = float(request.form['gender'])

    FLAG_OWN_CAR_INPUT = float(request.form['is_car'])

    FLAG_OWN_REALTY_INPUT = float(request.form['is_property'])

    CNT_CHILDREN_INPUT = int(request.form['children'])

    AMT_INCOME_TOTAL_INPUT = int(request.form['income'])

    NAME_INCOME_TYPE_INPUT = float(request.form['income_cat'])

    NAME_EDUCATION_TYPE_INPUT = float(request.form['edu_level'])

    NAME_FAMILY_STATUS_INPUT = float(request.form['marital_status'])

    NAME_HOUSING_TYPE_INPUT = float(request.form['way_of_living'])

    DAYS_EMPLOYED_INPUT = int(request.form['days_employed'])

    CNT_FAM_MEMBERS_INPUT = int(request.form['fam_size'])


    Xmax_list = pd.read_csv("files/xmax.csv").T
    Xmin_list = pd.read_csv("files/xmin.csv").T
    
    max_list = Xmax_list.values.tolist()
    min_list = Xmin_list.values.tolist()

    if CNT_CHILDREN_INPUT < min_list[0][3]:
        CNT_CHILDREN_INPUT = min_list[0][3]
    elif CNT_CHILDREN_INPUT > max_list[0][3]:
        CNT_CHILDREN_INPUT = max_list[0][3]

    if AMT_INCOME_TOTAL_INPUT < min_list[0][4]:
        AMT_INCOME_TOTAL_INPUT = min_list[0][4]
    elif AMT_INCOME_TOTAL_INPUT > max_list[0][4]:
        AMT_INCOME_TOTAL_INPUT = max_list[0][4]

    if DAYS_EMPLOYED_INPUT > -1*min_list[0][9]:
        DAYS_EMPLOYED_INPUT = -1*min_list[0][9]
    elif DAYS_EMPLOYED_INPUT < max_list[0][9]:
        DAYS_EMPLOYED_INPUT = max_list[0][9]

    if CNT_FAM_MEMBERS_INPUT < min_list[0][10]:
        CNT_FAM_MEMBERS_INPUT = min_list[0][10]
    elif CNT_FAM_MEMBERS_INPUT > max_list[0][10]:
        CNT_FAM_MEMBERS_INPUT = max_list[0][10]

    input_list = [CODE_GENDER_INPUT, FLAG_OWN_CAR_INPUT, FLAG_OWN_REALTY_INPUT, CNT_CHILDREN_INPUT, AMT_INCOME_TOTAL_INPUT, NAME_INCOME_TYPE_INPUT, NAME_EDUCATION_TYPE_INPUT, NAME_FAMILY_STATUS_INPUT, NAME_HOUSING_TYPE_INPUT, DAYS_EMPLOYED_INPUT, CNT_FAM_MEMBERS_INPUT]
    input_df = pd.DataFrame([input_list], columns=['CODE_GENDER','FLAG_OWN_CAR','FLAG_OWN_REALTY','CNT_CHILDREN','AMT_INCOME_TOTAL','NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','NAME_HOUSING_TYPE','DAYS_EMPLOYED','CNT_FAM_MEMBERS'])

    # print(input_df.dtypes)

    # for x in input_df:
    #     if input_df[x].dtypes == 'object':
    #         input_df[x] = loaded_le.fit_transform(input_df[x])

    # print(max_list)
    # print(min_list)

    # print()
    # print()
    # print("X max at 4 ", max_list[0][4], " X min at 4 ", min_list[0][4])
    # print()
    # print()

    #Scaling AMT_INCOME_TOTAL and DAYS_EMPLOYED
    X = input_df
    X["CNT_CHILDREN"] = (X["CNT_CHILDREN"] - min_list[0][3])/(max_list[0][3] - min_list[0][3])
    X["AMT_INCOME_TOTAL"] = (X["AMT_INCOME_TOTAL"] - min_list[0][4])/(max_list[0][4] - min_list[0][4])
    X["DAYS_EMPLOYED"] = (X["DAYS_EMPLOYED"])/(min_list[0][9]*-1)
    X["CNT_FAM_MEMBERS"] = (X["CNT_FAM_MEMBERS"] - min_list[0][10])/(max_list[0][10] - min_list[0][10])

    # print()
    # print()
    # print()
    # X_scaled = pd.DataFrame(loaded_mms.fit_transform(X))
    # print(input_list)
    # print()
    # print(X)
    # print()
    # print(X.info())

    # print('Testing days employed')
    # test_var = 1393
    # test_var = (test_var)/(max_list[0][9] - min_list[0][9])
    # print(test_var)

    # X = [1.0,1.0,1.0,0.5,0.250000,0.75,0.25,1.0,0.2,0.09630346161818558,1.0] # False
    #Male, Y, Y, 2, 258750, Student, Higher Education, Widow, House/Apartment, 1393 days, 4

    # X = [1.0,1.0,1.0,1.0,0.25,0.75,0.25,1.0,0.2,0.096248,1.0]
    # columns=['CODE_GENDER','FLAG_OWN_CAR','FLAG_OWN_REALTY','CNT_CHILDREN','AMT_INCOME_TOTAL','NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','NAME_HOUSING_TYPE','DAYS_EMPLOYED','CNT_FAM_MEMBERS']
    # X = pd.DataFrame([X])
    # X.columns = columns


    pd.options.display.max_columns = None

    # prediction = loaded_model.predict(X)
    logProbs = loaded_model.predict_proba(X)
    print(logProbs)
    # print()
    # print()
    # print()

    print(X)


    if logProbs[0][0] >= 0.70:
        printtext = "Your application will be approved"
    else:
        printtext = "Your application won\'t be approved"

    return render_template('index.html', prediction_text=printtext)

if __name__ == "__main__":
    app.run()

#  export FLASK_DEBUG=1
