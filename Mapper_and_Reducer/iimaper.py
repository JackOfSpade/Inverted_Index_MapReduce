#!/usr/bin/python
import sys


def map(key, value):
    # Split line by the comma delimiter
    value_list = value.strip().split(",")

    business_id = value_list[0]
    # Split categories by the semicolon delimiter
    categories = value_list[-1].strip().split(";")

    # Map to new key-value pairs
    for category in categories:
        key2 = category
        value2 = business_id

        # Emit
        print(key2 + "\t" + value2)


if __name__ == "__main__":
    for line in sys.stdin:
        # Ignore the header
        if line != "business_id,name,neighborhood,address,city,state,postal_code,latitude,longitude,stars,review_count,is_open,categories\n":
            map("yelp_business", line)
