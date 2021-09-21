import requests


APP_URL = "http://localhost:8000"
RESOURCES = [""]


r = requests.get(f"{APP_URL}/slow")


print(r.text)

r = requests.get(f"{APP_URL}/fast")


print(r.text)

r = requests.get(f"{APP_URL}/stuck")


print(r.text)

def test(resource: str, mode: str) -> requests.Response:

    return




if __name__ == "__main__":
    print()