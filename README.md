# Parse Exchange mail for python

### 此repo為練習exchangelib+bs4

### 使用的模組
- Beautifulsoup4
- exchangelib


### Installation
```bash
pip install exchangelib
```

### 使用情境
假設信箱中有一封信進來，把需要的資料欄位進行格式化並存進資料庫，以供後續之處理與分析



### 資料格式
```python
personal_data={
        'name':'',
        'age':'',
        'gender':'',
        'Time':'',
        'ID':'',
        'creation_time':''
    }
```

### 設定config.py
```python
# define email account
username = ''
password = ''
primary_smtp_address = '' # example@xxx.con.tw
server = '' #mail.xxx.com.tw
```

### login exchange
```python

credentials = Credentials(username= username,  password=password)
version = Version(build=Build(15, 0, 12, 34))
config = Configuration(server=server, credentials=credentials,version = version, auth_type=NTLM)

self.account = Account(primary_smtp_address=primary_smtp_address,config=config, credentials=credentials, autodiscover=False,access_type=DELEGATE )

ews_url = self.account.protocol.service_endpoint
ews_auth_type = self.account.protocol.auth_type

config = Configuration(service_endpoint=ews_url, credentials=credentials, auth_type=ews_auth_type)
account = Account(
    primary_smtp_address=primary_smtp_address,
    config=config, autodiscover=False,
    access_type=DELEGATE,
)

```
