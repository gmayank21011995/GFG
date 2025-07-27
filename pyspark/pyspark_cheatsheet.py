from pyspark.sql import SparkSession

spark = SparkSession.builder.appName("test").getOrCreate()

data = {
    "name":["mayank", "neeraj"],
    "age":[18, 20]
}
df = spark.createDataFrame(data)

# From list of tuples
data = [("Alice", 30), ("Bob", 25)]
df = spark.createDataFrame(data, ["name", "age"])

# From RDD
rdd = spark.sparkContext.parallelize(data)
df = rdd.toDF(["name", "age"])

# CSV
df = spark.read.csv("file.csv", header=True, inferSchema=True)
df.write.csv("output.csv", header=True)

# Parquet
df = spark.read.parquet("file.parquet")
df.write.parquet("output.parquet")

# JSON
df = spark.read.json("file.json")

# basic operation
df.printSchema()
df.show()
df.describe().show()
df.columns
df.dtypes
df.count()

# select and filter
df.select("name", "age").show()
df.filter(df.age > 25).show()
df.where("age < 30").show()

# with col and rename
from pyspark.sql.functions import col, lit

df = df.withColumn("new_col", col("age") + 10)
df = df.withColumnRenamed("age", "years")

# group by aggregations
from pyspark.sql.functions import avg, count, max

df.groupBy("department").agg(
    count("*").alias("count"),
    avg("salary").alias("avg_salary")
).show()

# window functions
from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, rank, dense_rank

windowSpec = Window.partitionBy("dept").orderBy("salary")

df.withColumn("row_num", row_number().over(windowSpec)).show()
df.withColumn("rank", rank().over(windowSpec)).show()
df.withColumn("dense_rank", dense_rank().over(windowSpec)).show()

# joins
df1.join(df2, df1.id == df2.id, "inner")
df1.join(df2, "id", "left_outer")
df1.join(df2, "id", "right_outer")
df1.join(df2, "id", "full_outer")

# UDF
from pyspark.sql.functions import udf
from pyspark.sql.types import StringType

def mask_email(email):
    return email[0] + "***@" + email.split("@")[-1]

mask_udf = udf(mask_email, StringType())

df.withColumn("masked_email", mask_udf(col("email"))).show()

# handling nulls
df.fillna({"salary": 0})
df.dropna(subset=["name", "age"])
df.na.replace("N/A", None)

# explode and flatten
from pyspark.sql.functions import explode

df = df.withColumn("exploded_col", explode("nested_array"))

# pivoting 
df.groupBy("name").pivot("month").sum("sales").show()

# broadcast join
from pyspark.sql.functions import broadcast

df1.join(broadcast(df2), "id").show()

# performance optimization
# Cache
df.cache()
df.persist()

# Repartition / Coalesce
df.repartition(10)
df.coalesce(1)

# Explain Plan
df.explain()

# write df
df.write.partitionBy("year", "month").parquet("output/")

# schema manipulation
df.schema
df.printSchema()

# Change column datatype
df = df.withColumn("age", col("age").cast("int"))

# read nested json
df = spark.read.json("nested.json", multiLine=True)
df.select("name", "address.city").show()

# date & timestamp
from pyspark.sql.functions import to_date, current_timestamp

df = df.withColumn("date_col", to_date(col("timestamp_col")))
df = df.withColumn("current_ts", current_timestamp())

# delta lake
# Reading & Writing
df.write.format("delta").save("/delta/events")
df = spark.read.format("delta").load("/delta/events")

# Time Travel
spark.read.format("delta").option("timestampAsOf", "2025-06-01").load("/delta/events")
