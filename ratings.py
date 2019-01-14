"""Restaurant rating lister."""

# put your code here
def format_restaurant_ratings(textfile):

    textfile = open(textfile)
    restaurant_info_dict = {}

    for line in textfile:
        line = line.rstrip()
        name, rating = line.split(":")
        restaurant_info_dict[name] = rating

    sorted_restaurant_info = sorted(restaurant_info_dict)

    for item in sorted_restaurant_info:
        rating = restaurant_info_dict[item]
        print(f'{item} is rated at {rating}.')




format_restaurant_ratings("scores.txt")
