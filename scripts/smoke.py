#!/usr/bin/env python3
import os,re,json,pathlib,hashlib,secrets,requests,urllib.parse
b=os.environ['BASE_URL'].rstrip('/');phase=os.environ['SMOKE_PHASE'];assert phase in ('boot','upgrade','redeploy');pw=os.environ['ADMIN_PASSWORD'];secure='https://'+urllib.parse.urlsplit(b).netloc
p=pathlib.Path(__file__).with_name('state-'+hashlib.sha256(b.encode()).hexdigest()[:16]+'.json')
home=requests.get(b+'/',timeout=40);assert home.status_code==200 and 'wger' in home.text.lower();asset=re.search(r'href="([^"]*/static/[^"]+\.css)"',home.text);assert asset
css=requests.get(urllib.parse.urljoin(b+'/',asset.group(1)),timeout=40);assert css.status_code==200 and 'text/css' in css.headers.get('content-type','')
def request(s,path,method='GET',**kwargs):
 cookies=s.cookies.get_dict();headers={'Referer':secure+path,'Cookie':'; '.join(k+'='+v for k,v in cookies.items())}
 if 'csrftoken' in cookies:headers['X-CSRFToken']=cookies['csrftoken']
 return s.request(method,b+path,headers=headers,timeout=40,allow_redirects=False,**kwargs)
def login(password):
 s=requests.Session();g=request(s,'/en/user/login');assert g.status_code==200;token=re.search(r'name="csrfmiddlewaretoken" value="([^"]+)"',g.text);assert token
 r=request(s,'/en/user/login','POST',data={'csrfmiddlewaretoken':token.group(1),'login':'admin','password':password,'next':'/'});return s,r
bad,r=login('wrong-'+pw);assert r.status_code==200,'invalid login unexpectedly redirected'
s,r=login(pw);assert r.status_code in (302,303),'valid login rejected';good=request(s,'/')
# Authenticated root redirects through locale/dashboard; replay secure cookies at each hop.
for _ in range(5):
 if good.status_code not in (301,302,303,307,308):break
 target=urllib.parse.urlsplit(urllib.parse.urljoin(b+'/',good.headers['Location']))
 assert target.netloc==urllib.parse.urlsplit(b).netloc,'cross-origin login redirect'
 good=request(s,target.path+('?' + target.query if target.query else ''))
assert good.status_code==200 and 'logout' in good.text.lower(),f'authenticated page status {good.status_code}'
anon=requests.Session();denied=request(anon,'/api/v2/routine/','POST',json={'name':'must-not-create'});assert denied.status_code in (401,403)
def api(path,data=None,expected=200):
 r=request(s,'/api/v2/'+path,'GET' if data is None else 'POST',json=data) if data is not None else request(s,'/api/v2/'+path)
 assert r.status_code==expected,f'{path} status {r.status_code}'
 return r.json()
if p.exists():state=json.loads(p.read_text())
else:
 assert phase=='boot','missing workout state; refusing to reseed'
 marker='railway-'+secrets.token_hex(8);routine=api('routine/',{'name':marker,'description':'Synthetic release validation','start':'2026-11-15','end':'2026-12-15','is_public':False},201)
 day=api('day/',{'routine':routine['id'],'order':1,'name':marker},201);state={'routine':routine['id'],'day':day['id'],'marker':marker};p.write_text(json.dumps(state));p.chmod(0o600)
routine=api('routine/'+str(state['routine'])+'/');day=api('day/'+str(state['day'])+'/');assert routine['name']==state['marker'];assert day['name']==state['marker'] and day['routine']==state['routine']
print(json.dumps({'ok':True,'phase':phase,'ui_css':True,'workout_routine_and_day_persisted':True,'negative_auth':True}))
