import re
import urllib.request
#https://in.finance.yahoo.com/quote/
url = 'https://in.finance.yahoo.com/quote/'
stock = input('Enter The Stock name ? ')
url = url + stock + '?p=' + stock
#print(url)
data = urllib.request.urlopen(url).read()
data1 = data.decode('utf-8')
'''file = open("/home/rahul/Desktop/test.txt",'w') 
file.write(data1)'''
m = re.search('"currentPrice":{"raw":',data1)
start = m.end()
end = start + 10
newString = data1[start:end]
m = re.search(',"',newString)
end = m.start()
newString1 = newString[0:end]
print('The Current Stock Value of '+ stock.upper() + ' is $' + newString1 + ' USD')