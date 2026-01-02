from api import fetch_countries
from transform import parse_countries
from repository import save_countries
from tabulate import tabulate

countries = fetch_countries()
rows = parse_countries(countries)
headers = ['name','capital','region','population']
print(tabulate(rows,headers,tablefmt='grid'))
save_countries(rows)
print(f"🌎 Total países insertados: {len(rows)}")