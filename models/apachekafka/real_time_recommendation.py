from pyspark import SparkContext
from pyspark.streaming import StreamingContext
from pyspark.streaming.kafka import KafkaUtils
import json

# Initialize Spark context
sc = SparkContext(appName="RealTimeRecommendation")
ssc = StreamingContext(sc, 10)  # Batch interval of 10 seconds

# Connect to Kafka
kafka_stream = KafkaUtils.createDirectStream(ssc, ['user_interactions'], {'metadata.broker.list': 'localhost:9092'})

# Process data
def process_data(record):
    data = json.loads(record[1])
    user = data['user']
    action = data['action']
    timestamp = data['timestamp']
    # Example recommendation logic
    recommendation = "recommended_item_based_on_" + action
    return (user, recommendation)

# Apply transformation
recommendations = kafka_stream.map(process_data)

# Print recommendations
recommendations.pprint()

ssc.start()
ssc.awaitTermination()
