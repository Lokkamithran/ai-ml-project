import pickle, pandas as pd

loaded_le = pickle.load(open("le_file.pkl", "rb"))
loaded_mms = pickle.load(open("minmax_file.pkl", "rb"))
loaded_model = pickle.load(open("mlp_model.pkl", "rb"))

gender = ['M', 'F']
yes_no = ['Y', 'N']
income_cat = ['Working', 'Commercial associate', 'Pensioner', 'State servant', 'Student']
edu_level = ['Secondary / secondary special', 'Higher education', 'Incomplete higher', 'Lower secondary', 'Academic degree']
married_status = ['Married', 'Single / not married', 'Civil marriage', 'Separated', 'Widow']
way_of_living = ['House / apartment', 'With parents', 'Municipal apartment', 'Rented apartment', 'Office apartment']

<<<<<<< HEAD

# def COMMENT():
#     print()
#     print('Gender?\n1. Male\n2. Female')
#     CODE_GENDER_INPUT = gender[int(input())-1]

#     print()
#     print('Owns a car?\n1. Yes\n2. No')
#     FLAG_OWN_CAR_INPUT = yes_no[int(input())-1]

#     print()
#     print('Owns property?\n1. Yes\n2. No')
#     FLAG_OWN_REALTY_INPUT = yes_no[int(input())-1]

#     print()
    # print('Number of children?')
    # CNT_CHILDREN_INPUT = int(input())

    # print()
    # print('Annual Income?')
    # AMT_INCOME_TOTAL_INPUT = int(input())

    # print()
    # print('Income Category?\n1. ',income_cat[0],'\n2. ', income_cat[1],'\n3. ', income_cat[2],'\n4. ', income_cat[3],'\n5. ', income_cat[4])
    # NAME_INCOME_TYPE_INPUT = income_cat[int(input())-1]

    # print()
    # print('Education level?\n1. ',edu_level[0],'\n2. ',edu_level[1],'\n3. ',edu_level[2],'\n4. ',edu_level[3],'\n5. ',edu_level[4])
    # NAME_EDUCATION_TYPE_INPUT = edu_level[int(input())-1]

    # print()
    # print('Marital status?\n1. ',married_status[0],'\n2. ',married_status[1],'\n3. ',married_status[2],'\n4. ',married_status[3],'\n5. ',married_status[4])
    # NAME_FAMILY_STATUS_INPUT = married_status[int(input())-1]

#     print()
#     print('Way of living?\n1. ',way_of_living[0],'\n2. ',way_of_living[1],'\n3. ',way_of_living[2],'\n4. ',way_of_living[3],'\n5. ',way_of_living[4])
#     NAME_HOUSING_TYPE_INPUT = way_of_living[int(input())-1]

#     print()
#     print('Days in employment?\nEnter 0, if unemployed')
#     DAYS_EMPLOYED_INPUT = int(input())

#     print()
#     print('Family size?')
#     CNT_FAM_MEMBERS_INPUT = int(input())

#     input_list = [CODE_GENDER_INPUT, FLAG_OWN_CAR_INPUT, FLAG_OWN_REALTY_INPUT, CNT_CHILDREN_INPUT, AMT_INCOME_TOTAL_INPUT, NAME_INCOME_TYPE_INPUT, NAME_EDUCATION_TYPE_INPUT, NAME_FAMILY_STATUS_INPUT, NAME_HOUSING_TYPE_INPUT, DAYS_EMPLOYED_INPUT*-1, CNT_FAM_MEMBERS_INPUT]



input_list = ['M', 'N', 'N', 999, 10, 'Pensioner', 'Incomplete higher', 'Civil marriage', 'With parents', -1, 11]
input_list = ['M', 'Y', 'Y', 2, 100000000000, 'Working', 'Academic degree', 'Married', 'House / apartment', -1000, 4]
# input_list = ['F', 'N', 'N', 2, 100000000000, 'Working', 'Academic degree', 'Married', 'House / apartment', -1000, 4]

