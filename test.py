import requests

r = requests.get(f"https://tcgcsv.com/tcgplayer/3/groups")
all_groups = r.json()['results']

for group in all_groups:
    print(f"Name: {group['name']} --- Abbreviation: {group['abbreviation']} --- Release Date: {group['publishedOn']} --- Group ID: {group['groupId']}")

    products = requests.get(f"https://tcgcsv.com/tcgplayer/3/{group['groupId']}/products")
    all_products = products.json()['results']

    # for product in all_products:
    #     print(product)