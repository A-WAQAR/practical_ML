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


import joblib
from fastapi import FastAPI
import numpy as np
app = FastAPI()
model = joblib.load("house_model.pk1")
@app.get("/")
def home():
    return {"message": "house price predictor API"}

@app.get("/predict/{area}")
def predict(area:float):
    prediction = model.predict([[area]])
    return {"area": area, "predicted_price": float(prediction[0])}