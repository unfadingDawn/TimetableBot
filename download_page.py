import requests

response = requests.get("https://rasp.yandex.ru/suburban/universitetskaya-saint-petersburg-and-leningradskaya-oblast"
                        "--sankt-peterburg-baltiyskiy/today")

text = response.text

f = open("page.html", "a")
f.write(text)
f.close()
