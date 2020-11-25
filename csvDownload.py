import requests

# req = requests.get(
#     'https://www1.ncdc.noaa.gov/pub/data/cdo/samples/PRECIP_HLY_sample_csv.csv')

req = requests.get(
    'https://drive.google.com/file/d/1JgYIO74CHf-k9VAzoclc2t100lLaasAJ/view?usp=drivesdk')

url_content = req.content
csv_file = open('D://Sem 4//downloaded.csv', 'wb')
print(csv_file)
csv_file.write(url_content)
csv_file.close()
