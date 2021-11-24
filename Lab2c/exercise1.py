#
# read the data from the URL and write to homepage.html
#
import urllib.request
# open a connection to a URL using urllib
webUrl  = urllib.request.urlopen('https://google.com')



print ("result code: " + str(webUrl.getcode()))

data = webUrl.read()

f = open("homepage.html", "w")
f.write(str(data))
f.close()

#Find UP address of that website
""""
import socket 

ip = socket.gethostbyname('www.google.com')
print(ip)
"""