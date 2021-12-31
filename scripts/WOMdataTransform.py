import pyspark
from pyspark.sql import dataframe
from pyspark.sql.functions import *

column_labels = ["Country", 'Total Cases', 'New Cases', 'Total Deaths', 'New Deaths',
                'Total Recovered', 'New Recovered', 'Active Cases', 'Serious Critical',
                'Tot Cases/1M pop', 'Deaths/1M pop', 'Total Tests', 'Tests/1M pop', 'Population', 'Continent']

def test_pos_rate(dataframe):
	return dataframe.withColumn('Test Positivity Rate', round(dataframe['New Cases'] / dataframe['Total Cases'] * 100, 2))

def recov_rate(dataframe):
	return dataframe.withColumn('Recovery Rate', round(100 * dataframe['Total Recovered'] / (dataframe['Total Deaths'] + dataframe['Total Cases']), 2))

def fatal_rate(dataframe):
	return dataframe.withColumn('Fatality Rate', round(dataframe['Total Deaths'] / dataframe['Total Cases'] * 100, 2))

def inc_deaths(dataframe):
	return dataframe.withColumn('Inc Deaths', round(dataframe['New Deaths'] / dataframe['Total Cases']*100, 2))

def inc_case(dataframe):
	return dataframe.withColumn('Inc Cases', round(dataframe['New Cases'] / dataframe['Total Cases']*100, 2))

def inc_recovered(dataframe):
	return dataframe.withColumn('Inc Recovered', round(dataframe['New Recovered'] / dataframe['Total Recovered']*100, 2))

def death_rate(dataframe):
	return dataframe.withColumn('Daily Death Rate', round(dataframe['New Deaths'] / dataframe['New Cases']*100, 2))

def add_date(dataframe):
	return dataframe.withColumn('Date', date_sub(current_date(), 1))

def remove_negative_values(dataframe):
    cols = dataframe.columns
    for i in range(len(cols)):
        dataframe = dataframe.withColumn(cols[i], when(col(cols[i]) < 0, 0).otherwise(col(cols[i])))
    return dataframe
