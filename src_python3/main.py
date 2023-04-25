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

if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0',port=8080)
    
