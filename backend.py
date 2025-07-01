from flask import Flask, request, send_from_directory, jsonify
import requests
import re
import random
import time
rod = random.randint(100000, 999999)
rad = str(rod)

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
    print(response.json())
    if response.status_code == 200:
        dtt = response.json()
        return(dtt["data_link"]['url'])
    else:
        return('cai dit me may')


app = Flask(__name__)

@app.route('/ch', methods=['POST'])
def c():
    json = request.get_json()
    if not json:
        return jsonify({'error': 'get the fuck out bitch'}), 400
    rurl = json['url']
    if not rurl:
        return jsonify({'error': 'get the fuck out bitch'}), 400
    urlmatch = re.search(r"funlink\.io/([A-Za-z0-9]+)", rurl)
    if urlmatch:
        id = urlmatch.group(1)
    if not urlmatch:
        return jsonify({'error': 'get the fuck out bitch'}), 400
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
            return jsonify({'error': 'get the fuck out bitch'}), 400
        type = dt["data_keyword"]["keyword_text"]
        ids = dt["data_keyword"]["id"]
        print(type)
        print(ids)
    else:
        return jsonify({'error': 'failed'}), 400
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
                code = getlink(dat['code'], ids, id, type)
                if code == 'cai dit me may':
                    return jsonify({'error': 'failed'}), 400
                else:
                    return jsonify({'success': code}), 200
                
            else:
                return jsonify({'error': 'failed'}), 400
        else:
            return jsonify({'error': 'failed'}), 400

    if type == 'w88':
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
       'href': 'https://w88vt.com/',
       'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
       'hostname': 'https://w88vt.com',
        }
            response = requests.post('https://public.funlink.io/api/code/code', headers=headers, json=json_data)
            if response.status_code == 200:
                dat = response.json()
                code = getlink(dat['code'], ids, id, type)
                if code == 'cai dit me may':
                    return jsonify({'error': 'failed'}), 400
                else:
                    return jsonify({'success': code}), 200              
                
            else:
                return jsonify({'error': 'failed'}), 400
        else:
            return jsonify({'error': 'failed'}), 400
    
    if type == 'fun88':
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
       'href': 'https://fun88kyc.com/',
       'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
       'hostname': 'https://fun88kyc.com',
        }
            response = requests.post('https://public.funlink.io/api/code/code', headers=headers, json=json_data)
            if response.status_code == 200:
                dat = response.json()
                code = getlink(dat['code'], ids, id, type)
                if code == 'cai dit me may':
                    return jsonify({'error': 'failed'}), 400
                else:
                    return jsonify({'success': code}), 200              
                
            else:
                return jsonify({'error': 'failed'}), 400
        else:
            return jsonify({'error': 'failed'}), 400

    if type == 'đá gà trực tiếp':
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
       'href': 'https://stelizabeth.co.uk/',
       'user_agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 13_5_2) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.5 Safari/605.1.15',
       'hostname': 'https://stelizabeth.co.uk',
        }
            response = requests.post('https://public.funlink.io/api/code/code', headers=headers, json=json_data)
            if response.status_code == 200:
                dat = response.json()
                code = getlink(dat['code'], ids, id, type)
                if code == 'cai dit me may':
                    return jsonify({'error': 'failed'}), 400
                else:
                    return jsonify({'success': code}), 200             
                
            else:
                return jsonify({'error': 'failed'}), 400
        else:
            return jsonify({'error': 'failed'}), 400

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
                code = getlink(dat['code'], ids, id, type)
                if code == 'cai dit me may':
                    return jsonify({'error': 'failed'}), 400
                else:
                    return jsonify({'success': code}), 200             
                
            else:
                return jsonify({'error': 'failed'}), 400
        else:
            return jsonify({'error': 'failed'}), 400

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
                code = getlink(dat['code'], ids, id, type)
                if code == 'cai dit me may':
                    return jsonify({'error': 'failed'}), 400
                else:
                    return jsonify({'success': code}), 200               
                
            else:
                return jsonify({'error': 'failed'}), 400
        else:
            return jsonify({'error': 'failed'}), 400
        
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
       'hostname': 'https://chisholmunitedfc.com/',
        }
            response = requests.post('https://public.funlink.io/api/code/code', headers=headers, json=json_data)
            if response.status_code == 200:
                dat = response.json()
                code = getlink(dat['code'], ids, id, type)
                if code == 'cai dit me may':
                    return jsonify({'error': 'failed'}), 400
                else:
                    return jsonify({'success': code}), 200               
                
            else:
                return jsonify({'error': 'failed'}), 400
        else:
            return jsonify({'error': 'failed'}), 400

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
       'screen': '1000 x 800',
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
                code = getlink(dat['code'], ids, id, type)
                if code == 'cai dit me may':
                    return jsonify({'error': 'failed'}), 400
                else:
                    return jsonify({'success': code}), 200              
                
            else:
                return jsonify({'error': 'failed'}), 400
        else:
            return jsonify({'error': 'failed'}), 400

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
                code = getlink(dat['code'], ids, id, type)
                if code == 'cai dit me may':
                    return jsonify({'error': 'failed'}), 400
                else:
                    return jsonify({'success': code}), 200         
                
            else:
                return jsonify({'error': 'failed'}), 400
        else:
            return jsonify({'error': 'failed'}), 400
    
    else:
        return jsonify({'error': 'unsupported'}), 400


