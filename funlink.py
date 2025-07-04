import requests
import random
import time
import re
rod = random.randint(100000, 999999)
rad = str(rod)

surl = input('nhập link rút gọn: ')

def funlink(rurl):
    def getlink(dot, ids, id, type):
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
    'keyword_answer': dot,
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
            return(dtt["data_link"]['url'])
        else:
            return('cai dit me may')







    if not rurl:
        return('url missing')
    urlmatch = re.search(r"funlink\.io/([A-Za-z0-9]+)", rurl)
    if urlmatch:
        id = urlmatch.group(1)
    if not urlmatch:
        return('not match url')
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
        if not dt:
            return('failed')
        urls = dt["data_keyword"]["url_destination"]
        ids = dt["data_keyword"]["id"]
        type = dt["data_keyword"]["keyword_text"]
        aurls = f'{urls}404'
     
    else:
        return('failed')
 
    fheaders = {
    'accept': '*/*',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'origin': urls,
    'priority': 'u=1, i',
    'referer': urls,
    'rid': rad,
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
}
    fresponse = requests.options('https://public.funlink.io/api/code/ch', headers=fheaders)
    if fresponse.status_code == 200:
        time.sleep(60)
        headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'content-type': 'application/json',
        'origin': urls,
        'priority': 'u=1, i',
        'referer': urls,
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
       'href': aurls,
       'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
       'hostname': urls,
        }
        response = requests.post('https://public.funlink.io/api/code/code', headers=headers, json=json_data)

        if response.status_code == 200:
            dat = response.json()
            code = getlink(dat['code'], ids, id, type)
            if code == 'cai dit me may':
                return('failed')
            else:
                return(code)
                
        else:
            return('failed')
    else:
        return('failed')
        


link = funlink(surl)
print(link)
