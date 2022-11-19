import pickle

loaded_cv = pickle.load(open('sarcasm_vectorizer.pkl', 'rb'))
loaded_model = pickle.load(open('sarcasm_model.pkl', 'rb'))

user = input("Enter text: ")
data = loaded_cv.transform([user]).toarray()
output = loaded_model.predict(data)

if output[0] == 'Sarcasm':
    print('It\'s a sarcastic headline.')
else:
    print('It\'s not a sarcastic headline.')