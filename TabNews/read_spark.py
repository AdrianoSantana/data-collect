# %%
from pyspark.sql import SparkSession

spark = (SparkSession.builder
        .appName('PythonSpark SQL')
        .config('spark.some.config', 'some-value')
        .getOrCreate())


# %%
path_data = '/mnt/datalake/TabNews/contents/json'
df = spark.read.json(path_data)
df.show()