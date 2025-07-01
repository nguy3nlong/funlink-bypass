import requests
import time
import random
type = input('nhập loại nhiệm vụ: ')
rod = random.randint(100000, 999999)
rad = str(rod)
if type == '188bet':
    fheaders = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'origin': 'https://88bet.hiphop',
    'priority': 'u=1, i',
    'referer': 'https://88bet.hiphop/',
    'rid': rad,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
}
    fresponse = requests.options('https://public.funlink.io/api/code/ch', headers=fheaders)
    if fresponse.status_code == 200:
        print('processing (60 seconds)')
        time.sleep(60)
        headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/json',
        'origin': 'https://88bet.hiphop',
        'priority': 'u=1, i',
        'referer': 'https://88bet.hiphop/',
        'rid': rad,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
        }
        json_data = {
       'screen': '1000 x 800',
       'browser_name': 'Safari',
       'browser_version': '100.0.0.0',
       'browser_major_version': '137',
       'is_mobile': False,
       'os_name': 'skibidiOS',
       'os_version': '10000000',
       'is_cookies': True,
       'href': 'https://88bet.hiphop/cach-tinh-tien-bat-ty-so-bong-da/',
       'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
       'hostname': 'https://88bet.hiphop',
        }

        response = requests.post('https://public.funlink.io/api/code/code', headers=headers, json=json_data)
        if response.status_code == 200:
            dat = response.json()
            print(f'your code: {dat['code']}')
        else:
            print(f'fail step 2: {response.status_code}')
    else:
        print(f'fail step 1: {fresponse.status_code}')

elif type == 'w88':
    fheaders = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'origin': 'https://w88vt.com',
    'priority': 'u=1, i',
    'referer': 'https://w88vt.com/',
    'rid': rad,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
}
    fresponse = requests.options('https://public.funlink.io/api/code/ch', headers=fheaders)
    if fresponse.status_code == 200:
        print('processing (60 seconds)')
        time.sleep(60)
        headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/json',
        'origin': 'https://w88vt.com',
        'priority': 'u=1, i',
        'referer': 'https://w88vt.com/',
        'rid': rad,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
        }
        json_data = {
       'screen': '1000 x 800',
       'browser_name': 'Safari',
       'browser_version': '100.0.0.0',
       'browser_major_version': '137',
       'is_mobile': False,
       'os_name': 'skibidiOS',
       'os_version': '10000000',
       'is_cookies': True,
       'href': "https://w88vt.com/",
       'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
       'hostname': "https://w88vt.com",
        }

        response = requests.post('https://public.funlink.io/api/code/code', headers=headers, json=json_data)
        if response.status_code == 200:
            dat = response.json()
            print(f'your code: {dat['code']}')
        else:
            print(f'fail step 2: {response.status_code}')
    else:
        print(f'fail step 1: {fresponse.status_code}')


elif type == 'fun88':
    fheaders = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'origin': 'https://fun88kyc.com',
    'priority': 'u=1, i',
    'referer': 'https://fun88kyc.com/',
    'rid': rad,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
}
    fresponse = requests.options('https://public.funlink.io/api/code/ch', headers=fheaders)
    if fresponse.status_code == 200:
        print('processing (60 seconds)')
        time.sleep(60)
        headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/json',
        'origin': 'https://fun88kyc.com',
        'priority': 'u=1, i',
        'referer': 'https://fun88kyc.com/',
        'rid': rad,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
        }
        json_data = {
       'screen': '1000 x 800',
       'browser_name': 'Safari',
       'browser_version': '100.0.0.0',
       'browser_major_version': '137',
       'is_mobile': False,
       'os_name': 'skibidiOS',
       'os_version': '10000000',
       'is_cookies': True,
       'href': "https://fun88kyc.com/",
       'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
       'hostname': "https://fun88kyc.com",
        }

        response = requests.post('https://public.funlink.io/api/code/code', headers=headers, json=json_data)
        if response.status_code == 200:
            dat = response.json()
            print(f'your code: {dat['code']}')
        else:
            print(f'fail step 2: {response.status_code}')
    else:
        print(f'fail step 1: {fresponse.status_code}')

elif type == 'daga':
    fheaders = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'origin': 'https://stelizabeth.co.uk',
    'priority': 'u=1, i',
    'referer': 'https://stelizabeth.co.uk/',
    'rid': rad,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
}
    fresponse = requests.options('https://public.funlink.io/api/code/ch', headers=fheaders)
    if fresponse.status_code == 200:
        print('processing (60 seconds)')
        time.sleep(60)
        headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/json',
        'origin': 'https://stelizabeth.co.uk',
        'priority': 'u=1, i',
        'referer': 'https://stelizabeth.co.uk/',
        'rid': rad,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
        }
        json_data = {
       'screen': '1000 x 800',
       'browser_name': 'Safari',
       'browser_version': '100.0.0.0',
       'browser_major_version': '137',
       'is_mobile': False,
       'os_name': 'skibidiOS',
       'os_version': '10000000',
       'is_cookies': True,
       'href': "https://stelizabeth.co.uk/",
       'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
       'hostname': "https://stelizabeth.co.uk",
        }

        response = requests.post('https://public.funlink.io/api/code/code', headers=headers, json=json_data)
        if response.status_code == 200:
            dat = response.json()
            print(f'your code: {dat['code']}')
        else:
            print(f'fail step 2: {response.status_code}')
    else:
        print(f'fail step 1: {fresponse.status_code}')


