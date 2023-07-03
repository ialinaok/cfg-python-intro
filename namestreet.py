place = {
    'name': 'The Anchor',
    'post_code': 'E14 6HY',
    'street_number' : '54',
    'location' : {
        'longitude' : 127,
        'latitude' : 63,
    }
}

place[2] = "The Crown"

print(place["name"])
print(place['post_code'])
print(place["street_number"])
print(place['location']['latitude'])