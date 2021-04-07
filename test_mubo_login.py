import requests

# def test_get_homepage():
#     url = 'https://www.mubu.com'
#     method = 'GET'
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
#     }
#     kwargs = {
#         'headers' : headers,
#         'verify' : False
#     }
#     resp = requests.request(method, url, **kwargs)
#     assert resp.status_code == 200
#     # resp_json = resp.json()
#     # # print(resp_json)
#     # assert resp_json
#     print(resp.text)
#
#
# def test_mubu_login():
#     # url = 'https://mubu.com/api/login/submit'
#     url = 'https://mubu.com/login'
#     method = 'GET'
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
#     }
#     kwargs = {
#         'headers' : headers,
#         'verify' : False
#     }
#     resp = requests.request(method, url, **kwargs)
#     assert resp.status_code == 200
#     assert '登录幕布' in resp.text
#     print(resp.text)
#
#
# def test_mubu_login_password():
#     # url = 'https://mubu.com/api/login/submit'
#     url = 'https://mubu.com/login/password'
#     method = 'GET'
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
#     }
#     kwargs = {
#         'headers' : headers,
#         'verify' : False
#     }
#     resp = requests.request(method, url, **kwargs)
#     assert resp.status_code == 200
#     print(resp.text)
#
#
#
# def test_mubu_post_login():
#     # url = 'https://mubu.com/api/login/submit'
#     url = 'https://mubu.com/login/password'
#     method = 'POST'
#     headers = {
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
#         'content - type': 'application / json;    charset = UTF - 8'
#     }
#     data = 'phone=18611527220&password=1qaz%23EDC&remember=true'
#     kwargs = {
#         'headers' : headers,
#         'data': data,
#         'verify' : False
#     }
#     resp = requests.request(method, url, **kwargs)
#     assert resp.status_code == 200
#     print('login_password=======\n'+resp.text)

def test_iod_login():
    url = 'http://124.70.52.190:18001/iodapi/sys_mgr/sign_in'
    method = 'POST'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Content-Type': 'application/json;charset=utf-8'
    }
    data = {"userName":"admin0","password":"WGlhbzEyMyY="}
    kwargs = {
        'headers' : headers,
        'json': data,
        'verify' : False
    }
    # json= 内部自动序列化为JSON
    resp = requests.request(method, url, **kwargs)
    assert resp.status_code == 200
    # print('login_password=======\n'+resp.text)
    return resp.text

def test_iod_login_siteadmin():
    url = 'http://124.70.52.190:18002/iodapi/sys_mgr/build_hdl_connection/siteadmin'
    method = 'POST'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36'
    }
    kwargs = {'headers' : headers}
    # json= 内部自动序列化为JSON
    resp = requests.request(method, url, **kwargs)
    assert resp.status_code == 200
    # print('login_password=======\n'+resp.text)
    resp_json = resp.json()
    # print('id=' + resp_json['obj']['id'])
    # print('userPubKey= ' + str(resp_json['obj']['userPubKey']))
    # print('toBeSigned= ' + resp_json['obj']['toBeSigned'])
    # print('kty or algorithm= ' + resp_json['obj']['algorithm'])
    # print('userPubKey_n= ' + resp_json['obj']['userPubKey']['n'])
    # print('userPubKey_e= ' + resp_json['obj']['userPubKey']['e'])
    return resp_json

def test_iod_login_signWithHdl():
    url = 'http://124.70.52.190:18002/iodapi/sys_mgr/sign_in_with_hdl'
    method = 'POST'
    uName = 'siteadmin',
    passwd = 'c2l0ZWFkbWlu'
    headers = {
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36',
        'Content-Type': 'application/json;charset=UTF-8'
    }
    sign_perf = test_iod_login_siteadmin()

    print('siteadmin====\n'+str(sign_perf))
    sign_id = sign_perf['obj']['id']
    sign_n = sign_perf['obj']['userPubKey']['n']
    sign_e = sign_perf['obj']['userPubKey']['e']
    sign_kty = sign_perf['obj']['userPubKey']['kty']
    sign_algorithm = sign_perf['obj']['algorithm']
    sign_toBeSigned = sign_perf['obj']['toBeSigned']
    sign_signed = sign_perf['obj']['signed']
    data = {
	"userName": uName,
	"password": passwd,
	"iodUser": {
        # "id": "ed922785-b951-4da6-a013-8c38a4e43f79",
        # "userPubKey": {
			# "kty": "RSA",
			# "n": "k7GfsZJM3bEll6tX05JTh7rOgJdgwUPFOVjDakhK8-7gXmNtPA8mS4MKJ6yU9D2wzzrV7rb6pxK4fMu7UdmiRsqTzuDKLvqU5ymX9QWnTBXOUf0YIXrjGOWb8LM6fuVZtP8BkT8_zxq245jPB8GxMsSPbxT8EPPyFfTYZxFbjV2KVisy5n3nyWmsEpgv-LKmMZA6T3KOVYE73HKJ3eS-niqXJZuGP2d8bbjF2lmxfHg_3pYgehR51lRY55Xdc7GeSHji8vCPnW7hZHUBdLMVY5p1jlh494KiTkw7LjilzNxXCtpdPtDI5aqS3nEPw1QmQr1nG2V9k_mRu7I4YVcnwQ",
			# "e": "AQAB"
		 #    },
        # "algorithm": "RSA",
        # "toBeSigned": "MLVV57u+2+FSkbsgowcXfAkIAwYOBgsBBwMOCwoBBQk=",
        # "signed": "fI4gahBdChe/6wB4mh+kk8mWuPpnWDIDDja7E8fPCXeMipHYddMFHmvgZ2WUVRoY5lEGQB6PIN9Tch16svFHPZIoBfmCgw/LCZodI/TyISoVH61Iz9Cjf0MLrxbZAX7taKYFi7rDTGflhN+8aqmNtbhaRqEbkWdzSn4ODW74iq9LO5X838Kmo4xg/ImyyKNmX9i/NBPovDB6j0LXtkRsSFFGvv9dYsRbKpH/EZoBMN5OTWeKDmfHPvNqCc3iPKiDgsCng3zwrlgGsWi5m6ZjfbmaXgEDk4XS5zce5x1+BWfGbKqQBYlaubP54c0WgiM/As9aNwIIbRPzHPZV8qOF2A=="
        "id": sign_id,
        "userPubKey": {
        "kty": sign_kty,
        "n": sign_n,
        "e": sign_e
           },
        "algorithm": sign_algorithm,
        "toBeSigned": sign_toBeSigned,
        "signed": sign_signed
        }
    }
    kwargs = {'headers' : headers,
              'json' : data
              }
    resp = requests.request(method, url, **kwargs)
    assert resp.status_code == 200
    print('login_password=======\n'+resp.text)
    resp_json = resp.json()
    print("resp_json:"+str(resp_json))
    return resp_json


if __name__ == '__main__':
    test_iod_login()