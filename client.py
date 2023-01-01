import requests

requests.post(
   "http://0.0.0.0:3000/classify",
   headers={"content-type": "application/json"},
   data="[[5.9, 3, 5.1, 1.8]]",
).text