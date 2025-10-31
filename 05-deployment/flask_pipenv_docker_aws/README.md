# Serving the Churn Model with Flask

This project demonstrates how to train and serve a customer churn prediction model using **Flask**. The model predicts the likelihood of a customer churning and can be integrated into other services (e.g., marketing automation).

---

## Project Structure

```
.
├── train.py          # Trains and saves the churn model
├── predict.py        # Flask app that serves predictions
├── predict-test.py   # Script to test the Flask API
├── model_C=1.0.bin   # Serialized model and DictVectorizer
```

---

## 1. Installation

Create and activate a virtual environment (optional but recommended):

```bash
python -m venv venv
source venv/bin/activate       # macOS/Linux
venv\Scripts\activate          # Windows
```

Install the required dependencies:

```bash
pip install flask scikit-learn requests gunicorn
```

---

## 2. Training the Model

Run the training script to train and save the churn model using `pickle`.
This will create a serialized model file (e.g., `model_C=1.0.bin`).

```bash
python train.py
```

---

## 3. Serving Predictions with Flask

The Flask app in `predict.py` loads the saved model and provides a **POST** endpoint at `/predict`.
It accepts customer data in JSON format and returns the churn probability and decision.

Example response:

```json
{
  "churn_probability": 0.63,
  "churn": true
}
```

Run the Flask app locally:

```bash
python predict.py
```

Note: The endpoint only supports **POST** requests.
Sending a **GET** request (e.g., by opening it in a browser) will result in a 405 error.

---

## 4. Testing the API

Use `predict-test.py` to send a test request to the Flask API and view the prediction result.

```bash
python predict-test.py
```

Example output:

```
{'churn': True, 'churn_probability': 0.6363584152721401}
sending promo email to xyz-123
```

---

## 5. Running in Production with Gunicorn

Flask’s built-in server is intended for development use only.
For production, use **Gunicorn** (available for Linux, macOS, and WSL).

Install Gunicorn:

```bash
pip install gunicorn
```

Run the web service:

```bash
gunicorn --bind 0.0.0.0:9696 predict:app
```

Then test the API again with:

```bash
python predict-test.py
```

---

## Summary

* **train.py** – trains and saves the model
* **predict.py** – serves the model via Flask
* **predict-test.py** – tests the Flask API
* **Gunicorn** – for production deployment

---
