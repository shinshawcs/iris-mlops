from fastapi import FastAPI
from pydantic import BaseModel
import joblib
import numpy as np
from app.models import Base
from app.db import engine
from app.db import SessionLocal
from sqlalchemy.orm import Session
from app.models import PredictionLog


Base.metadata.create_all(bind=engine)

app = FastAPI()

model = joblib.load("iris_model.pkl")

# 定义请求数据格式
class IrisInput(BaseModel):
    sepal_length: float
    sepal_width: float
    petal_length: float
    petal_width: float

class_names = ["Setosa", "Versicolor", "Virginica"]

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
        
@app.get("/")
def read_root():
    return {"message": "Welcome to FastAPI Machine Learning API"}

# 预测接口
@app.post("/predict")
def predict(iris: IrisInput):
    # 解析输入数据
    features = np.array([[iris.sepal_length, iris.sepal_width, iris.petal_length, iris.petal_width]])
    prediction = model.predict(features)
    predicted_class = class_names[prediction[0]]
    
    log = PredictionLog(
        sepal_length=iris.sepal_length,
        sepal_width=iris.sepal_width,
        petal_length=iris.petal_length,
        petal_width=iris.petal_width,
        predicted_class=predicted_class
    )
    db = next(get_db())
    db.add(log)
    db.commit()
    db.refresh(log)
    
    return {"prediction": predicted_class}