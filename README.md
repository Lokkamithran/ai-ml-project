# Credit Card Approval using Machine Learning

# Installing necessary modules
pip3 install scikit-learn
pip3 install imblearn
pip3 install flask
pip3 install pandas

# Training the model
> python3 approval_model.py (Run from inside the 'models' folder)

# Moving the model's pickle file to appropriate position
> mv mlp_model.pkl ../mlp_model.pkl (Run from inside the 'models' folder)

# Running the web application
> python3 web_app.py