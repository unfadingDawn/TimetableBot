import requests
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}

response = requests.get("https://rasp.yandex.ru/suburban/universitetskaya-saint-petersburg-and-leningradskaya-oblast"
                        "--sankt-peterburg-baltiyskiy/today", headers=headers)

text = response.text

f = open("page.html", "a")
f.write(text)
f.close()
