# Dataset Documentation — Part 2

Domain: Transport
Dataset: NYC Taxi & Limousine Commission — High Volume For-Hire Vehicle (HVFHV) trip records

---

## 1. License and Academic Use

This dataset is published by the New York City Taxi & Limousine Commission (TLC) under NYC's Open Data Law. NYC Open Data's own FAQ puts it plainly:

> "Open Data belongs to all New Yorkers. There are no restrictions on the use of Open Data."

The TLC page does carry a standard disclaimer — "TLC makes no representations as to the accuracy of these data"

The taxi zone lookup table used in Part 2 to name pickup zones comes from the same TLC page and falls under the same terms.

The dataset is fine to use academically.

---

## 2. Dataset Details

| Field | Detail |
|---|---|
| **Source** | NYC TLC's official trip record page (nyc.gov/site/tlc), also mirrored on the AWS Open Data Registry |
| **Dataset** | High Volume For-Hire Vehicle (HVFHV) trip records, trips from Uber, Lyft, Via, and Juno. |
| **Format** | Apache Parquet, one file per month |
| **Collection period** | February 2019 – May 2025 (73 monthly files). This isn't TLC's full history. |
| **Publication / updates** | HVFHV reporting started Feb 2019. TLC keeps publishing new months on a 2 month lag, so their live data goes well past May 2025 |
| **Raw dataset size** | 30.21 GB across 73 files |
| **Working dataset size** | 25.22 GB across 73 files, 1,283,180,517 rows. Built by trimming each raw file down to 11 columns and dropping rows with missing or impossible values |
| **Processing dataset size** | ~5 GB across 14 monthly Parquet files, 245,504,968 rows and 11 columns. This is the data PySpark actually reads and transforms in Part 2, read directly from disk and never converted to Pandas for the main analysis |
| **Processing subset selection** | 14 evenly spaced months drawn from the 73 working files: 2019-02, 2019-07, 2019-12, 2020-05, 2020-10, 2021-04, 2021-09, 2022-02, 2022-10, 2023-03, 2023-09, 2024-02, 2024-07, 2024-12. This keeps the full Feb 2019 – Dec 2024 span, including the COVID-19 drop and recovery, while staying manageable on Google Colab |
| **Subset justification** | Above the ≥3 GB processing minimum, and almost 4× larger than the 5% Pandas sample used in Part 1 (64,159,022 rows), so it demonstrates distributed processing rather than single machine analysis |
| **Columns (11)** | hvfhs_license_num, pickup_datetime, dropoff_datetime, PULocationID, DOLocationID, trip_miles, trip_time, base_passenger_fare, tips, driver_pay, shared_request_flag |
| **Data quality check** | Null count run across all 11 columns in PySpark: 0 missing values in every column, confirming the Part 1 cleaning carried through |
| **Additional input** | TLC taxi zone lookup table (taxi_zone_lookup.csv), joined to PULocationID to give each pickup zone a name and borough |
| **Processing engine** | PySpark DataFrame API on Google Colab (Map, Shuffle and Reduce handled by Spark's Catalyst optimiser and DAG execution) |

---

## Sources

- [TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- [NYC TLC Trip Records — AWS Open Data Registry](https://registry.opendata.aws/nyc-tlc-trip-records-pds/)
- [TLC Taxi Zone Lookup Table (CSV)](https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv)
- [NYC Open Data FAQ](https://opendata.cityofnewyork.us/faq/)
- [NYC Open Data Law overview](https://opendata.cityofnewyork.us/open-data-law/)
