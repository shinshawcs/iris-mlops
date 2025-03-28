FROM python:3.9

WORKDIR /app

COPY ./app /app/app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

RUN python app/train_model.py

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]