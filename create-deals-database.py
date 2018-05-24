
import json

import numpy as np
import pandas as pd


stores = ["Target", "Home Depot", "Walmart", "Amazon", "eBay", "CVS" ,"Kohl's" , "American Eagle", "Lowe's", "Nike"]
charities = ["American Red Cross", "Doctors Without Borders", "The Nature Conservancy", "World Wildlife Fund", "UNICEF", "Save the Children", "Bill & Melinda Gates Foundation" , "Salvation Army", "Feeding America", "Habitat for Humanity"]
deals = [10,10,15,20,25,10,30,15,20, 25]

if __name__ == "__main__":
    ALL_DEALS  = {};
    for x in range (0,10):
        deal = {};
        deal["charityID"] = charities[x]
        deal["percent_off"] = deals[x]
        ALL_DEALS[stores[x]] = deal

    js = json.dumps(ALL_DEALS)
    with open("deals.json", "w+") as outfile:
          outfile.write(js)