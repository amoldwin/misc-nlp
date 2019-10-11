import urllib2

for n in range(1,80):
        url = 'http://www.chakoteya.net/StarTrek/' + str(n) + '.htm'
        filedata = urllib2.urlopen(url)
        dtatatowrite = filedata.read()
        path = str(n) + '.txt'
        print(path)
        with open(path,'wb') as f:
                f.write(dtatatowrite)