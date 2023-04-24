
from chatgpt import GPT_VERCEL as Chatgpt

chatgpt = Chatgpt()


ask = '你的名字是什么？'
# ask = '用python写个冒泡排序'
model = 'openai:gpt-3.5-turbo'
#model = 'cohere:command-xlarge-nightly'

res = chatgpt.ask(ask,model)
print(res)


