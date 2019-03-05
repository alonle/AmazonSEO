# Amazon Product Researcher
# Input: Product Keyword
# Output: PDF file with first page product info and what could be improved to rank

from amazon.api import AmazonAPI
from key import *

keywords='cell phone charger'

amazon = AmazonAPI(newKey1,newKey2,'beyourshelves-20') # Inits API

# Gets first page results for top amazon products
products = amazon.search_n(10,Keywords=keywords, SearchIndex='All')

for i in products:
    print(i)