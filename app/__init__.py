import traceback
import time
import urllib3
import time,os,stat
import re
import datetime
import traceback
from bs4 import BeautifulSoup
import urllib3
import requests
from io import BytesIO

#這行保留, 才沒有報ssl錯誤
from exchangelib import DELEGATE, Account, Credentials,Configuration, NTLM,Build, Version
urllib3.disable_warnings(urllib3.exceptions.SecurityWarning)
from exchangelib.protocol import BaseProtocol, NoVerifyHTTPAdapter

#忽略憑證檢查
from requests.auth import HTTPBasicAuth
BaseProtocol.HTTP_ADAPTER_CLS = NoVerifyHTTPAdapter

#import module
from app.config import *


