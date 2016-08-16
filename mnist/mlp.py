# book url: https://www.amazon.com/dp/B01KH9YWSY
from pyspark import SparkContext
from pyspark.sql import SparkSession

from pyspark.ml.classification import MultilayerPerceptronClassifier
from pyspark.ml.evaluation import MulticlassClassificationEvaluator

sc = SparkContext("local", "My Simple App")
spark = SparkSession.builder.getOrCreate()


data = spark.read.format("libsvm").load("/home/macuser/mnist.scale")


# Split the data into train and test
splits = data.randomSplit([0.6, 0.4], 1234)
train, test = splits

trainer = MultilayerPerceptronClassifier(maxIter=30, layers=[780, 100, 10], blockSize=128, seed=1234)
model = trainer.fit(train)


# compute accuracy on the test set
result = model.transform(test)
predictionAndLabels = result.select("prediction", "label")
evaluator = MulticlassClassificationEvaluator(metricName="accuracy")
print("Accuracy: " + str(evaluator.evaluate(predictionAndLabels)))
