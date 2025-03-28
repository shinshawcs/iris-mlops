import numpy as np
import pandas as pd
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import joblib
import mlflow
import mlflow.sklearn
from mlflow.models.signature import infer_signature

# 1. Load the Iris dataset
iris = datasets.load_iris()
X = iris.data
y = iris.target

# Verify the data and target
print("Data shape:", X.shape)
print("Target shape:", y.shape)

# 2. Split the dataset
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
mlflow.set_tracking_uri("file:mlruns")

with mlflow.start_run():
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)

    # 创建输入示例和签名
    input_example = X_train[:1]
    prediction = model.predict(input_example)
    signature = infer_signature(X_train, prediction)

    mlflow.log_param("model_type", "RandomForestClassifier")
    train_score = model.score(X_train, y_train)
    test_score = model.score(X_test, y_test)
    mlflow.log_param("model_type", "RandomForestClassifier")
    mlflow.log_metric("train_score", train_score)
    mlflow.log_metric("test_score", test_score)
    # 保存模型（包含签名和输入示例）
    mlflow.sklearn.log_model(
        model, 
        "iris_model",
        signature=signature,
        input_example=input_example
    )
    # 可选：额外保存为 joblib 文件（供 inference 用）
    joblib.dump(model, "iris_model.pkl")        
# # 3. 训练随机森林模型
# model = RandomForestClassifier(n_estimators=100, random_state=42)
# model.fit(X_train, y_train)
# # log 参数 & metrics
# mlflow.log_param("model_type", "RandomForestClassifier")
# mlflow.log_metric("train_score", model.score(X_train, y_train))
# mlflow.log_metric("test_score", model.score(X_test, y_test))
#  # 保存模型
# mlflow.sklearn.log_model(model, "iris_model")

# # 4. 保存模型
# joblib.dump(model, "iris_model.pkl")
# print("✅ 模型已训练并保存为 iris_model.pkl")

