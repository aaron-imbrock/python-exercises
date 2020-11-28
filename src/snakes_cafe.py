import sys

menu = {
    "Appetizers": {
        "Wings": 0,
        "Cookies": 0,
        "Spring Rolls": 0
    },
    "Entrees": {
        "Salmon": 0,
        "Steak": 0,
        "Meat Tornado": 0,
        "A Literal Garden": 0,
    },
    "Desserts": {
        "Ice Cream": 0,
        "Cake": 0,
        "Pie": 0,
    },
    "Drinks": {
        "Coffee": 0,
        "Tea": 0,
        "Unicorn Tears": 0,
    },
}


def say(quote):

    query = "How are you?"
    print(f"Hello {quote}, {query} {1+4}")


say("Hello World!")

def main():
    pass
