import urllib2
url=raw_input("Give a url: ")
response = urllib2.urlopen(url)
page = response.read()
p=page.split("<p ")#not "<p"(ex. <pre>)
p2=page.split("<p>")
br=page.split("<br>")
href=page.split('href=')
cl=len(p)-1+len(p2)-1+len(br)-1
url=len(href)-1
print cl,url
