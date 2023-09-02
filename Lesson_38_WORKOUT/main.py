import requests
from datetime import datetime

NUTRITIONIX_API = ""
NUTRITIONIX_ID = ""
EXERCISE_ENDPOINT = "https://trackapi.nutritionix.com/v2/natural/exercise"
GENDER = "male"
WEIGHT = 100
HEIGHT = 190
AGE = 40


DATE = datetime.now().strftime("%d/%m/%Y")
TIME = datetime.now().strftime("%X")


SHEETY_ENDPOINT_POST = "https://api.sheety.co/b8023ce17e732b7f6fcd401ea2f7926d/myWorkouts/workouts"

nutrition_headers = {
    "x-app-id": NUTRITIONIX_ID,
    "x-app-key": NUTRITIONIX_API,
}

text = input(": ")

nutrition_parameters = {
    "query": text,
    "gender": GENDER,
    "weight_kg": WEIGHT,
    "height_cm": HEIGHT,
    "age": AGE
}

response = requests.post(EXERCISE_ENDPOINT, json=nutrition_parameters, headers=nutrition_headers)
result = response.json()



for exercise in result["exercises"]:
    sheety_parameters = {
        "workout": {
            "date": DATE,
            "time": TIME,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

sheety_headers = {
    "Authorization": "Bearer "
}

sheety_response = requests.post(SHEETY_ENDPOINT_POST,json=sheety_parameters,headers=sheety_headers)
sheety_result = sheety_response.json()
print(sheety_result)