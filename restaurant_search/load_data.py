import os
import csv
import json
import django
from django.conf import settings

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'restaurant_search.settings')
django.setup()

from search_app.models import Restaurant

def run(file_path):
    try:
        with open(file_path, 'r') as file:
            reader = csv.DictReader(file)
            print(reader)
            for row in reader:
                try:
                    items = json.loads(row['items'].replace("'", '"'))
                    restaurant = Restaurant(
                        id=row['id'],
                        name=row['name'],
                        location=row['location'],
                        items=items
                    )
                    restaurant.save()
                    print(f"Saved restaurant: {restaurant.name}")
                except Exception as e:
                    print(f"Error saving restaurant {row['name']}: {e}")
    except Exception as e:
        print(f"Error reading file: {e}")

if __name__ == "__main__":
    csv_file_path = '/home/mahesh/Desktop/restaurants_small .csv' 
    run(csv_file_path)

