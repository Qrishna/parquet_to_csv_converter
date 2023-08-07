import pandas as pd
import glob
import multiprocessing
import sys
import os


def convert_parquet_to_csv(filename):
    target_directory = sys.argv[2]
    df = pd.read_parquet(filename)
    df.to_csv(target_directory + "/" + filename.split("/")[-1] + ".csv")


def main():
    path = None
    if len(sys.argv) != 3:
        print("USAGE: python3 parquet_to_csv_converter.py <source directory> <output directory>")
        return
    elif len(sys.argv) == 3:
        path = sys.argv[1]

    files = glob.glob(path + "/*.parquet")
    if files:
        os.makedirs(sys.argv[2], exist_ok=True)
        print("list of parquet files found in path: ", files)
        num_cores = multiprocessing.cpu_count()

        with multiprocessing.Pool(num_cores) as pool:
            pool.map(convert_parquet_to_csv, files)
    else:
        print("No parquet files found in the provided path ", path)
        print("USAGE: python3 parquet_to_csv_converter.py <source directory> <output directory>")


if __name__ == "__main__":
    main()
