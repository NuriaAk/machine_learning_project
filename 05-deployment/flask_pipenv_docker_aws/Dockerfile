# Base image
FROM python:3.12-slim

RUN pip install pipenv

# Create a directory and cd there
WORKDIR /app

RUN pipenv lock

# Do not create enviroment, it is already isolated
RUN pipenv install --system --deploy
RUN pip install numpy flask scikit-learn
RUN pip install gunicorn

# Copy the files from your locl machine in the build enviroment
COPY ["predict.py", "model_C=1.0.bin", "./"]

EXPOSE 9696

ENTRYPOINT ["gunicorn", "--bind=0.0.0.0:9696", "predict:app"]