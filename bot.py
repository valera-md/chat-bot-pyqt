class _Bot:
# semantic versioning
 version = "1.0.0"
 def __init__(self, name):
  if len(name) >= 3:
   self.name = name
  else:
   print("ERROR: bot name must be at least 3 characters")
   exit()

 def replyTo(self, message):
  return f"{self.name}: Hello!"
 
#pip install requests
#https://platform.openai.com/docs/api-reference/authentication - документация по подключению к чат боту
import requests
import json
class _BotOPENAI(_Bot):
 def __init__(self, name):
  super().__init__(name)
 def replyTo(self, message):
  headers = {"Authorization": f"Bearer {self.gpt_key}" }
  if self.model.startswith("gpt-"):
   payload = { 
    "model": "self.model", 
    "messages": [{"role": "user", "content": message}],
} 
  elif self.model.startswith("dall-e-"):
   payload = { 
    "model": "self.model", 
    "prompt": message,
} 
  #res = requests.post("https://api.openai.com/v1/chat/completions", 
  res = requests.post(
  f"https://api.openai.com{self.url}", 
  headers=headers, 
  json=payload
) 
  if res.status_code == 200:
   response = res.content.decode('utf-8')
   data = json.loads(response)
   if self.model.startswidth("gpt-"):
    return data["choices"][0]["message"]["content"], "text"
   elif self.model.startswidth("dall-e-"):
    return data["data"][0]["url"], "image"
  else:
   return "Error\n\n" + str(res) + str(res.content)
  #print(res.status_code)
  #print(res.content)

class BotBuilder:
 def __init__(self, botType, botName):
# HWl: use match/case]
  match botType:
   case "openai":
    self.__bot = _BotOPENAI(botName)
   case "csv":
   #self.__bot = _BotCSV(botName)
    pass
   case _:
    raise TypeError("This bot does not support {botType}")
 def withKey(self,key):
  self.__bot.gpt_key = key
  return self
 #def withLang(self,lang):
 # self.__bot.lang = lang
 # return self
 #def withDomain(self,domain):
 # self.__bot.domain = domain
 # return self
 def withModel(self,model):
  self.__bot.model = model
  return self
 def withUrl(self,url):
  self.__bot.url = url
  return self
 def build(self):
  return self.__bot
#Все промежуточные методы ретурнят, возвращают ссылку обратно на текущий билдер, почему? - чтоб можно было цепочку вызывать.
#Чтоб можно было из билдера, вызывая опцию, которая что-то включает, чтобы тут сформировался объект, к которому мы можем следующую опцию, метод следующей опции вызвать.
#build это тот метод, который имеет доступ к текущему, никакой параметр не получает и возвращает ссылку на конструируемый объект, то есть в нашем случае на наш бот - __bot.
#403 forbiden, не туда попал
#400 bad request, формат сообщения должен отличаться