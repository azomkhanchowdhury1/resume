import requests

url = 'https://resume-wfw9.onrender.com/contact/'
client = requests.session()
# First get the CSRF token from home page
try:
    res = client.get('https://resume-wfw9.onrender.com/')
    print("GET status:", res.status_code)
    if 'csrftoken' in client.cookies:
        csrftoken = client.cookies['csrftoken']
        headers = {'X-CSRFToken': csrftoken, 'Referer': 'https://resume-wfw9.onrender.com/'}
        data = {'name': 'Azom', 'email': 'test@test.com', 'message': 'Hello'}
        post_res = client.post(url, data=data, headers=headers)
        print("POST status:", post_res.status_code)
        print("POST body:", post_res.text)
    else:
        print("No CSRF token found in cookies!")
except Exception as e:
    print("Error:", e)
