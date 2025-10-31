# Machine Learning Project

This repository contains a step-by-step progression through a machine learning curriculum, from introductory concepts to deploying a model as a service. It is structured in modules (01, 02, 03, …), each focusing on a specific theme:

- **01-intro** — basic setup, introduction  
- **02-regression** — regression modeling  
- **03-classification** — classification modeling  
- **04-eval_metrics_classification** — evaluation & metrics for classification  
- **05-deployment** — turning a model into a web service  

Each module includes notebooks, scripts, and explanations. The **05-deployment** module culminates in deploying a model via FastAPI + Docker.

### How to Use This Repo

1. Clone the repo  
   ```bash
   git clone https://github.com/NuriaAk/machine_learning_project.git
   
2. Navigate into a module, e.g.:  
   ```bash
   cd 02-regression

3. Read the module’s README.md for instructions (data downloading, environment setup, running notebooks).

### Requirements & Environment
* Python 3.8+ (or as specified per module)
* Packages: numpy, pandas, scikit-learn, joblib or pickle, fastapi, uvicorn, docker
* (Optional) Virtual environment or uv / Poetry / pip-tools for isolation

### Contribution & Extensions
* You can adapt any module for your dataset
* Extend the deployment with CI/CD, monitoring, or new endpoints
* Add more metrics (ROC, SHAP/Explainability) or more advanced models