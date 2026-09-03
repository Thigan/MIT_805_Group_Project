# NYC TLC HVFHV Big Data Project (MIT 805)

Analysis of NYC Taxi & Limousine Commission High Volume For-Hire Vehicle
(HVFHV) trip records, February 2019 - May 2025.

## Folder structure

- `notebooks/` - the Jupyter notebooks (build working dataset, EDA)
- `src/` - the raw data download script
- `data/` - see `data/README.md` (the actual data is not stored in this repository)
- `figures/` - exported chart images from the EDA notebook
- `output/` - dataset documentation
- `report/` - the written Part 1 report / write-up

## How to reproduce this project

1. Run `src/nyc_tlc_downloader_local.py` to download the raw HVFHV data
2. Run `notebooks/build_working_dataset.ipynb` to build the cleaned working dataset
3. Run `notebooks/eda_notebook.ipynb` to reproduce the exploratory data analysis
   and generate the chart images in `figures/`

## Data source

NYC Taxi & Limousine Commission - High Volume For-Hire Vehicle (HVFHV) trip
records. See `output/dataset_documentation.md` for full details on license,
size, format, and collection period.
