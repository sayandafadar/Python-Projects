#from requests.auth import HTTPBasicAuth
import requests
from datetime import datetime

APP_ID = "1dbdf9ba"
API_KEY = "6afe974e5e8b5a1f10b982243280239a"

GENDER = "Male"
WEIGHT_KG = 56
HEIGHT_CM = 164.2
AGE = 17

exercise_endpoint = "https://trackapi.nutritionix.com/v2/natural/exercise"

exercise_text = input("Tell me which exercises you did: ")

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "Authorization": "Basic bnVsbDpudWxs"
}

parameters = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
    "height_cm": HEIGHT_CM,
    "age": AGE
}

response = requests.post(exercise_endpoint, json=parameters, headers=headers)
result = response.json()

sheety_url = "https://api.sheety.co/7439e064d24da5ff3b9e0ce82e7c7dae/myWorkouts/workouts"
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")
bearer_headers = {
"Authorization": "Basic c2F5YW5vbWk6Ym5Wc2JEcHVkV3hz"
}


for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    sheet_response = requests.post(
        sheety_url,
        json=sheet_inputs,
        auth=(
            "sayanomi",
            "bnVsbDpudWxs",
        )
    )

    sheet_response = requests.post(sheety_url, json=sheet_inputs, headers=bearer_headers)

    print(sheet_response.text)
#requests.get('https://api.github.com/user', auth=HTTPBasicAuth('sayanomi', 'bnVsbDpudWxs'))
