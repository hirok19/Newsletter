#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 22 16:34:08 2019

@author: supaul
"""

#
import requests
url = ('https://newsapi.org/v2/top-headlines?'
       'country=in&'
       'apiKey='+config.SECRETKEY)
response = requests.get(url)
jsonObject=response.json()
msg = ("Hello this is your news update !"+"\n")
print(jsonObject)
listOfArticles=jsonObject["articles"]
for article in listOfArticles[:10]:
    print(article["title"])
    print(article["urlToImage"])
    msg+=article["title"]+"\n";
    msg+=("Link to this story:"+article["url"]+"\n");
    print("Link to this story:",article["url"])
    print()
    

'''
goodReadResponse = requests.get('http://quotes.rest/qod.json')
quoteJson=goodReadResponse.json()
quoteContent=quoteJson['contents']
qt=quoteContent['quotes']
finalQuote=qt[0]
print(finalQuote['quote'])
print(finalQuote['author'])

print(msg)
msg+=(finalQuote['quote']+"-"+finalQuote['author'])
'''

import smtplib

import config


def send_email(subject, msg,senderemail):
    try:
        server = smtplib.SMTP('smtp.gmail.com:587')
        server.ehlo()
        server.starttls()
        server.login(config.USERNAME,config.PASSWORD)
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail(config.USERNAME,senderemail,message)
        server.quit()
        print("Success: Email sent!")
    except:
        print("Email not sent")
   

subject = "News letter of the day"

for email in config.EMAILLIST:
    send_email(subject, msg,email)
