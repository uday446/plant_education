FROM python:3.7

WORKDIR /plant_education
COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

ENTRYPOINT ["python", "app.py"]