input_df = pd.DataFrame([input_list], columns=['CODE_GENDER','FLAG_OWN_CAR','FLAG_OWN_REALTY','CNT_CHILDREN','AMT_INCOME_TOTAL','NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','NAME_HOUSING_TYPE','DAYS_EMPLOYED','CNT_FAM_MEMBERS'])
print(input_df)
print()
=======
print()
print('Gender?\n1. Male\n2. Female')
CODE_GENDER_INPUT = gender[int(input())-1]

print()
print('Owns a car?\n1. Yes\n2. No')
FLAG_OWN_CAR_INPUT = yes_no[int(input())-1]

print()
print('Owns property?\n1. Yes\n2. No')
FLAG_OWN_REALTY_INPUT = yes_no[int(input())-1]

print()
print('Number of children?')
CNT_CHILDREN_INPUT = int(input())

print()
print('Annual Income?')
AMT_INCOME_TOTAL_INPUT = int(input())

print()
print('Income Category?\n1. ',income_cat[0],'\n2. ', income_cat[1],'\n3. ', income_cat[2],'\n4. ', income_cat[3],'\n5. ', income_cat[4])
NAME_INCOME_TYPE_INPUT = income_cat[int(input())-1]

print()
print('Education level?\n1. ',edu_level[0],'\n2. ',edu_level[1],'\n3. ',edu_level[2],'\n4. ',edu_level[3],'\n5. ',edu_level[4])
NAME_EDUCATION_TYPE_INPUT = edu_level[int(input())-1]

print()
print('Marital status?\n1. ',married_status[0],'\n2. ',married_status[1],'\n3. ',married_status[2],'\n4. ',married_status[3],'\n5. ',married_status[4])
NAME_FAMILY_STATUS_INPUT = married_status[int(input())-1]

print()
print('Way of living?\n1. ',way_of_living[0],'\n2. ',way_of_living[1],'\n3. ',way_of_living[2],'\n4. ',way_of_living[3],'\n5. ',way_of_living[4])
NAME_HOUSING_TYPE_INPUT = way_of_living[int(input())-1]

print()
print('Days in employment?\nEnter 0, if unemployed')
DAYS_EMPLOYED_INPUT = int(input())

print()
print('Family size?')
CNT_FAM_MEMBERS_INPUT = int(input())

input_list = [CODE_GENDER_INPUT, FLAG_OWN_CAR_INPUT, FLAG_OWN_REALTY_INPUT, CNT_CHILDREN_INPUT, AMT_INCOME_TOTAL_INPUT, NAME_INCOME_TYPE_INPUT, NAME_EDUCATION_TYPE_INPUT, NAME_FAMILY_STATUS_INPUT, NAME_HOUSING_TYPE_INPUT, DAYS_EMPLOYED_INPUT*-1, CNT_FAM_MEMBERS_INPUT]
input_df = pd.DataFrame([input_list], columns=['CODE_GENDER','FLAG_OWN_CAR','FLAG_OWN_REALTY','CNT_CHILDREN','AMT_INCOME_TOTAL','NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','NAME_HOUSING_TYPE','DAYS_EMPLOYED','CNT_FAM_MEMBERS'])

>>>>>>> b8cf50aa0134fb3c456c654f1173f86d74bd8a2b
# print(input_df.dtypes)

for x in input_df:
    if input_df[x].dtypes == 'object':
<<<<<<< HEAD
        input_df[x] = loaded_le.fit_transform(input_df[x].values)
print(input_df)
print()
X = input_df
X_scaled = pd.DataFrame(loaded_mms.fit_transform(X.values))
print(X_scaled)
print()
prediction = loaded_model.predict(X_scaled.values)
print(prediction)
print()
if prediction[0] == 0:
    print('Your application will be approved')
else:
    print('Your application won\'t be approved')

    # 1 1 1 1 100000000 1 5 1 1000  3
=======
        input_df[x] = loaded_le.fit_transform(input_df[x])

X = input_df
X_scaled = pd.DataFrame(loaded_mms.fit_transform(X))
print(X.info())
prediction = loaded_model.predict(X_scaled)
if prediction[0] == '0':
    print('Your application won\'t be approved')
else:
    print('Your application will be approved')
>>>>>>> b8cf50aa0134fb3c456c654f1173f86d74bd8a2b
