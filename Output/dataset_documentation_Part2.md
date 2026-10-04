# Data

The raw, working and processing datasets are not stored in this repository
because of their size (raw: ~30GB across 73 files, working: ~25GB, processing: ~4.8GB
across 14 files).

- **Raw data**: downloaded by running `src/nyc_tlc_downloader_local.py`
- **Working data**: produced by running `notebooks/build_working_dataset.ipynb`
  on the raw data
- **Processing data** (Part 2): produced by running
  `notebooks/Part2_Processing_Dataset.ipynb` on the working data. It sorts the
  73 working files by date and copies 14 evenly spaced ones (target ~5GB) into
  a sample folder: 2019-02, 2019-07, 2019-12, 2020-05, 2020-10, 2021-04,
  2021-09, 2022-02, 2022-10, 2023-03, 2023-09, 2024-02, 2024-07, 2024-12
  (4.82GB, 245,504,968 rows). Point `PROCESSING_DATA_FOLDER` in
  `notebooks/MIT_805_Part2.ipynb` at that folder. PySpark reads it directly
- **Taxi zone lookup** (Part 2): downloaded automatically by
  `notebooks/MIT_805_Part2.ipynb` from
  https://d37ci6vzurychx.cloudfront.net/misc/taxi_zone_lookup.csv
