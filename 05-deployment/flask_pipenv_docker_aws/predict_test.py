"we use the requests library to send our request to the web service. "
"As previously mentioned, we use the POST method. The POST method of requests takes "
"two arguments. ‘url’ points to the web service, and ‘json’ represents "
"our customer information, which needs to be in JSON format. "
"Depending on the result, the script will determine whether to send a promotion email or not."

import requests
 
url = 'http://localhost:9696/predict'
 
customer_id = 'xyz-123'
customer = {
    "gender": "female",
    "seniorcitizen": 0,
    "partner": "yes",
    "dependents": "no",
    "phoneservice": "no",
    "multiplelines": "no_phone_service",
    "internetservice": "dsl",
    "onlinesecurity": "no",
    "onlinebackup": "yes",
    "deviceprotection": "no",
    "techsupport": "no",
    "streamingtv": "no",
    "streamingmovies": "no",
    "contract": "month-to-month",
    "paperlessbilling": "yes",
    "paymentmethod": "electronic_check",
    "tenure": 1,
    "monthlycharges": 29.85,
    "totalcharges": 29.85
}
 
response = requests.post(url, json=customer).json()
print(response)
 
if response['churn'] == True:
    print('sending promo email to %s' % customer_id)
else:
    print('not sending promo email to %s' % customer_id)