import requests

def send_otp(otp):
    # Server URL
    url = "https://127.0.0.1:4443"

    data = f"otp:verify:{otp}:newUser"

    response = requests.post(url, data=data, verify=False)
    # Print server response
    print(response.text)

def generate_otp():
    # Server URL
    url = "https://127.0.0.1:4443"

    data = f"otp:generate:newUser"

    response = requests.post(url, data=data, verify=False)
    # Print server response
    print(response.text)

send_otp(399807)
# generate_otp()