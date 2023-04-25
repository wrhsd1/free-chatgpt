from chatgpt import GPT_VERCEL as Chatgpt
from flask import Flask, request,  jsonify,stream_with_context,Response



app = Flask(__name__)

@app.route('/')
def __index():
    return "hello"


@app.route('/api', methods=['GET', 'POST'])
def _openai():
    
    messages = request.json.get("messages",'')
    model = request.json.get("model","openai:gpt-3.5-turbo")
    txt = request.json.get("prompt","")

    chatgpt = Chatgpt()
    res = chatgpt.ask(txt,model)
    return res


@app.route('/<path:path>', methods=['GET', 'POST'])
def _openai2(path):

    def generate(res):
        # res 原来的全部文本
        for xx in res:
        
  
            x2x_json = {"choices":[{"delta":{"content":xx}}]}
            
            x3x_str = json.dumps(x2x_json)
            
            x4x_str = f"data: {x3x_str}\n\n"
            
            x5x_byte = x4x_str.encode('utf-8')
            
            yield x5x_byte


    messages = request.json.get("messages",'')
    #print(messages) # chatgpt应用端发送的 消息，含历史上下文和问题。
    
    txt = ''
    for i in messages:
        txt = txt + f"{i.get('role')}:{i.get('content')}\n\n"
        
    model = request.json.get("model","openai:gpt-3.5-turbo")
    
    #print('q:',txt)
    #print('model:',model)


    with app.app_context():
        chatgpt = Chatgpt()

        #res = '我是AI助手，没有固定的名字。'
        #res = 'assistant:我是AI助手，没有固定的名字。'
        res = chatgpt.ask(txt,model)
        #print(res) #原始全文字符串
        if res.startswith('assistant:'):
            res = res[11:]


        return Response(stream_with_context(generate(res)),mimetype='text/event-stream') # 原始全文字符串转为stream 格式返回给应用端
    
        



        

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=8080)
    
    
#应用端 修改 base_url 为 http://ip:8080/v1  可以用 openai api 接口的格式请求，stream 返回
#这个代理获取网页内容不是流，但是暴露给应用端是流返回。
#便于接入给应用端原来配置或者规则是流请求。
    
    
