# Credit Card Approval using Machine Learning

# Installing necessary modules
```bash
pip3 install scikit-learn
pip3 install imblearn
pip3 install flask
pip3 install pandas
```


# Training the model
```bash
cd models/
python3 approval_model.py 
mv mlp_model.pkl ../mlp_model.pkl
```
 Training the model and Moving the model's pickle file to appropriate position

# Running the web application
```bash
python3 web_app.py
```