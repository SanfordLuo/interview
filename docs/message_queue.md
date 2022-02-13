### 消息队列
   [Kafka](/docs/message_queue.md#Kafka)
   [RabbitMq](/docs/message_queue.md#RabbitMq)
   [Celery](/docs/message_queue.md#Celery)  
   作用：消息通讯，异步处理，应用解耦，流量削峰

###### Kafka
1. Kafka特点  
   可靠性：分布式的、可区分的、数据可备份的、高度容错的  
   可扩展性：在无需停机的情况下可实现轻松扩展  
   消息持久性：可持久化到本地磁盘  
   高性能：吞吐量很高，百万级吞吐量。顺序写、零拷贝  
2. 架构及工作流程  
   Producer生产者将消息发送到Kafka集群，再由消费者进行消费，提交偏移量。  
   Kafka集群的一台机器Broker，Broker里包含多个topic，topic可指定多个分区Partition，  
   Kafka的Topic中的分区Partition是leader与follower的主从机制，生产者产生的消息push到实际存在分区，与leader进行交互，follower进行备份。  
   消费者同样与leader进行交互，pull消息进行消费。消费者组中的消费者不能同时消费topic中的同一分区，如果为了保持消息的顺序性一般一个topic指定一个分区就行。  
   Zookeeper存储broker信息: 包含各个broker的服务器信息、Topic信息.  
   Zookeeper存储消费者信息: 主要存储每个消费者消费的topic的offset的值。  
   offset偏移量：记录队列中当前读取消息的位置。如果未提交偏移量latest从最新产生的开始消费所以会丢失数据，earliest从上次提交偏移量开始消费。  
3. 注意事项  
   缓冲池满了：kafka的缓冲池会出现满了的情况，因此需要回收。最大值log.retention.bytes，过期时间(log.retention.hours)。  
             对于超过最大值的按照partitions下的segment为单位进行删除，对于过期时间的则根据时间策略删除。  
   数据传输的事务：最多一次：消费者先提交偏移量再处理事务；最少一次：先处理事务再提交偏移量。  
   消息丢失：生产者push消息的时候broker挂了；消费者已经提交偏移量但是处理消息的时候异常了；leader所在的broker挂掉时消息还未完全备份到follower。  
4. 示例
   [生产者](tool_demos/script/kafka_producer.py)
   [消费者](tool_demos/script/kafka_consumer.py)

###### RabbitMq

###### Celery
