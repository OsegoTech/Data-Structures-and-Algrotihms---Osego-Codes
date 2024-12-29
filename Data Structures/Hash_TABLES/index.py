book = dict()

book["apple"] = 0.67
book["milk"] = 1.49
book["avocado"] = 1.49
print(book)

# ask for the price of avocado
print(book["avocado"])

# hash tables are very fast
# looking up the price of an item is O(1) time complexity
# adding an item to the hash table is also O(1) time complexity
# deleting an item from the hash table is also O(1) time complexity
# searching for an item in the hash table is also O(1) time complexity
# hash tables are used for caching, memoization, and indexing data
# hash tables are used in databases, caches, and sets and lookup tables
"""
use in DNS, routers, and network switches
"""

# lets build a phone book using a hash table
phone_book = dict()
phone_book["jenny"] = 8675309
phone_book["emergency"] = 911
print(phone_book["jenny"])

voted = {}
value = voted.get("tom")
print(value)

def check_voter(name):
    if voted.get(name):
        print("kick them out!")
    else:
        voted[name] = True
        print("let them vote!")

check_voter("tom")
check_voter("mike")
check_voter("mike")