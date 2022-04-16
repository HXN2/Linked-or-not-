from colorama import *
print(Fore.BLUE+" [£] All Copy rights reserved© to @hxn_here << insta")
#Thanks For Mr.Joker (:
try:
	import threading,phonenumbers,socket,re,requests,json
	from colorama import *
	from threading import Thread,Lock
	from phonenumbers import carrier
	from time import sleep
	from random import choice
	from requests import get,post
	import urllib.parse as urlparse
except Exception as e:exit(e)
LINX={"K","k","1"};PHON={"P","p","2"}
PRNT = Lock();theards =[]
red = "\033[1;31;40m";yel = '\033[1;33;40m'
bloFT = "\033[1;36;40m"
grn = '\033[1;32;40m';wit = "\033[1;37;40m"
try:
    import requests
    import socket as s
    import webbrowser
    from sys import platform
    import colorama

except ModuleNotFoundError:
    os.system("pip install requests")
    os.system("pip install socket")
    os.system("pip install webbrowser")
    os.system("pip install sys")
    os.system("pip install platform")
    os.system("pip install colorama")
import webbrowser
url = "https://t.me/HEXiN1K"
webbrowser.open(url)
from sys import platform
from colorama import *
import socket
import requests

name = socket.gethostname()
myHostName = socket.gethostname()

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print("\n===========================================================")
name = ("""\n                    Hello sir """ +name+Style.RESET_ALL)
print(name)
host = ("""\n                  Your platform is """+ platform+Style.RESET_ALL)
print(host)

api = "https://api.ipify.org/?format=json"
req = requests.get(api)
response = req.json()
a = response["ip"]

IP = ("""\n                Your Local iP is """+Fore.RED+a+Style.RESET_ALL)
print(IP)

v = (Fore.RED+"""\n                    Your iNFO PROXY is\n"""+Style.RESET_ALL)

print(v)
print(s)

print("\n===========================================================")

lib = input("""
\n  من صنع هيكسن انستجرام @hxn_here
\n  BY HEXiN INSTA @hxn_here
\n  tarafından yapılmış HEXiN Instagram @hxn_here
\n
===========================================================
\n   من صنع هيكسن تيليجرام @HEXiN 
\n  BY HEXiN TELeGRaM @HEXiN1K
\n  Bir telgraf HEXiN oluşturun @HEXiN1K
\n ===========================================================
 
 [1] DOWNLOAD LiP & UPDATE . تنزيل وتحديث المكاتب

\n [2] SKiP DOWNLOAD & UPDATE LiP . تخطي تنزيل وتحديث المكاتب 

\n [+] Please Choice >> """)
import os
if lib == "1":
    try:
        os.system('pip install requests')
        os.system('pip install webbrowser')
        os.system('pip install socket')
        os.system('pip install sys')  
        os.system('pip install colorama')
        os.system('pip install threading')
        os.system('pip install phonenumbers')
        os.system('pip install time')
        os.system('pip install random')
        os.system('pip install urllib.parse')
        os.system('cls' if os.name == 'nt' else 'clear')
        pass
    except:
        pass
else:
    os.system('cls' if os.name == 'nt' else 'clear')
    pass
os.system('clear')
import requests
import webbrowser
import time as mm
import sys as n
import threading,phonenumbers,socket,re,requests,json
from colorama import *
from threading import Thread,Lock
from phonenumbers import carrier
from time import sleep
from random import choice
from requests import get,post
import urllib.parse as urlparse
def slow(M):
	for c in M + '\n':
		n.stdout.write(c)
		n.stdout.flush()
		mm.sleep(1. / 60)
slow(Fore.RED+"""
 ...........................................................  

   
  Coded BY HEXiN inStAGrAm : @hxn_here
  
  TeLEGram programmer : @HEXiN1K 

........................................................... 
                                                 """)
bn = (Fore.CYAN+"""  .-.    _       .-.            .-.
  : :   :_;      : :.-.         : :
  : :   .-.,-.,-.: `'.' .--.  .-' :
  : :__ : :: ,. :: . `.' '_.'' .; :
  :___.':_;:_;:_;:_;:_;`.__.'`.__.'
                                  """)
print(bn)
def telegram_hxn(*a, **b):
	with PRNT:
		print(*a, **b)
def User_Agent():
	ios = [
		'13_5','13_6','14','13_3','14_4','15','12_6'
		'15_1','15_1_1','14_3','14_6','13_2','12_7']
	rv = [
		'604.1','596.2','706.6',
		'397.3','937.9','936.3']
	version = [
		'18.5.0','21.1.0',
		'19.3.0','19.1.0',
		'17.7.0','16.6.1']
	User_Agent = 'Mozilla/5.0 (iPhone; CPU iPhone OS '+choice(ios)+' like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/'+choice(version)+' Mobile/15E148 Safari/'+choice(rv)
	return User_Agent

