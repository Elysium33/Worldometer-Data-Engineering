import pandas as pd
import WOMscraper as woms
from WOMdataTransform import column_labels
from google.cloud import storage
from datetime import date, datetime


today = datetime.now()
yesterday = "%s-%d-%d" %(date.today().strftime('%b'), today.day-1, today.year)

df = pd.DataFrame(woms.web_scrape())

df = df.drop([15, 16, 17, 18, 19, 20], axis=1)
df.columns = column_labels

client = storage.Client()
bucket = client.get_bucket('coviddataproject')

bucket.blob('covid-'+yesterday.lower()+".csv").upload_from_string(df.to_csv(index=False), 'csv')

print("Check GCS bucket for result.")