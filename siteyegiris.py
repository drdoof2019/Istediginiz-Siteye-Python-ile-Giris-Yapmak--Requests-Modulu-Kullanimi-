import requests
from bs4 import BeautifulSoup as BS 


user_data = {
'name': 'drdoof58',
'pass': 'Yakinda.Degistirilecek58',
'form_id': 'new_login_form',
'op': 'Login'
}
headers = {
    'user-agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.120 Mobile Safari/537.36'
}
with requests.Session() as ses:
    url = 'https://www.codechef.com/'
    r = ses.get(url,headers=headers)
    soup = BS(r.content,'html5lib')
    user_data['csrfToken'] = soup.find('input', attrs={'name':'csrfToken'})['value']
    user_data['form_build_id'] = soup.find('input', attrs={'name':'form_build_id'})['value']
    giris_yap = ses.post(url,headers=headers,data=user_data)
    print(giris_yap.content)
    