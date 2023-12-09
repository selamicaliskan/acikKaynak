import requests
try:
	response=requests.get("https://dog.ceo/api/breeds/image/random")
	response_data=response.json()
	print("DOG IMAGE MESSAGE -> ",response_data["message"],"\nRETURN -> ",response_data["status"])
except requests.exceptions.Timeout:
	print("TimeOut")
except requests.exceptions.TooManyRedirects:
	print("Try different URL")
except requests.exceptions.RequestException as e:
	raise SystemExit(e)

