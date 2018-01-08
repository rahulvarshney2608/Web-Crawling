import re
import urllib.request
#http://www.dictionary.com/browse/
while True:
  url = 'http://www.dictionary.com/browse/'
  word = input('Give Word whose meaning is fo find: ')
  url = url + word
  data = urllib.request.urlopen(url).read()
  data1  = data.decode('utf-8')
  m = re.search('meta name="description" content="',data1)
  start = m.end()
  end = start + 300
  String = data1[start:end]
  m = re.search(' See more.',String)
  end = m.start()
  newString = String[0:end]
  print(newString)
  m = input('Do you Want to Search For another Word [Y/N] :')
	if m == 'n' or m == 'N':
		break
