## Introduction 

The aim of the project is to create an Streaming application with Spark that connects to a 
Kafka cluster, reads and process the data.
 
#answers


1. How did changing values on the SparkSession property parameters affect the throughput and latency of the data?

referring to the processedRowsPerSecond. The higher number we get on here, it means that we could process more rows in second.

2. What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal? 


spark.default.parallelism: total number of cores on all executor nodes.

spark.sql.shuffle.partitions: number of partitions to use when shuffling data for joins or aggregations.

spark.streaming.kafka.maxRatePerPartition: maximum rate at which data will be read from each Kafka partition


spark.sql.shuffle.partitions                15
spark.streaming.kafka.maxRatePerPartition   15
spark.default.parallelism                   15000


