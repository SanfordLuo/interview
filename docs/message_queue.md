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
   [生产者](https://github.com/SanfordLuo/tool_demos/blob/master/script/kafka_producer.py)
   [消费者](https://github.com/SanfordLuo/tool_demos/blob/master/script/kafka_consumer.py)

###### RabbitMq
1. 架构及工作流程  
   遵循的协议：AMQP协议，高级消息队列协议，进程间传递异步消息的一个网络协议。  
   工作流程：生产者(Publisher) ---> 交换机(Exchange) ---> 队列(Queue) ---> 消费者(Consumer)  
   Broker: 代理，由Exchange和Queue组成。连接生产者消费者，实现AMPQ协议中消息队列和路由功能的进程。  
   Virtual Host: 虚拟主机，一个虚拟主机里可以有多个Exchange和Queue，用于权限控制。  
   Exchange: 交换机，接收生产者发送的消息，并且根据routing_key把消息路由到指定的Queue中去。  
   Queue: 消息队列，存储待消费的消息。由headers和body组成，headers包含生产者添加的消息的各种属性参数，body是真正发送的数据内容。    
   Binding: 通过routing_key将Exchange与Queue绑定。routing_key不能使任意的字符串，一般用"."分割开，  
            例如 "register.shanghai", "register.beijing", "register.#"正则时 *(星号)代表任意一个单词; #(hash)代表0个或者多个单词。  
   Channel: 信道，消费者与Broker通信的渠道，建立在TCP连接上的虚拟连接。一个TCP连接上可以建立好多信道，减少系统开销提高性能。  
2. 工作模式  
   简单模式: 最简单的一对一。  
   工作队列模式: 一对多。一个生产者对应多个消费者，但每条消息只能被其中的一个消费者消费。  
      轮询分发: 将消息轮流发给每个消费者，一个消费者处理完才会发送下一个。例: A消费第1,4,7...条消息，B消费第2,5,8...条消息，C消费第3,6,9...条消息。  
      公平分发: 只要有空闲的消费者就给发待处理的消息，相对于轮询分发提高效率。
   发布/订阅模式: 一个生产者产生的消息，可以同时被多个消费者消费。生产者将消息发送给broker，由Exchange将消息转发到绑定在此交换机的每一个Queue中，消费者监听自己的Queue进行消费。
   路由模式: 生产者将消息发送给broker，由Exchange根据routing_key分发到不同的Queue中，消费者也根据routing_key找到对应的Queue进行消费。  
   主题模式: 在路由模式的基础上，routing_key支持正则匹配。  
   RPC模式: 通过消息队列实现RPC功能，客户端发送消息到消费队列，服务端消费消息执行程序将结果再返回给客户端，就是把结果发送消息到回调队列。
3. 汇总  
   简单模式，工作队列模式为一类: 不需要声明交换机就可以用，更不需要指定交换机类型。  
      实际上是由消息代理事先声明好的空字符串的直连交换机。新建的队列都会自动绑定到此交换机，routing_key与队列名相等。  
   发布/订阅模式，路由模式，主题模式都需要声明交换机，并且指定交换机类型。  
   发布订阅模式是往交换机上绑定的每一个queue都发消息，路由模式则是根据路由键发到指定的queue中。  

###### Celery