class search_Numbers:
	def __init__(self):
		print(Fore.RED+"\n [/] Type like this [974 55555555] ")
		self.Number=input(Fore.CYAN+"\n [+] Enter Phone Number: ")
		self.Numbers=self.Number.split(' ')
		self.code = self.Number.split(' ')[0]
		try:self.phone = self.Number.split(' ')[1]
		except IndexError:exit(input('[-] You must type the country code, then a space, and then the phone number.. \nExample[ 974 52947429 ]'))
		self.Number_facebook()
	def Number_Info(self):
		if self.code == '20':country="EG:Egypt"
		elif self.code =='98':country="IR:Iran"
		elif self.code =='212':country="MA:Morocco"
		elif self.code =='213':country="DZ:Algeria"
		elif self.code =='216':country="TN:Tunisia"
		elif self.code =='249':country="SD:Sudan"
		elif self.code =='252':country="SO:Somalia"
		elif self.code =='961':country="LB:Libya"
		elif self.code =='962':country="JO:Jordan"
		elif self.code =='963':country="SY:Syria"
		elif self.code =='964':country="IQ:Iraq"
		elif self.code =="965":country="KW:Kuwait"
		elif self.code =='966':country="SA:Saudi Arabia"
		elif self.code =='967':country="YE:Yemen"
		elif self.code =='968':country="OM:Oman"
		elif self.code =='970':country="PS:Palestine"
		elif self.code =='971':country="AE:Emirates"	
		elif self.code =='972':country="ISR:Israel"
		elif self.code =='973':country="BH:Bahrain"
		elif self.code =='974':country="QA:Qatar"
		else:exit("[¿] The country code is not added for this number, it will be added soon")
		countr = country.split(':')[0]
		countr2= country.split(':')[1]
		send =get(f"http://caller-id.saedhamdan.com/index.php/UserManagement/search_number?number={self.phone}&country_code={countr}",headers={"User-Agent":"8Y/69"})
		try:
			name = send.json()['result'][0]['name']
			if name=='':name='nothing'
			nump = send.json()['result'][0]['number']
			pho=phonenumbers.parse('+'+self.Number)
			qtr = carrier.name_for_number(pho,'en')
			telegram_hxn(f'\n{grn}[+] phone : {nump}\n[+] country : {countr2}\n[+] ZIP code : {countr}\n[+] name : {name}\n[+] number type : {qtr} {wit}')
			Go_Back()
		except KeyError:
			telegram_hxn(yel+'[-] No leaked information found'+wit)
	def Number_Talabat(self):
		sent = post('https://api.talabat.com/api/v1/Account/ForgetPassword/8',headers={'Host': 'api.talabat.com','Content-Type': 'application/json','X-PX-AUTHORIZATION': '3:fb9556a0a8424d34117554cc0e9a3f92e45dba193d9dfcea3e4d54397a62d9b3:w1FY1NT4xhUFi5ilTK1vunJ6Svf6RVYj/56ZGRxTX6dG0/MPBBxqc2M2Am1Xj5wsFa8O2MI2IelPALRc+xKc9A==:1000:CF/0p7FhgwxQIiv6DKrQAXSMAAXWnOLAn6UHU+AQ2wF2nhGFSd8BFoHNpV745XG8SlRdyyNvYKLRZ1bjQsWStWXZERSihW/PDpgf/shTSWCs58re/hcBfL58ahk//g7dzq2Ai5uO0FUstSvxrN9gv04GSQ/IeqNZOs2l21pYzBu6TaOErlxZk3Ly58cJVwPUHW6+AJFMHCnXwziYXQnX9A==','Accept': '*/*','X-Device-Version': '8.7.8','X-Device-Source': '4','Accept-Language': 'ar-KW','BrandType': '1','AppBrand': '1','Accept-Encoding': 'gzip, deflate, br','X-PerseusSessionId': '1649634446063.1935786645.xejenkfhir','Content-Length': '76','X-Device-ID': '74180189-77F9-45AE-B384-71BF18BF110D','X-PerseusClientId': '1641917233047.9435967280.hrqaqruhlz','User-Agent': 'Talabat/1081 CFNetwork/1240.0.4 Darwin/20.5.0','Connection': 'keep-alive','X-NewRelic-ID': 'XQUPWFNbGwcBXVJRAgIGXg==','Cookie': 'AWSALB=eF0fwNXmW0uJ1J3kPZMR8nRB72BxHZbdpXvJ9PxysvhDr47vsq9nw5fcXmoN+vetHM3/jKL0PWfDw34vmH/KW1VSgvFottpEOFd0QUdIvCjxlf5ty5hp5VDzmGhB; AWSALBCORS=eF0fwNXmW0uJ1J3kPZMR8nRB72BxHZbdpXvJ9PxysvhDr47vsq9nw5fcXmoN+vetHM3/jKL0PWfDw34vmH/KW1VSgvFottpEOFd0QUdIvCjxlf5ty5hp5VDzmGhB; AWSALBTG=vmOEmccpqfD1FTGQ7OE3FoqU+ExjzW2mscQy1FLBSMbjtov/Ki752XRNLhMnjbB3IdwFl2ND4EJPtuoHgzNgaa1QA/2jQ+F8x+k/sEtxbopdh2i8kMo0J2q4QI1EqdRLxGJFfpF9iy70ch4aXZpqxUKyNepv0ZdPAfG66rMFjQlp12lmCrw=; AWSALBTGCORS=vmOEmccpqfD1FTGQ7OE3FoqU+ExjzW2mscQy1FLBSMbjtov/Ki752XRNLhMnjbB3IdwFl2ND4EJPtuoHgzNgaa1QA/2jQ+F8x+k/sEtxbopdh2i8kMo0J2q4QI1EqdRLxGJFfpF9iy70ch4aXZpqxUKyNepv0ZdPAfG66rMFjQlp12lmCrw=; __cf_bm=XSypDCSkDzPlJ6CNrHV5AsafVEyBE95uYzkmPdFU5kw-1649634471-0-AQmYgErYdOn7oRTQQHqsaNNXe9O7zPjbaugfBYsNd6ghTIBtjJkiqnEVNWEJ7g0OuOxJstN2DbmXVAf3GYDuS0beAlKUCD+CxAtU4jzLFLCo'},json={"Email":"","MobileNumber":self.phone,"mobileCountryCode":self.code}).text
		if ('"رقم الهاتف المتنقل غير صحيح"')in sent:telegram_hxn(red+'-[4] Not linked on Talabat.com ✖️')
		elif ('"عذرًا، لم نعثر على أي حساب مسجّل بهذا الرقم. لُطفًا حاول مرة أخرى أو أنشِئ حسابًا جديدًا."')in sent:telegram_hxn(red+'-[4] Not linked on Talabat.com ✖️')
		else:telegram_hxn(grn+'-[4] linked to an account Talabat.com ☑️')
		self.Number_Info()
	def Number_Twitter(self):
		sent=post('https://mobile.twitter.com/i/api/1.1/onboarding/task.json',headers={'Host': 'mobile.twitter.com','x-guest-token': '1513193250127069191','Accept': '*/*','Authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA','x-twitter-client-language': 'en','Accept-Language': 'en','Accept-Encoding': 'gzip, deflate, br','Content-Type': 'application/json','Origin': 'https://mobile.twitter.com','Content-Length': '193','User-Agent': User_Agent(),'Referer': 'https://mobile.twitter.com/i/flow/password_reset?input_flow_data=%7B%22requested_variant%22%3A%22eyJwbGF0Zm9ybSI6IlJ3ZWIifQ%3D%3D%22%7D','Connection': 'keep-alive','x-csrf-token': 'd45fd6d7c961ba75120edc7abd64653a','x-twitter-active-user': 'yes','Cookie': '_ga=GA1.2.2006589579.1649556997; _gid=GA1.2.251835287.1649556997; _twitter_sess=BAh7CSIKZmxhc2hJQzonQWN0aW9uQ29udHJvbGxlcjo6Rmxhc2g6OkZsYXNo%250ASGFzaHsABjoKQHVzZWR7ADoPY3JlYXRlZF9hdGwrCMgCUhSAAToMY3NyZl9p%250AZCIlZjAxMTIyZDNkOTI5YjI5MDU2YzllODgzNDM0YjBjNmQ6B2lkIiU1OWY1%250AMTUzYzQ2ZDgwMzQ5ZTkyZWFkOTU3OTRkODQ5MQ%253D%253D--6479ef2ca757d7ba01f3f4f55fe6872ab93c38a6; external_referer=padhuUp37zjgzgv1mFWxJ8aHbAM%2FyKh7|0|8e8t2xd8A2w%3D; att=1-K1BUUTxMtqfARyCfLZCEPItYHYsk5SC2Hkacl7Hc; gt=1513193250127069191; ct0=d45fd6d7c961ba75120edc7abd64653a; guest_id=v1%3A164955699388392009; guest_id_ads=v1%3A164955699388392009; guest_id_marketing=v1%3A164955699388392009; personalization_id="v1_0jRguk/LS28SwZ/S4gm+IA=="'},json={"flow_token":"g;164955699388392009:-1649608365402:7lGsO4nGSLM0ocNoeWidwbc2:1","subtask_inputs":[{"subtask_id":"PasswordResetBegin","enter_text":{"text":self.Number,"link":"next_link"}}]}).text
		if ('"Verify your identity by entering the username associated with your Twitter account."')in sent:TWR = grn+'-[3] linked to an account Twitter ☑️'
		elif ('You’ll need to wait before you can try again. We do this when we notice suspicious activity.') in sent:TWR = yel+'-[3] search error [Twitter.com]'
		elif ('"Sorry, we could not find your account."'):TWR = red+'-[3] Not linked on Twitter.com ✖️'
		else:print(sent)
		telegram_hxn(TWR)
		self.Number_Talabat()
	def Number_IG(self):
		Cookies = get('https://www.instagram.com/',headers={'User-Agent': User_Agent()}).cookies
		send=post('https://www.instagram.com/accounts/account_recovery_send_ajax/',headers={'Host': 'www.instagram.com','Accept': '*/*','X-ASBD-ID': '198387','X-Requested-With': 'XMLHttpRequest','X-IG-App-ID': '1217981644879628','X-Instagram-AJAX': 'cec4fe0d7efe','Accept-Language': 'ar','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://www.instagram.com','User-Agent': User_Agent(),'Referer': 'https://www.instagram.com/accounts/password/reset/','X-IG-WWW-Claim': '0','Content-Length': '95','Connection': 'keep-alive','Cookie': 'csrftoken='+Cookies['csrftoken']+'; ig_did='+Cookies['ig_did']+'; ig_nrcb='+Cookies['ig_nrcb']+'; mid='+Cookies['mid'],'X-CSRFToken': Cookies['csrftoken']},data='email_or_username='+self.Numbers[0]+self.Numbers[1]+'&recaptcha_challenge_field=&flow=&app_id=&source_account_id=').text
		if ('We sent an SMS') in send:IG=grn+'-[2] linked to an account instagram ☑️'
		elif ('We limit how often you can do certain things on Instagram to protect our community. Tell us if you think we made a mistake.')in send:IG=grn+'-[2] linked to an account instagram ☑️'
		elif ('We apologize, but we are currently unable to recover your account. Please try again in a day.')in send:IG=grn+'-[2] linked to an account instagram ☑️'
		elif ('Please wait a few minutes before you try again.')in send:IG = yel+'-[2] search error [instagram.com]'
		else:IG = red+'-[2] Not linked on instagram.com ✖️'
		telegram_hxn(IG)
		self.Number_Twitter()
	def Number_facebook(self):
		sent=post('https://m.facebook.com/login/identify/?ctx=recover&c=%2Flogin%2F%3Frefsrc%3Ddeprecated&search_attempts=1&ars=facebook_login&alternate_search=0&show_friend_search_filtered_list=0&birth_month_search=0&city_search=0',headers={'Host': 'm.facebook.com','Content-Type': 'application/x-www-form-urlencoded','Origin': 'https://m.facebook.com','Accept-Encoding': 'gzip, deflate, br','Cookie':'fr=0tgtKAhNPBEEEt0ml..BiUhtV.PJ.AAA.0.0.BiUhtf.AWUiorIUqk0; m_pixel_ratio=3; wd=375x812; datr=VRtSYtbrYMCWJoSLYww9m0t3; sb=VRtSYsE5HyPq5GEOMqujTOJm','Connection': 'keep-alive','Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8','User-Agent': User_Agent(),'Referer': 'https://m.facebook.com/login/identify/?ctx=recover&c=https%3A%2F%2Fm.facebook.com%2Flogin%2F%3Frefsrc%3Ddeprecated&multiple_results=0&ars=facebook_login&from_login_screen=0&lwv=100&_rdr','Content-Length': '81','Accept-Language': 'ar'},data='lsd=AVqp9U6EFAg&jazoest=2879&email='+self.Number+'&did_submit=%D8%A8%D8%AD%D8%AB').text
		if ('رقم الهاتف أو البريد الإلكتروني الذي أدخلته لا يطابق أي حساب. يرجى إعادة المحاولة') in sent:
			Fec = red+'-[1] Not linked on facebook.com ✖️'
		elif ('يمكننا إرسال رمز تسجيل دخول إليك') in sent:
			Fec = grn+'-[1] linked to an account facebook ☑️'
		elif ('إذا لم تكن قد سجّلت الدخول بالفعل')in sent:
			Fec = grn+'-[1] linked to an account facebook ☑️'
		elif ('جرّب إدخال كلمة السر') in sent:
			Fec = grn+'-[1] linked to an account facebook ☑️'
		else:
			Fec = red+'-[1] Not linked on facebook.com ✖️'
		telegram_hxn(Fec)
		self.Number_IG()
search_Numbers()
