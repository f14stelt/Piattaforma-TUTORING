import json
import urllib2

data = 'cid=&pin=&pwd=Matteo00&target=&uid=G4124356H'

req = urllib2.Request('https://web.spaggiari.eu/auth-p7/app/default/AuthApi4.php?a=aLoginPwd')
req.add_header('Content-Type', 'application/x-www-form-urlencoded; charset=UTF-8')
req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36')
req.add_header('Referer', 'https://web.spaggiari.eu/home/app/default/login.php?ch=scuola')
response = urllib2.urlopen(req, data)

j = json.loads(response.read())
if str(j["data"]["auth"]["verified"]) == "False":
	print("Username o password errati")
elif str(j["data"]["auth"]["verified"]) == "True":
	print("Accesso eseguito")
	print(" Nome = "+j["data"]["auth"]["accountInfo"]["nome"])
	print(" Cognome = "+j["data"]["auth"]["accountInfo"]["cognome"])
	print(" ID Istituto = "+j["data"]["auth"]["accountInfo"]["cid"])