import requests
import os


data = {
        'from': 'AUTO',
        'to': 'AUTO',
        'smartresult': 'dict',
        'client': 'fanyideskweb',
        'salt': '15881340026715',
        'sign': '5cf0db6ba3ec245fa0c6e3ce00e47395',
        'ts': '1588134002671',
        'bv': 'aba2eb413aab2b3c6b790cc4b2ce2dc8',
        'doctype': 'json',
        'version': '2.1',
        'keyfrom': 'fanyi.web',
        'action': 'FY_BY_REALTlME'
}

web_headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36 Edg/84.0.522.40'
}

class Youdao():
    def __init__(self):
        self.scr = ''
        self.tgt = ""
        self.inputs_text = ""
        self.main_path = os.getcwd()
        self.youdao_url = 'http://fanyi.youdao.com/translate?smartresult=dict&smartresult=rule'
        self.headers = web_headers
        self.data = data

    def os_file(self):
        if not os.path.exists(os.path.join(self.main_path, "translation")):
           os.mkdir(os.path.join(self.main_path, "translation"))
           print(f'已在{self.main_path}创建translation文件夹')


    def write_json(self, write_json_info):  # 将信息写入txt文件
        with open(os.path.join(self.main_path, "translation", f"{self.scr}翻译结果.txt"), 'w', encoding='utf-8') as fb:
            print("已在{}文件夹创建 {}翻译结果.txt".format(os.path.join(self.main_path, "translation"), self.scr))
            fb.write(str(write_json_info))


    def inputs(self):
        self.inputs_text = input('请输入您需要翻译的内容：')
        while not self.inputs_text:
            self.inputs_text = input('请输入您需要翻译的内容：')
        self.data['i'] = self.inputs_text
            
            
    def requests_post(self):
        self.inputs()
        req_post = requests.post(url=self.youdao_url,data=self.data,headers=self.headers).json()
        for translateResult in req_post['translateResult']:
            for translateResult_list in translateResult:
                self.scr = translateResult_list['src']
                self.tgt = translateResult_list['tgt']
                result = "输入内容" + self.scr + "\n翻译结果:" + self.tgt
            print(result)
        if len(self.inputs_text) == 0:
            pass
        else:
            self.write_json(result)
                
if __name__ == '__main__':
    Youdao = Youdao()
    Youdao.os_file()
    while True:
        Youdao.requests_post()