# Worldometer Covid Data Pipeline

### Goal Of Project

  Create architecture to perform ETL on Worldometer covid data.
  
### Obtaining The Data

  For this I will scrape the covid-19 Worldometer table that has worldwide data, afterwhich I will store said data in Google Cloud Storage
  and then add some statistical columns using PySpark and finally, I will store the processed data into Postgresql.
  
## Data Project Architecture

![](architecture/ArchitectureSchema.png)

