from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

# Initialize Spark context
sc = SparkContext(appName="RealTimeProcessing")
ssc = StreamingContext(sc, 10)  # Batch interval of 10 seconds

# Connect to Kafka
kafka_stream = KafkaUtils.createDirectStream(ssc, ['user_interactions'], {'metadata.broker.list': 'localhost:9092'})

# Process data
def process_data(record):
    data = json.loads(record[1])
    user = data['user']
    action = data['action']
    timestamp = data['timestamp']
    return (user, (action, timestamp))

# Apply transformation
processed_data = kafka_stream.map(process_data)

# Print processed data
processed_data.pprint()

# Save processed data to HDFS (optional)
processed_data.saveAsTextFiles("hdfs://path/to/save/processed_data")

ssc.start()
ssc.awaitTermination()
