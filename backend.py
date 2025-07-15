from flask import Flask, request, send_from_directory, jsonify
import requests
import re

app = Flask(__name__)


domains = [
    "https://traffic-user.net/GET_MA.php?codexn=taodeptrai&url=https://v9betdi.com/cuoc-thang-ap-dao-la-gi&loai_traffic=https://v9betdi.com/&clk=1000",
    "https://traffic-user.net/GET_MA.php?codexn=taodeptrai&url=https://v9betho.com/ca-cuoc-bong-ro-ao&loai_traffic=https://v9betho.com/&clk=1000",
    "https://traffic-user.net/GET_MA.php?codexn=taodeptrai&url=https://v9betxa.com/cach-choi-craps&loai_traffic=https://v9betxa.com/&clk=1000",
]

success = False
@app.route('/bypass', methods=['POST'])
def k():
    json = request.get_json()
    if not json:
        return jsonify({'error': 'get the fuck out bitch'}), 400
    type = json['type']
    if not type:
        return jsonify({'error': 'get the fuck out bitch'}), 400
    
    if type == 'm88':
        response = requests.post(f'https://traffic-user.net/GET_MA.php?codexn=taodeptrai&url=https://bet88ec.com/cach-danh-bai-sam-loc&loai_traffic=https://bet88ec.com/&clk=1000')
        html = response.text
        match = re.search(r'<span id="layma_me_vuatraffic"[^>]*>\s*(\d+)\s*</span>', html)
        if match:
            code = match.group(1)
            return jsonify({'code': code}), 200
        else:
            return jsonify({'error': 'cannot get code'}), 400

    if type == 'fb88':
        response = requests.post(f'https://traffic-user.net/GET_MA.php?codexn=taodeptrai&url=https://fb88mg.com/ty-le-cuoc-hong-kong-la-gi&loai_traffic=https://fb88mg.com/&clk=1000')
        html = response.text
        match = re.search(r'<span id="layma_me_vuatraffic"[^>]*>\s*(\d+)\s*</span>', html)
        if match:
            code = match.group(1)
            return jsonify({'code': code}), 200
        else:
            return jsonify({'error': 'cannot get code'}), 400

    if type == '188bet':
        response = requests.post(f'https://traffic-user.net/GET_MA.php?codexn=taodeptrailamnhe&url=https://88betag.com/cach-choi-game-bai-pok-deng&loai_traffic=https://88betag.com/&clk=1000')
        html = response.text
        match = re.search(r'<span id="layma_me_vuatraffic"[^>]*>\s*(\d+)\s*</span>', html)
        if match:
            code = match.group(1)
            return jsonify({'code': code}), 200
        else:
            return jsonify({'error': 'cannot get code'}), 400

    if type == 'w88':
        response = requests.post(f'https://traffic-user.net/GET_MA.php?codexn=taodeptrai&url=https://188.166.185.213/tim-hieu-khai-niem-3-bet-trong-poker-la-gi&loai_traffic=https://188.166.185.213/&clk=1000')
        html = response.text
        match = re.search(r'<span id="layma_me_vuatraffic"[^>]*>\s*(\d+)\s*</span>', html)
        if match:
            code = match.group(1)
            return jsonify({'code': code}), 200
        else:
            return jsonify({'error': 'cannot get code'}), 400

    if type == 'v9bet':
        success = False  
        for domain in domains:
            try:
                response = requests.post(domain)
                if response.ok:
                    html = response.text
                    match = re.search(r'<span id="layma_me_vuatraffic"[^>]*>\s*(\d+)\s*</span>', html)
                    if match:
                        code = match.group(1)
                        return jsonify({'code': code}), 200
                    else:
                        print(response.json())
                        continue
            except requests.RequestException as e:
                
                continue

        
        return jsonify({'error': 'cannot get code'}), 400

    if type == 'bk8':
        response = requests.post(f'https://traffic-user.net/GET_MA.php?codexn=taodeptrai&url=https://bk8xo.com/lo-ba-cang-la-gi&loai_traffic=https://bk8xo.com/&clk=1000')
        html = response.text
        match = re.search(r'<span id="layma_me_vuatraffic"[^>]*>\s*(\d+)\s*</span>', html)
        if match:
            code = match.group(1)
            return jsonify({'code': code}), 200
        else:
            return jsonify({'error': 'cannot get code'}), 400

    if type == 'vn88':
        response = requests.post(f'https://traffic-user.net/GET_MA.php?codexn=deobiet&url=https://vn88ie.com/cach-choi-mega-6-45&loai_traffic=https://vn88ie.com/&clk=1000')
        html = response.text
        match = re.search(r'<span id="layma_me_vuatraffic"[^>]*>\s*(\d+)\s*</span>', html)
        if match:
            code = match.group(1)
            return jsonify({'code': code}), 200
        else:
            return jsonify({'error': 'cannot get code'}), 400
