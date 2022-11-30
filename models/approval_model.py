import pickle
import pandas as pd
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler
from imblearn.over_sampling import SMOTE
from sklearn.neural_network import MLPClassifier

app_record = pd.read_csv("application_record.csv")
credit_record = pd.read_csv("credit_record.csv")

app_record = app_record.drop_duplicates('ID', keep='last')

app_record.drop('OCCUPATION_TYPE', axis=1, inplace=True) # Since this column has null entries
app_record.drop(['DAYS_BIRTH', 'FLAG_MOBIL', 'FLAG_WORK_PHONE', 'FLAG_PHONE', 'FLAG_EMAIL'], axis=1, inplace=True)
app_record['DAYS_EMPLOYED'] = app_record['DAYS_EMPLOYED'].apply(lambda x:0 if x >= 0 else x)

# Label Encoding the strings in the dataset
le = LabelEncoder()
for x in app_record:
    if app_record[x].dtypes == 'object':
        app_record[x] = le.fit_transform(app_record[x])

# There are outliers in 3 columns.
# CNT_CHILDREN, AMT_INCOME_TOTAL and CNT_FAM_MEMBERS
# Removing the outliers

# For CNT_CHILDREN column
q_hi = app_record['CNT_CHILDREN'].quantile(0.999)
q_low = app_record['CNT_CHILDREN'].quantile(0.001)
app_record = app_record[(app_record['CNT_CHILDREN']>q_low) & (app_record['CNT_CHILDREN']<q_hi)]

# For AMT_INCOME_TOTAL column
q_hi = app_record['AMT_INCOME_TOTAL'].quantile(0.999)
q_low = app_record['AMT_INCOME_TOTAL'].quantile(0.001)
app_record = app_record[(app_record['AMT_INCOME_TOTAL']>q_low) & (app_record['AMT_INCOME_TOTAL']<q_hi)]

# For CNT_FAM_MEMBERS column
q_hi = app_record['CNT_FAM_MEMBERS'].quantile(0.999)
q_low = app_record['CNT_FAM_MEMBERS'].quantile(0.001)
app_record = app_record[(app_record['CNT_FAM_MEMBERS']>q_low) & (app_record['CNT_FAM_MEMBERS']<q_hi)]

credit_record['Months from today'] = credit_record['MONTHS_BALANCE']*-1
credit_record = credit_record.sort_values(['ID','Months from today'], ascending=True)

# Replacing STATUS with 0 for non-defaulters and 1 for defaulters
credit_record['STATUS'].replace({'C': 0, 'X' : 0}, inplace=True)
credit_record['STATUS'] = credit_record['STATUS'].astype('int')
credit_record['STATUS'] = credit_record['STATUS'].apply(lambda x:1 if x >= 2 else 0)

# Data is oversampled. Will be resolved after joining the 2 tables
# print(credit_record['STATUS'].value_counts(normalize=True)) 

# Group by ID so it can be joined with app table
credit_record_gb = credit_record.groupby('ID').agg(max).reset_index()

# Joining the 2 tables
df = app_record.join(credit_record_gb.set_index('ID'), on='ID', how='inner')
df.drop(['Months from today', 'MONTHS_BALANCE'], axis=1, inplace=True)


X = df.iloc[:,1:-1] # X value contains all the variables except labels
y = df.iloc[:,-1] # these are the labels

<<<<<<< HEAD


# mms = MinMaxScaler()
# xmax = X.max().to_csv("xmax.csv",index=False)
# print(xmax)
# xmin = X.min().to_csv("xmin.csv",index=False)
# print(xmin)


# print(X)
# print(y)

x_std = (X - X.min(axis = 0))/(X.max(axis=0) - X.min(axis=0))
# print(x_std)
# print(X_train.columns)
# print(mms.fit_transform(X_train)[0])
# X_scaled = pd.DataFrame(mms.fit_transform(X), columns=X.columns)
# x_std.to_csv('x_std.csv')
# X_test_scaled = pd.DataFrame(mms.transform(X_test), columns=X_test.columns)

# Creating the test-train split
X_train, X_test, y_train, y_test = train_test_split(x_std,y, test_size=0.3)
# print(y_test.head())

# Scaling the data using MinMaxScaler
# mms = MinMaxScaler()
# print(X_train.columns)
# print(mms.fit_transform(X_train)[0])
# X_scaled = pd.DataFrame(mms.fit_transform(X_train), columns=X_train.columns)
# X_test_scaled = pd.DataFrame(mms.transform(X_test), columns=X_test.columns)

