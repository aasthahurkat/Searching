from math import cos, asin, sqrt
def distance(lat1, lon1, lat2, lon2):
    p = 0.017453292519943295     #Pi/180
    a = 0.5 - cos((lat2 - lat1) * p)/2 + cos(lat1 * p) * cos(lat2 * p) * (1 - cos((lon2 - lon1) * p)) / 2
    return 12742 * asin(sqrt(a)) #2*R*asin...

f = open('C:\\Users\\HP\\Desktop\\bagrawal-aahurkat-rrokde-a1-master\\part2\\city-gps.txt', 'r')
data = str(f.readlines())
line = data.find('Aberdeen,_Ohio')
end = data.find(' ',line,len(data))
x = data.find(' ',end+1,len(data))
lat2 = float((data[end+1:x]))
y = data.find(' ',x+1, len(data))
lon2 = float((data[x+1:y-4]))

with open('C:\\Users\\HP\\Desktop\\bagrawal-aahurkat-rrokde-a1-master\\part2\\city-gps.txt','r') as file:
    for line in file:
        city_name = str.split(line)[0]
        latitude = str.split(line)[1]
        longitude = str.split(line)[2]
        lat1 = float(latitude)
        lon1 = float(longitude)
        heuristic_distance = distance(lat1,lon1,lat2,lon2)
        print("distance for", city_name, "is", heuristic_distance)
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
