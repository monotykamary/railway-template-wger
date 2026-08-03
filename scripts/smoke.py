#!/usr/bin/env python3
import os,re,requests
b=os.environ['BASE_URL'].rstrip('/');pw=os.environ['ADMIN_PASSWORD'];home=requests.get(b+'/',timeout=30);assert home.status_code==200 and 'wger' in home.text.lower();asset=re.search(r'href="([^"]*/static/[^"]+\.css)"',home.text);assert asset;css=requests.get(requests.compat.urljoin(b,asset.group(1)),timeout=30);assert css.status_code==200 and 'text/css' in css.headers.get('content-type','')
def submit(password):
 s=requests.Session();g=s.get(b+'/en/user/login',timeout=30);token=re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"',g.text);assert token
 r=s.post(b+'/en/user/login',data={'csrfmiddlewaretoken':token.group(1),'login':'admin','password':password,'next':'/'},headers={'Referer':g.url},allow_redirects=True,timeout=30);return s,r
_,bad=submit('wrong-password');assert '/login' in bad.url
s,good=submit(pw);assert good.status_code==200 and '/login' not in good.url and 'logout' in good.text.lower()
print('wger smoke checks passed')
