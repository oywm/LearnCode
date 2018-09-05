import urllib.request
import urllib.parse
import json


url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
headers = {
    'X-Requested-With': 'XMLHttpRequest',
    'Accept': 'application/json, text/javascript, */*; q=0.01',
    'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/63.0.3239.132 Safari/537.36"
}
word = input('请输入要翻译的英文单词: ')
form_data = {
    'i': word,
    'from': 'AUTO',
    'to': 'AUTO',
    'smartresult': 'dict',
    'client': 'fanyideskweb',
    'salt': '1535942246351',
    'sign': '265a31955f3e4a6c51c7a0a0e486d67b',
    'doctype': 'json',
    'version': '2.1',
    'keyfrom': 'fanyi.web',
    'action': 'FY_BY_CLICKBUTTON',
    'typoResult': 'true'
}

data = bytes(urllib.parse.urlencode(form_data), encoding='utf-8')

request = urllib.request.Request(url, data, headers)
response = (urllib.request.urlopen(request).read()).decode('utf-8')
print(response)
json_data = json.loads(response)
result = json_data['translateResult'][0][0]['tgt']
print(result)
