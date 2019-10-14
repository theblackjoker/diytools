# -*- coding: utf-8 -*-
# @Author : 90sec.com
# @Tools  : Pycharm
print("""
+++++++++++++++++++++++++++++++++++++++++++
______ _           _   _____ _____ _      +
|  ___(_)         | | /  ___/  ___| |     +
| |_   _ _ __   __| | \ `--.\ `--.| |     +
|  _| | | '_ \ / _` |  `--. \`--. | |     +
| |   | | | | | (_| | /\__/ /\__/ | |____ +
\_|   |_|_| |_|\__,_| \____/\____/\_____/ +
                                          +
+++++++++++++++++++++++++++++++++++++++++++                                       
""")

import requests
import re
import sys
import os

TIME_OUT = 60
def get_SSL(domain):
    domains = []
    url = 'https://crt.sh/?q=%25.{}'.format(domain)
    response = requests.get(url,timeout = TIME_OUT)
    ssl = re.findall("<TD>(.*?).{}</TD>".format(domain),response.text)
    for i in ssl:
         i += '.' + domain
         domains.append(i+'\n')
    fileurl = open('url.txt','w')
    for i in domains:
        fileurl.write(i)
        fileurl.write('\n')
    fileurl.close()
    file = os.path.exists('url.txt')
    filesize = os.path.getsize('url.txt')
    if file and (filesize > 0):
        print("Ok!")
    else:
        print("false")
if __name__ == '__main__':
    result = sys.argv[1]
    get_SSL(result)