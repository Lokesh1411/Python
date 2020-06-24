import COVID19Py
import csv
import pickle

#new obj for accessing
covid19=COVID19Py.COVID19()

#data source
covid19=COVID19Py.COVID19(data_source='jhu')

latest=covid19.getLatest()
locations=covid19.getLocations(timelines=True)
location=covid19.getLocations(rank_by='confirmed')
location1=covid19.getLocations(rank_by='recovered')
location2=covid19.getLocations(rank_by='deaths')
loc=covid19.getLocationByCountryCode('IN')

print (loc)

latest_changes=covid19.getLatestChanges()

'''
pickle_out=open('covid19_tracker.csv','wb')
pickle.dump(loc,pickle_out)
pickle_out.close()


w = csv.writer(open("covid19.csv", "wb"))
for key, val in loc:
    w.writerow(key, val)
w.close()
'''
