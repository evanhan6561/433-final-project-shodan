#!/usr/bin/env python
import shodan
import json

SHODAN_API_KEY = "YOUR_API_KEY"
api = shodan.Shodan(SHODAN_API_KEY)

try:
    # Search Shodan w/o spending all our credits. One banner costs .01 credits I believe
    limit = 300
    counter = 0
    banners = []
    for banner in api.search_cursor('org:"Bjc Health System"'):
        banners.append(banner)

        counter += 1
        if counter >= limit:
            print("!!!!! LIMIT REACHED, TERMINATING")
            break

    # Dump results to a JSON file
    with open('bjc-all-ips.json', 'w') as f:
        print("WRITING ", len(banners), " Banners")
        json.dump(banners, f)
    


except shodan.APIError as e:
    print('Error: {}'.format(e))