# Solving the over-sampling issue
oversample = SMOTE()
X_balanced, y_balanced = oversample.fit_resample(X_train, y_train)
X_test_balanced, y_test_balanced = oversample.fit_resample(X_test, y_test)
# y_test_balanced.to_csv("ytest.csv",index=False)
=======
# Creating the test-train split
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size=0.3)

# Scaling the data using MinMaxScaler
mms = MinMaxScaler()
X_scaled = pd.DataFrame(mms.fit_transform(X_train), columns=X_train.columns)
X_test_scaled = pd.DataFrame(mms.transform(X_test), columns=X_test.columns)

# Solving the over-sampling issue
oversample = SMOTE()
X_balanced, y_balanced = oversample.fit_resample(X_scaled, y_train)
X_test_balanced, y_test_balanced = oversample.fit_resample(X_test_scaled, y_test)

>>>>>>> b8cf50aa0134fb3c456c654f1173f86d74bd8a2b
# Before: 
# print(y_train.value_counts())
# print(y_test.value_counts())
# After: 
# print(y_balanced.value_counts())
# print(y_test_balanced.value_counts())

<<<<<<< HEAD
mlp = MLPClassifier(solver='adam', alpha=1e-5,hidden_layer_sizes=(9, 2), random_state=1, max_iter=10000, shuffle = True)

mlp.fit(X_balanced, y_balanced)
# X_balanced.to_csv("xbal.csv",index=False)
# y_balanced.to_csv("ybal.csv",index=False)
=======
mlp = MLPClassifier(solver='lbfgs', alpha=1e-5,hidden_layer_sizes=(5, 2), random_state=1, max_iter=10000)

mlp.fit(X_balanced, y_balanced)

>>>>>>> b8cf50aa0134fb3c456c654f1173f86d74bd8a2b
# Saving the model into a pickle file
filename = 'mlp_model.pkl'
pickle.dump(mlp, open(filename, 'wb'))
# Saving the label encoder into a pickle file
<<<<<<< HEAD
# le_file = 'le_file.pkl'
# pickle.dump(le, open(le_file, 'wb'))
# Saving the MinMaxScaler into a pickle file
# minmax_file = 'minmax_file.pkl'
# pickle.dump(mms, open(minmax_file, 'wb'))
=======
le_file = 'le_file.pkl'
pickle.dump(le, open(le_file, 'wb'))
# Saving the MinMaxScaler into a pickle file
minmax_file = 'minmax_file.pkl'
pickle.dump(mms, open(minmax_file, 'wb'))
>>>>>>> b8cf50aa0134fb3c456c654f1173f86d74bd8a2b

train_score = mlp.score(X_balanced, y_balanced)
test_score = mlp.score(X_test_balanced, y_test_balanced)

print(train_score)
<<<<<<< HEAD
print(test_score)


# input_list = ['M', 'N', 'N', 999, 10, 'Pensioner', 'Incomplete higher', 'Civil marriage', 'With parents', -1, 11]
# input_list = ['M', 'Y', 'Y', 2, 100000000000, 'Working', 'Academic degree', 'Married', 'House / apartment', -1000, 4]
# input_list = ['F', 'N', 'N', 2, 100000000000, 'Working', 'Academic degree', 'Married', 'House / apartment', -1000, 4]

# input_df = pd.DataFrame([input_list], columns=['CODE_GENDER','FLAG_OWN_CAR','FLAG_OWN_REALTY','CNT_CHILDREN','AMT_INCOME_TOTAL','NAME_INCOME_TYPE','NAME_EDUCATION_TYPE','NAME_FAMILY_STATUS','NAME_HOUSING_TYPE','DAYS_EMPLOYED','CNT_FAM_MEMBERS'])
# print(input_df)
# print()
# # print(input_df.dtypes)

# for x in input_df:
#     if input_df[x].dtypes == 'object':
#         print("le done", input_df[x])
#         input_df[x] = le.fit_transform(input_df[x].values)
        

# print(input_df)
# print()
# X = input_df
# X_scaled = pd.DataFrame(mms.fit_transform(X.values))
# print(X_scaled)
# print()
# prediction = mlp.predict(X_scaled.values)
# print(prediction)
# print()
# if prediction[0] == 0:
#     print('Your application will be approved')
# else:
#     print('Your application won\'t be approved')

    # 1 1 1 1 100000000 1 5 1 1000  3
=======
print(test_score)
>>>>>>> b8cf50aa0134fb3c456c654f1173f86d74bd8a2b
