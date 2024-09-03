import tls_client

api = "https://mineshaft.help/api/submit"
headers = {"Content-Type": 'text/plain;charset=utf-8'}
data = "https://google.com"
r = tls_client.Session().post(api, headers=headers, data=data)

print(r.status_code, r.text)