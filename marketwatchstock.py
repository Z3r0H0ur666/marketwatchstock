import urllib
import re

symbolscode = open("symcode.txt").read()
symbolscode = symbolscode.split("\n")

for symbol in symbolscode:
	urlfile = urllib.urlopen("http://www.marketwatch.com/investing/stock/" +symbol)
	urltext = urlfile.read()
	regex = '<p class="data bgLast">(.+?)</p>'
	pattern = re.compile(regex)
	price = re.findall(pattern, urltext)
	print "the last price for ", symbol, "is", price
