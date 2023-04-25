from diy_ua import random_user_agent as get_ua
from requests import Session

class GPT_VERCEL:

    def __init__(self:object) -> None:
        self.base_url = 'https://play.vercel.ai'
        self.session = Session()
        self.session.headers.update({
            'origin': self.base_url,
            'referer': self.base_url
        })
        self._cache_user_agents = []

    def Custom_Encoding(self:object) -> str:
        url = f'{self.base_url}/openai.jpeg'
        headers = {'User-Agent': get_ua()}
        try:
            res = self.session.get(url, headers=headers).text
            return res + '.'
        except Exception as e:
            print(e)
            return ''
    
    def content_analysis(self:object,txt:str) -> str:
        #print(txt)
        #txt = ''.join([i[1:-1] for i in txt.split('\n') if len(i)>2]) #按换行符分割 
        #txt = ''.join([i[1:-1] for i in txt.splitlines() if len(i)>2]) #按行分割
        txt = ''.join([i[1:-1].replace('\\n','\n') for i in txt.splitlines() if len(i)>2]) #按行分割,修复回复内容换行符不换行。
        #print('=='*20)
        #print(txt)
        
        return txt





    
    def ask(self:object,prompt,model) -> str:
        url = f'{self.base_url}/api/generate'
        headers = {'User-Agent': get_ua(),
                   'custom-encoding': self.Custom_Encoding(),
                   'Connection': 'keep-alive',
                   'Referer':self.base_url,
                   'Accept': '*/*',
                   'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8',
                   'DNT': '1'}
        params = {
            'prompt': prompt,
            'model': model,
            'temperature': 0.9,
            'max_tokens': 100,
            'top_p': 1,
            'frequency_penalty': 0,
            'presence_penalty': 0,
            'stop_sequences': ['```']
        }
        try:
            res = self.session.post(url, headers=headers, json=params)
            return self.content_analysis(res.text)
            
        except Exception as e:
            print(e)
            return ''
