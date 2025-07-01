import requests
import time
import random
import re
nurl = input('nhập url: ')
rod = random.randint(100000, 999999)
rad = str(rod)
urlmatch = re.search(r"funlink\.io/([A-Za-z0-9]+)", nurl)

if urlmatch:
    id = urlmatch.group(1)
if not urlmatch:
    print('fail to fetch link')
headers = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'origin': 'https://funlink.io',
    'priority': 'u=1, i',
    'referer': 'https://funlink.io/',
    'rid': rad,
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
}

params = {
    'ignoreId': rad,
    'id': id,
}

response = requests.get('https://public.funlink.io/api/code/renew-key', params=params, headers=headers)
if response.status_code == 200:
    dt = response.json()
    type = dt["data_keyword"]["keyword_text"]
    ids = dt["data_keyword"]["id"]
    print(f'type: {type}')
    print(f'id: {ids}')
else:
    print('fail to fetch keyword')
if type == '188Bet':
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

if type == 'kubet':
    fheaders = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'origin': 'https://www.randalls.uk.com',
    'priority': 'u=1, i',
    'referer': 'https://www.randalls.uk.com/',
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
        'origin': 'https://www.randalls.uk.com',
        'priority': 'u=1, i',
        'referer': 'https://www.randalls.uk.com/',
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
       'href': 'https://www.randalls.uk.com/saba-sports-kubet-casino',
       'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
       'hostname': 'https://www.randalls.uk.com',
        }

        response = requests.post('https://public.funlink.io/api/code/code', headers=headers, json=json_data)
        if response.status_code == 200:
            dat = response.json()
            print(f'your code: {dat['code']}')
        else:
            print(f'fail step 2: {response.status_code}')
    else:
        print(f'fail step 1: {fresponse.status_code}')

if type == '8xbet 8xbetvina.com':
    fheaders = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'origin': 'https://8xbetvina.com',
    'priority': 'u=1, i',
    'referer': 'https://8xbetvina.com/',
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
        'origin': 'https://8xbetvina.com',
        'priority': 'u=1, i',
        'referer': 'https://8xbetvina.com/',
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
       'href': 'https://8xbetvina.com/8xbet-hoan-tra-e-sports-nhan-1-2-moi-ngay-khong-gioi-han.html',
       'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
       'hostname': 'https://8xbetvina.com',
        }

        response = requests.post('https://public.funlink.io/api/code/code', headers=headers, json=json_data)
        if response.status_code == 200:
            dat = response.json()
            print(f'your code: {dat['code']}')
        else:
            print(f'fail step 2: {response.status_code}')
    else:
        print(f'fail step 1: {fresponse.status_code}')

if type == 'trang cá cược':
    fheaders = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'origin': 'https://chisholmunitedfc.com',
    'priority': 'u=1, i',
    'referer': 'https://chisholmunitedfc.com/',
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
        'origin': 'https://chisholmunitedfc.com',
        'priority': 'u=1, i',
        'referer': 'https://chisholmunitedfc.com/',
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
       'href': 'https://chisholmunitedfc.com/huong-dan/',
       'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
       'hostname': 'https://chisholmunitedfc.com',
        }

        response = requests.post('https://public.funlink.io/api/code/code', headers=headers, json=json_data)
        if response.status_code == 200:
            dat = response.json()
            print(f'your code: {dat['code']}')
        else:
            print(f'fail step 2: {response.status_code}')
    else:
        print(f'fail step 1: {fresponse.status_code}')

if type == 'lu88 vnco':
    fheaders = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'origin': 'https://lu88vn.co.uk',
    'priority': 'u=1, i',
    'referer': 'https://lu88vn.co.uk/',
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
        'origin': 'https://lu88vn.co.uk',
        'priority': 'u=1, i',
        'referer': 'https://lu88vn.co.uk/',
        'rid': rad,
        'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
        }
        json_data = {
       'screen': '1000 x 1000',
       'browser_name': 'Safari',
       'browser_version': '100.0.0.0',
       'browser_major_version': '137',
       'is_mobile': False,
       'os_name': 'skibidiOS',
       'os_version': '10000000',
       'is_cookies': True,
       'href': 'https://lu88vn.co.uk/game-bai-lu88/',
       'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
       'hostname': 'https://lu88vn.co.uk',
        }

        response = requests.post('https://public.funlink.io/api/code/code', headers=headers, json=json_data)
        if response.status_code == 200:
            dat = response.json()
            print(f'your code: {dat['code']}')
        else:
            print(f'fail step 2: {response.status_code}')
    else:
        print(f'fail step 1: {fresponse.status_code}')

if type == 'm88lu':
    fheaders = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'origin': 'https://m88lu.io',
    'priority': 'u=1, i',
    'referer': 'https://m88lu.io/',
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
        'origin': 'https://m88lu.io',
        'priority': 'u=1, i',
        'referer': 'https://m88lu.io/',
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
       'href': 'https://m88lu.io/da-ga-m88/',
       'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
       'hostname': 'https://m88lu.io',
        }

        response = requests.post('https://public.funlink.io/api/code/code', headers=headers, json=json_data)
        if response.status_code == 200:
            dat = response.json()
            print(f'your code: {dat['code']}')
        else:
            print(f'fail step 2: {response.status_code}')
    else:
        print(f'fail step 1: {fresponse.status_code}')

headers = {
    'accept': 'application/json',
    'accept-language': 'en-US,en;q=0.9',
    'content-type': 'application/json',
    'origin': 'https://funlink.io',
    'priority': 'u=1, i',
    'referer': 'https://funlink.io/',
    'rid': rad,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
}

json_data = {
    'browser_name': 'skibidu',
    'browser_version': '99999',
    'os_name': 'SkibidiOS',
    'os_version': '10000',
    'os_version_name': '1000',
    'keyword_answer': dat['code'],
    'link_shorten_id': id,
    'keyword': type,
    'ip': '',
    'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
    'device_name': 'desktop',
    'token': '',
    'keyword_id': ids,
}

response = requests.post('https://public.funlink.io/api/url/tracking-url', headers=headers, json=json_data)
if response.status_code == 200:
    dtt = response.json()
    print(f'link: {dtt["data_link"]['url']}')
else:
    print('fail!')
print('nếu không có phẩn hồi nghĩa là loại nhiệm vụ chưa được hỗ trợ')
