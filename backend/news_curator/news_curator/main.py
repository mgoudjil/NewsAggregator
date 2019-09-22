from scrapers import *
from os.path import dirname, basename, isfile, join, abspath, dirname
import glob

# Run each Scrapper & get results

# 1. Initialize SQL connection

# 2. WHILE TRUE

# 3. Start time & for loop scrapers


def main():

    # Connect to databases

    # Creates table if doesn't exist

    # Get all scraper in scrapers folder
    modules_path = glob.glob(join(dirname(abspath(__file__)) + "/scrapers", "*.py"))
    scrapers = [
        basename(f)[:-3]
        for f in modules_path
        if isfile(f) and not f.endswith("__init__.py")
    ]

    for scraper in scrapers:
        result = getattr(eval(scraper), "main")()
        print(result)
        # Add Result to database
        # And calculate score

    # Redis Instance 2 (Click, vote, share, )
    # FOR loop
    # REDIS GETSET to 0
    # Add to mariadb & update to "recalculate needed: TRUE"

    # For Each Reculated Needed
    # Get article values
    # Calculate NEW SCORE
    # Add to mariadb & update to "recalculate needed: FALSE"

    #
    # Sum Votes of an Articles
    # C
    # Sum SQLITE VOTES & deletes
    # Add Votes to mariadb & changed statut to "need calculation"
    # Get


if __name__ == "__main__":
    main()

# print("Hello")


# json = {
#     'youtube.com':{
#         '/..',
#         '/...'
#     }
# }

# * While

# for (i,j) in json


# from 'scraper/youtube.py' import

# functions = [function_one, function_two, function_three, ...]

# n = int(input('Number: '))


# while 1

# // start time

# for i in range(n):

#     result = functions[i]()
#     // Do something
#     // Add to sqlite

# Post work
# add to SQL DATABASE

# // End-Time

# // Pause

