# parquet_to_csv_converter
This program uses the multiprocessing library in python to parallelize converting parquet files to csv


### REQUIREMENTS
- You have to have python version 3.11.4 or above
- You have to have pip3 version 23.2.1 or above installed. pip is a python package manager for python
- You need the pandas library for python
```
pip3 install pandas
```

#### Running the program
```
python3 parquet_to_csv_converter.py <source directory> <output directory>
```

For example:
```
python3 parquet_to_csv_converter.py . output
```

This will look for parquet files in the "." which is the current directory of where the program is being run from, and \
export the csv files to the directory called output. 