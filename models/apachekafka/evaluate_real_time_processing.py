from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import time

# Initialize Spark context
sc = SparkContext(appName="EvaluateRealTimeProcessing")
ssc = StreamingContext(sc, 10)  # Batch interval of 10 seconds

# Connect to Kafka
kafka_stream = KafkaUtils.createDirectStream(ssc, ['user_interactions'], {'metadata.broker.list': 'localhost:9092'})

# Measure latency and throughput
start_time = time.time()
message_count = [0]

def process_data(record):
    message_count[0] += 1

kafka_stream.foreachRDD(lambda rdd: rdd.foreach(process_data))

ssc.start()

# Run for a certain duration to measure
time.sleep(60)  # Run for 60 seconds

ssc.stop(stopSparkContext=True, stopGraceFully=True)

end_time = time.time()
total_time = end_time - start_time
total_messages = message_count[0]
throughput = total_messages / total_time
latency = total_time / total_messages

print(f"Total Messages: {total_messages}")
print(f"Total Time: {total_time} seconds")
print(f"Throughput: {throughput} messages/second")
print(f"Latency: {latency} seconds/message")
