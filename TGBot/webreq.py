import requests

def getphoto():
    url = 'https://randomfox.ca/floof/'
    resp = requests.get(url)
    if resp.status_code:
        data = resp.json()
        return data.get('image')

if __name__ == '__main__':
    getphoto()