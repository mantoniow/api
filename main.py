import requests

#DINAMIC API KEY
api_key = '94819417d51fd6992a86fc711cc58f5f'
base_url = 'http://api.countrylayer.com/v2'

#FUNCTION TO MAKE A GET REQUEST TO THE API
def get_country(endpoint):
    url = f'{base_url}/{endpoint}?access_key={api_key}'
    response = requests.get(url)
    return response.json()

# FUNCTION TO MAKE A POST REQUEST TO THE API
def create_country(endpoint, data):
    url = f'{base_url}/{endpoint}?access_key={api_key}'
    response = requests.post(url, json=data)
    return response.json()

# FECTH DATA COUNTRIES
'''
all_countries = get_country('all')
print('All countries:', all_countries)
'''
#GET DATA FOR SPECIFIC COUNTRIES (US, DE, GB)
countries = ['US', 'DE', 'GB']
for country_code in countries:
    country_data = get_country(f'alpha/{country_code}')
    if 'name' in country_data:
        print(f'Country {country_code}:', country_data)
    else:
        print(f'Country {country_code} not found.')

#TRY TO GET DATA FOR NON-EXISTENT COUNTRIES
nonexistent_countries = ['XX', 'ZZZ']
for country_code in nonexistent_countries:
    country_data = get_country(f'alpha/{country_code}')
    if 'name' in country_data:
        print(f'Country {country_code}:', country_data)
    else:
        print(f'Country {country_code} not found.')

#EXAMPLE POST REQUEST (TEST TO VALIDATE NEW COUNTRY ADITION)
new_country_data = {
    'name': 'Wakanda',
    'alpha2_code': 'WF',
    'alpha3_code': 'WFE'
}

response = create_country('all', new_country_data)
print('POST response:', response)