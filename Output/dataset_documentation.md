# Dataset Documentation

Domain: Transport
Dataset: NYC Taxi & Limousine Commission — High Volume For-Hire Vehicle (HVFHV) trip records

---

## 1. License and Academic Use

This dataset is published by the New York City Taxi & Limousine Commission (TLC) under NYC's Open Data Law. NYC Open Data's own FAQ puts it plainly:

> "Open Data belongs to all New Yorkers. There are no restrictions on the use of Open Data."

The TLC page does carry a standard disclaimer — "TLC makes no representations as to the accuracy of these data"

The dataset is fine to use academically.

---

## 2. Dataset Details

| Field | Detail |
|---|---|
| **Source** | NYC TLC's official trip record page (nyc.gov/site/tlc), also mirrored on the AWS Open Data Registry |
| **Dataset** | High Volume For-Hire Vehicle (HVFHV) trip records, trips from Uber, Lyft, Via, and Juno. |
| **Format** | Apache Parquet, one file per month |
| **Collection period** | February 2019 – May 2025 (73 monthly files). This isn't TLC's full history.|
| **Publication / updates** | HVFHV reporting started Feb 2019. TLC keeps publishing new months on a 2 month lag, so their live data goes well past May 2025 |
| **Raw dataset size** | 30.21 GB across 73 files |
| **Working dataset size** | 25.22 GB across 73 files, 1,283,180,517 rows. Built by trimming each raw file down to 11 columns and dropping rows with missing or impossible values |
| **Processing dataset size** | Not finalized yet. This will be whatever the PySpark pipeline in Part 2 actually reads and transforms (target ≥3GB) |

---

## Sources

- [TLC Trip Record Data](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- [NYC TLC Trip Records — AWS Open Data Registry](https://registry.opendata.aws/nyc-tlc-trip-records-pds/)
- [NYC Open Data FAQ](https://opendata.cityofnewyork.us/faq/)
- [NYC Open Data Law overview](https://opendata.cityofnewyork.us/open-data-law/)
