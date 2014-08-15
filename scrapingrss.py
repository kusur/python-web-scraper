#!/usr/bin/python -tt

import urllib2
from urllib2 import urlopen
import re
import cookielib
from cookielib import CookieJar
import time
import sys
import time

cj = CookieJar()
opener = urllib2.build_opener(urllib2.HTTPCookieProcessor(cj))
opener.addheaders = [('User-agent','Mozilla/5.0')]


def topmenu_hyperlinks(url):

  page = opener.open(url).read()
  top_menu = re.findall(r'<div id="ucMenu_TopMenu".*</div>',page)
  
  for top_str in top_menu:
    links = re.findall(r"<a href='[/\w*]*' target='_self'>[\s\w]*</a>",top_str)
  for link in links:
    temp = re.search(r"<a href='[/\w*]*'",link).group()
    if temp[0:len("<a href='")] == "<a href='" and temp[-1] == "'":
      temp = temp[len("<a href='"):-1]      
    caption = re.search(r'>[\s\w]*<',link).group().strip('<>')
    temp = "http://www.somaiya.edu"+temp
    print caption +"-->"+temp

def submenu_hyperlinks(url):

  page = opener.open(url).read()
  sub_menu = re.findall(r'<div id="ucMenu_SubMenu".*</div>',page)
      
  for sub_str in sub_menu:
    links = re.findall(r"<a href='[/\w*]*' target='_self'>[\s\w]*</a>",sub_str)
  for link in links:
    temp = re.search(r"<a href='[/\w*]*'",link).group()
    if temp[0:len("<a href='")] == "<a href='" and temp[-1] == "'":
      temp = temp[len("<a href='"):-1]      
    caption = re.search(r'>[\s\w]*<',link).group().strip('<>')
    temp = "http://www.somaiya.edu"+temp
    print caption +"-->"+temp
  
def imageParser(url):
  
  page = opener.open(url).read()
  images = re.findall(r'<img.*src=".*[.]jpg"',page)
  for image in images:
    image = "http://www.somaiya.edu"+image[len("<img src=\""):-1]
    print image

def calendarOfEvents(url):
  
  page = opener.open(url).read()
  notifications = re.findall(r'<div class=\"calendarMainDive">\s*<div .*>\s*\d\d\s*<span>.*</span>\s*</div>\s*<div class="calendartextDive">\s*<span .*>[/\w*]*</span>\s*[\w\s*]*',page)
  for notification in notifications:
    temp1 = re.search(r'<div class="calendarMainDive">\s*<div .*>\s*',notification).group()
    temp1 = notification[len(temp1):]
    temp2 = re.search(r'</span>\s*</div>\s*<div .*>\s*<span .*>[/\w*]*</span>\s*[\w\s*]*',temp1).group()
    date = re.search(r'\d\d',temp1[:len(temp2)]).group()
    month = re.search(r'<span>\w\w\w',temp1[:len(temp2)]).group()
    year = re.search(r'\d\d\d\d',temp1[:len(temp2)]).group()
    Date = date+'-'+month[len('<span>'):]+'-'+year
    desc_url = re.search(r'calendarRedirectUrl">[/\w*]*</span>',notification).group()[len('calendarRedirectUrl">'):-len('<span>')-1]
    desc_temp = re.search(r'calendarRedirectUrl">[/\w*]*</span>\s*[\w\s]*',notification).group()
    desc_temp_first_part = re.search(r'calendarRedirectUrl">[/\w*]*</span>\s*',desc_temp).group()
    desc = desc_temp[len(desc_temp_first_part):].strip(' \t\n\r')
    print Date
    print "http://www.somaiya.edu"+desc_url
    print desc
    print '------------------'
    

if __name__ == '__main__':    
  #hyperlinks(sys.argv[1])
  #parsePage()
  #imageParser(sys.argv[1])
  calendarOfEvents(sys.argv[1])
