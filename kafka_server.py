import producer_server


def run_kafka_server():
    # get the json file path
    input_file = "police-department-calls-for-service.json"

    #  fill in blanks
    producer = producer_server.ProducerServer(
        input_file=input_file,
        topic="SF_Crime_Statistics",
        bootstrap_servers="localhost:9092",
        #         consumer_group="0",
        #         api_version=(0,10,1)
    )

    return producer


def feed():
    producer = run_kafka_server()
    producer.generate_data()


if __name__ == "__main__":
    feed()