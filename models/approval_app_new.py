import pickle, pandas as pd

# loaded_le = pickle.load(open("le_file.pkl", "rb"))
# loaded_mms = pickle.load(open("minmax_file.pkl", "rb"))
loaded_model = pickle.load(open("mlp_model.pkl", "rb"))

gender = ['M', 'F']
yes_no = ['Y', 'N']
income_cat = ['Working', 'Commercial associate', 'Pensioner', 'State servant', 'Student']
edu_level = ['Secondary / secondary special', 'Higher education', 'Incomplete higher', 'Lower secondary', 'Academic degree']
married_status = ['Married', 'Single / not married', 'Civil marriage', 'Separated', 'Widow']
way_of_living = ['House / apartment', 'With parents', 'Municipal apartment', 'Rented apartment', 'Office apartment']

# input_list = ['M', 'N', 'N', 999, 10, 'Pensioner', 'Incomplete higher', 'Civil marriage', 'With parents', -1, 11]
input_list = [0, 1, 1, 2, 850000, 0, 1, 0.25, 0.2, -10000, 2]
input_list = [0.0, 0.0, 0.0, 2.0, 50000.0, 0.0, 0.0, 0.0, 0.0, 0.0, 4.0]
# input_list = ['F', 'N', 'N', 2, 100000000000, 'Working', 'Academic degree', 'Married', 'House / apartment', -1000, 4]

input_df = pd.DataFrame([input_list])
# print(input_df.dtypes)

# for x in input_df:
#     if input_df[x].dtypes == 'object':
#         input_df[x] = loaded_le.fit_transform(input_df[x].values)
# print(input_df)
# print()
X = input_df
# print(X)
Xmax_list = pd.read_csv("xmax.csv").T
# print(Xmax_list)
Xmin_list = pd.read_csv("xmin.csv").T
# print(Xmin_list)
x_scaled = (X.iloc[0] - Xmin_list.iloc[0])/(Xmax_list.iloc[0] - Xmin_list.iloc[0])
x_scaled = [1.0,1.0,1.0,0.5,0.23684210526315788,1.0,1.0,0.25,0.2,0.9630346161818558,1.0]
x_scaled = [1.0,1.0,1.0,0.5,0.250000,0.75,0.25,1.0,0.2,0.9630346161818558,1.0] # False
x_scaled = [0.0,0.0,0.0,0.0,0.031578947368421054,1.0,0.25,0.25,0.2,0.9736060250120915,0.0]

# x_scaled_df = pd.DataFrame(columns=['CODE_GENDER','FLAG_OWN_CAR','FLAG_OWN_REALTY','CNT_CHILDREN','AMT_INCOME_TOTAL','NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','NAME_HOUSING_TYPE','DAYS_EMPLOYED','CNT_FAM_MEMBERS'])
# print(x_scaled_df)
# X_scaled = pd.DataFrame(loaded_mms.fit_transform(X.values))
# # s
columns=['CODE_GENDER','FLAG_OWN_CAR','FLAG_OWN_REALTY','CNT_CHILDREN','AMT_INCOME_TOTAL','NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','NAME_HOUSING_TYPE','DAYS_EMPLOYED','CNT_FAM_MEMBERS']
x_scaled_df = pd.DataFrame([x_scaled])
x_scaled_df.columns = columns
prediction = loaded_model.predict(x_scaled_df)
logProbs = loaded_model.predict_proba(x_scaled_df)
print(logProbs)
print(x_scaled_df)
print(prediction)
# print()
if prediction[0] == 0:
    print('Your application will be approved')
else:
    print('Your application won\'t be approved')

    # 1 1 1 1 100000000 1 5 1 1000  3