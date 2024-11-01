# -*- coding: utf-8 -*-
"""example.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1gyDa6K254j5TTkR0Jc-g32CU-kpJmBB2
"""

from pyspark.sql import SparkSession
from pyspark.sql.types import *

def readdata(spark):
  # Create a dataframe manually, from a list
  df = spark.createDataFrame([(1,'Nguyen'),(2,'Dinh'),(3,'Vinh')])
  print(type(df))
  df.show()
  df.printSchema()


if __name__ == "__main__":
  spark = SparkSession.builder.appName("Simple with Session").getOrCreate()
  readdata(spark)

  spark.stop()