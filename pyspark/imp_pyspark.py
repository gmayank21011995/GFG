# Top N Salaries per Department

from pyspark.sql.window import Window
from pyspark.sql.functions import row_number, col

windowSpec = Window.partitionBy("department").orderBy(col("salary").desc())
df.withColumn("rank", row_number().over(windowSpec)) \
  .filter(col("rank") <= 3).show()

# Fill missing salaries with department-level average.
from pyspark.sql.functions import avg

avg_salary = df.groupBy("department").agg(avg("salary").alias("avg_salary"))
df = df.join(avg_salary, on="department", how="left") \
       .withColumn("salary_filled", when(col("salary").isNull(), col("avg_salary")).otherwise(col("salary")))

# Extract fields from nested JSON.
df = spark.read.json("nested_data.json", multiLine=True)
df.select("user.name", "user.address.city", "user.address.zip").show()

# Find duplicate rows based on columns.
df.groupBy("id", "name").count().filter(col("count") > 1).show()

# Cumulative sales per department over time.
from pyspark.sql.functions import sum

windowSpec = Window.partitionBy("department").orderBy("date") \
    .rowsBetween(Window.unboundedPreceding, Window.currentRow)

df.withColumn("running_total", sum("sales").over(windowSpec)).show()

# Get latest login per user.
windowSpec = Window.partitionBy("user_id").orderBy(col("timestamp").desc())
df.withColumn("rn", row_number().over(windowSpec)).filter(col("rn") == 1).show()

# Convert nested array to flat rows.
from pyspark.sql.functions import explode

df.select("id", explode("hobbies").alias("hobby")).show()

# Count Nulls in Each Column
from pyspark.sql.functions import sum, col

from pyspark.sql.functions import col, count, when

# Count nulls in each column
null_counts = df.select(
    [count(when(col(c).isNull(), c)).alias(c) for c in df.columns]
)

null_counts.show()

# Get latest status per job from log data.
windowSpec = Window.partitionBy("job_id").orderBy(col("log_time").desc())
df.withColumn("rn", row_number().over(windowSpec)) \
  .filter(col("rn") == 1).select("job_id", "status").show()

# Get First & Last Event per User (first, last, Window functions)
from pyspark.sql.functions import first, last

windowSpec = Window.partitionBy("user_id").orderBy("timestamp")
df.withColumn("first_evt", first("event").over(windowSpec)) \
  .withColumn("last_evt", last("event").over(windowSpec)).show()

# Repartition for Efficient File Writing
df.repartition(10).write.parquet("output/")
df.coalesce(1).write.csv("single_file_output/", header=True)
