import pyspark
from pyspark.sql import SparkSession
import WOMdataTransform as dt
from datetime import date, datetime
import sqlalchemy

today = datetime.now()
yesterday = "%s-%d-%d" %(date.today().strftime('%b'), today.day-1, today.year)

path = "gs://coviddataproject/"+'covid-'+yesterday.lower()+ ".csv"

spark = SparkSession.builder.appName('CovidData').master('local[*]').getOrCreate()
engine = sqlalchemy.create_engine('postgresql+psycopg2://user:password@localhost:5432/db')

#You need a .jar file to be able to read gs:// paths
df = spark.read.csv(path, header=True, inferSchema=True)

df = dt.test_pos_rate(df)
df = dt.recov_rate(df)
df = dt.fatal_rate(df)
df = dt.death_rate(df)
df = dt.inc_case(df)
df = dt.inc_deaths(df)
df = dt.inc_recovered(df)

df = dt.remove_negative_values(df)

df = dt.add_date(df)

df.toPandas().to_sql(
    name = 'covid_data_'+yesterday.lower(),
    con = engine,
    index = False,
    if_exists = 'fail'
)

df.toPandas().to_sql(
    name = 'covid_all_data',
    con = engine,
    index = False,
    if_exists = 'append'
)




