import simplejson,csv

writer=csv.writer(open('myfriends.csv','wb+'),quoting=csv.QUOTE_ALL)

fn='friends.txt'

data = simplejson.load(open(fn,'r'))
id=0
for d in data['rows']:
        id=id+1
        #'interests' is the column name containing the Likes data
        interests=simplejson.loads(d['Likes'])
        for i in interests['data']:
           if i['category'] == 'Interest':
              print str(id),i['name'],i['category']
              writer.writerow([str(id),i['name'].encode('ascii','ignore')])
