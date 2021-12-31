# Worldometer Covid Data Pipeline

### Goal Of Project

  Create architecture to perform ETL on worldometer covid data.
  
### Obtaining The Data

  For this I will scrape the covid-19 worldometer table that has worldwide data, afterwhich I will store said data in Google Cloud Storage
  and then add some statistical columns using PySpark and finally, I will store the processed dataa into postgresql.
  
## Data Project Architecture

![](architecture/ArchitectureSchema.png)

