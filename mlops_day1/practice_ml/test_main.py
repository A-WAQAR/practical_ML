
# from main import add
# def test_add():
#     assert add(2, 3) == 5
    


import os
def test_model():
    assert os.path.exists(
        "house_model.pkl"
    )
