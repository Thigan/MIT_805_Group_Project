# NYC TLC HVFHV Big Data Project (MIT 805) - Part 2

Distributed processing of NYC Taxi & Limousine Commission High Volume For-Hire
Vehicle (HVFHV) trip records using PySpark and the MapReduce model
(Map, Shuffle, Reduce).

The analysis runs on a 4.82GB processing subset (14 monthly files,
245,504,968 trips, February 2019 - December 2024) and answers two questions:
when demand peaks during the week, and which pickup zones are busiest at peak
hours. It also tracks monthly trip volumes through the COVID-19 drop and recovery.

## Folder structure

- `notebooks/` - the Jupyter notebooks (build processing dataset, PySpark processing)
- `data/` - see `data/README.md` (the actual data is not stored in this repository)
- `figures/` - exported chart images from the PySpark notebook
- `output/` - dataset documentation
- `report/` - the written Part 2 report
- `requirements.txt` - Python packages needed to run the notebooks

## Setup

```
pip install -r requirements.txt
```

PySpark also needs Java (JDK 8, 11 or 17) installed. Google Colab already has it.

## How to reproduce this project

1. Get the working dataset (73 monthly Parquet files, 25.22GB). See `data/README.md`
   for how it is produced from the raw TLC data
2. Run `notebooks/Part2_Processing_Dataset.ipynb` to build the processing dataset.
   It copies 14 evenly spaced monthly files (target ~5GB) from the working dataset
   into a sample folder
3. Run `notebooks/MIT_805_Part2.ipynb` to run the PySpark analysis. Set
   `PROCESSING_DATA_FOLDER` to the sample folder from step 2. The notebook
   downloads the taxi zone lookup table automatically and generates the charts
   (hourly demand heatmap, peak-hour pickup zones, monthly trips) in `figures/`

## Data source

NYC Taxi & Limousine Commission - High Volume For-Hire Vehicle (HVFHV) trip
records. See `output/dataset_documentation.md` for full details on license,
size, format, collection period and how the processing subset was selected.
