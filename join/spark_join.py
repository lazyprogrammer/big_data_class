# book url: https://www.amazon.com/dp/B01KH9YWSY
from pyspark import SparkContext
from pyspark.sql import SparkSession

sc = SparkContext("local", "My Simple App")
spark = SparkSession.builder.getOrCreate()

names = spark.read.json("/home/hduser/join/names.txt")
fruits = spark.read.json("/home/hduser/join/fruits.txt")

joined = names.join(fruits, names.user_id == fruits.user_id)
joined.show()

