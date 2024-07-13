from kafka import KafkaProducer

# Initialize Kafka producer
producer = KafkaProducer(bootstrap_servers='localhost:9092')

# Sample data to send
sample_data = [
    {"user": "user_1", "action": "click", "timestamp": "2024-07-11T12:34:56"},
    {"user": "user_2", "action": "like", "timestamp": "2024-07-11T12:35:56"},
    {"user": "user_3", "action": "search", "timestamp": "2024-07-11T12:36:56"},
]

# Send sample data to Kafka topic 'user_interactions'
for data in sample_data:
    producer.send('user_interactions', value=str(data).encode('utf-8'))

producer.flush()
