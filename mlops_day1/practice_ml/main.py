# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def home():
#     return {"message": "hello AI"}


# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def home():
#     return {
#         "message": "my first ml api"
#     }


# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/about")
# def about():
#     return {
#         "course": "mlops"
#     }

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/")
# def home():
#     return {"message": "welcome"}

# @app.get("/name")
# def name():
#     return {"name": "asif"}

# @app.get("/course")
# def course():
#     return {"course": "mlops"}

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/predict")
# def predict(age:int):
#     if age > 18:
#         return {"adult": True}
#     else:
#         return {"adult": False}
# print(predict(25))


# from sklearn.linear_model import LinearRegression
# import numpy as np
# import joblib
# from fastapi import FastAPI

# x = np.array([[500], [1000], [1500], [2000]])
# y = np.array([5, 10, 15, 20])

# model = LinearRegression()
# model.fit(x, y)

# joblib.dump(model, "house_model.pk1")
# print("model saved")


# import joblib
# from fastapi import FastAPI
# import numpy as np
# app = FastAPI()
# model = joblib.load("house_model.pk1")
# @app.get("/")
# def home():
#     return {"message": "house price predictor API"}

# @app.get("/predict/{area}")
# def predict(area:float):
#     prediction = model.predict([[area]])
#     return {"area": area, "predicted_price": float(prediction[0])}


# import os
# API_key = os.getenv("API_Key")




# import logging

# logging.basicConfig(
#     level = logging.INFO
# )
# logging.info("Application started")
# print("running---")

# from fastapi import FastAPI
# import logging

# logging.basicConfig(
#     level = logging.INFO
# )
# app = FastAPI()
# @app.get("/")
# def home():
#     logging.info("home endpoint called")
#     return {"message": "hello"}

# import logging
# logging.basicConfig(
#     level = logging.INFO
# )
# try:
#     x = 10/0
# except Exception as e:
#     logging.error(e)


# from sklearn.metrics import accuracy_score
# actual = [1, 0, 1, 1]
# predicted = [1, 0, 0, 1]
# acc = accuracy_score(actual, predicted)
# print(acc)


# import pandas as pd
# train_mean = 30
# production = pd.Series([80, 90, 95, 100])
# prod_mean = production.mean()
# print(prod_mean)


# import time
# start = time.time()
# time.sleep(2)
# end = time.time()
# print(end-start)

# from fastapi import FastAPI
# app = FastAPI()
# @app.get("/health")
# def health():
#     return {"status": "health"}

# import logging
# logging.basicConfig(
#     level = logging.INFO
# )
# prediction = 250000
# logging.info(f"prediction:{prediction}")

# import logging
# from fastapi import FastAPI
# import joblib
# logging.basicConfig(
#     level = logging.INFO
# )
# app = FastAPI()
# @app.get("/")
# def home():
#     logging.info("home endpoint called")
#     return {"message": "hello"}

# model = joblib.load("house_model.pk1")
# @app.get("/predict/{area}")
# def predict(area:float):
#     logging.info(f"prediction request for area:{area}")
#     prediction = model.predict([[area]])
#     return {"prediction": float(prediction[0])}

# from app import add
# def test_add():
#     assert add(2, 3) == 5


# from sklearn.linear_model import LinearRegression
# import joblib
# model = LinearRegression()
# x = [[1],[2],[3]]
# y = [10, 20, 30]
# model.fit(x, y)
# joblib.dump(model, "house_model.pk1")

# def add(a, b):
#     return a + b

from sklearn.linear_model import LinearRegression
import joblib

x = [[1],[2],[3]]
y = [10, 20, 30]
model = LinearRegression()
model.fit(x, y)
joblib.dump(model, "house_model.pkl")
