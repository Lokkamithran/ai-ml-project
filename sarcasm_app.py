from flask import Flask, render_template, request
import pickle

app = Flask(__name__)
# model = pickle.load(open('model.pkl', 'rb'))

loaded_cv = pickle.load(open('sarcasm_vectorizer.pkl', 'rb'))
loaded_model = pickle.load(open('sarcasm_model.pkl', 'rb'))


@app.route("/")
def hello():
    return render_template('index.html')

@app.route("/predict", methods=['POST'])
def predict():

    sentence = request.form['sentence']
    data = loaded_cv.transform([sentence]).toarray()
    output = loaded_model.predict(data)

    printtext = ""
    if output[0] == 'Sarcasm':
        printtext = "It\'s a sarcastic headline."
    else:
        printtext = "It\'s not a sarcastic headline."
    return render_template('index.html', prediction_text=printtext)

if __name__ == "__main__":
    app.run()
