#!/usr/bin/env python
import requests
import mail
from collections import namedtuple
from datetime import datetime

now = datetime.now() # current date and time

WebsiteStatus = namedtuple('WebsiteStatus', ['status_code', 'reason'])
names = [
	'akcjademokracja', 
	'naszademokracja', 
	'prasa.akcjademokracja', 
	'portainer.akcjademokracja', 
	'rzeczy.akcjademokracja', 
	'wiruszyczliwosci', 
	'dzialaj.akcjademokracja']


def get_status(site):
    try:
        response = requests.head(site, timeout=5)
        status_code = response.status_code
        reason = response.reason
    except requests.exceptions.ConnectionError:
        status_code = '000'
        reason = 'ConnectionError'
    website_status = WebsiteStatus(status_code, reason)
    return website_status

date_time = now.strftime("%m/%d/%Y, %H:%M:%S")
print("date and time:",date_time)

for name in names:
    site = 'https://{}.pl'.format(name)
    website_status = get_status(site)
    print("{0:30} {1:10} {2:10}"
          .format(site, website_status.status_code, website_status.reason))
    status_check = int(website_status.status_code)
    if status_check == 0 or status_check >= 400:
        print("Error")
        mail.main(site, website_status.status_code, website_status.reason)

print("______\n")

