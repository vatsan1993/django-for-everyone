import requests
response = requests.get('http://127.0.0.1:9000/romeo.txt')
if response.status_code == 200:
    for line in response.text.splitlines():
        print(line)