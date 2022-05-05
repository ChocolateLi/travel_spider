# s = "2020.09.05"
# print(s)
# s1 = s.replace('.','-')
# print(s1)


# # s = "I love you"
# # print(s)
# # s.replace(' ','-')
# # print(s)

# print(type(str(len(s))))

import json
from Utils import Utils

utils = Utils()
place_json_name = "place.json"
place_json_path = "."
places_file = utils.find_file(place_json_name,place_json_path)
with open(places_file,'r') as file:
    places = json.load(file)

print(places)
print("********************")
print(type(places))
print("********************")
place_list = places['place_list']
print(place_list)
print("********************")
for place_info in place_list:
    region = place_info['region']
    place = place_info['place']
    place_url = place_info['place_url']
    place_url_page = place_info['place_url_page']
    print(region,place,place_url,place_url_page)