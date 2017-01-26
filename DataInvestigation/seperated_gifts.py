import os

script_dir = os.path.dirname(__file__)
gifts_csv_location = os.path.join(script_dir, "../giftsdata.csv")
gifts = open(gifts_csv_location, 'r')
gifts = gifts.read()
gifts = gifts.split('\n')
