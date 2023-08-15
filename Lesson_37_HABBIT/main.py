import requests
import datetime

PIXELA_TOKEN = "asDGasdgSDFGasdfgdg"
PIXELA_USERNAME = "bebopjunky"
PIXELA_GRAPH = "graph1"
today = datetime.date.today()
TODAY = today.strftime("%Y%m%d")

PIXELA_USER_ENDPOINT = "https://pixe.la/v1/users"
PIXELA_GRAPH_ENDPOINT = f"{PIXELA_USER_ENDPOINT}/{PIXELA_USERNAME}/graphs"
PIXELA_PIXEL_POST_ENDPOINT = f"{PIXELA_USER_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH}"
PIXELA_PIXEL_PUT_ENDPOINT = f"{PIXELA_USER_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH}/{TODAY}"
PIXELA_PIXEL_DEL_ENDPOINT = f"{PIXELA_USER_ENDPOINT}/{PIXELA_USERNAME}/graphs/{PIXELA_GRAPH}"

pixela_parameters = {
    "token": PIXELA_TOKEN,
    "username": PIXELA_USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

#response = requests.post(url=PIXELA_USER_ENDPOINT, json=pixela_parameters)

graph_parameters = {
    "id": PIXELA_GRAPH,
    "name": "Coding History",
    "unit": "min",
    "type": "int",
    "color": "shibafu"
}

headers = {
    "X-USER-TOKEN": PIXELA_TOKEN
}

#response = requests.post(url=PIXELA_GRAPH_ENDPOINT,json=graph_parameters,headers=headers)



pixel_post_parameters = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "120"
}
#response = requests.post(url=PIXELA_PIXEL_POST_ENDPOINT,json=pixel_post_parameters,headers=headers)

pixel_put_parameters = {
    "quantity": "180"
}

response = requests.put(url=PIXELA_PIXEL_PUT_ENDPOINT,json=pixel_put_parameters,headers=headers)