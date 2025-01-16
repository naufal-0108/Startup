import os
import numpy as np, pandas as pd
from pyspark.sql import SparkSession
from datasets import load_dataset


spark = SparkSession.builder.getOrCreate()

if __name__ == "__main__":
    df = pd.read_csv(r"C:\Users\naufal\Startup\datasets\corporate_stress_dataset.csv", sep=",")
    df.head()