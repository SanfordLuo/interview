## 数据库

[Mysql](/docs/database.md#Mysql)  
[Redis](/docs/database.md#Redis)  
[ES](/docs/database.md#ES)

### Mysql

1. 存储引擎  
   InnoDB特点：  
   1.支持事务；2.支持外键约束；3.支持表、行级锁，行锁是实现在索引上的。命中索引则使用行锁，未命中索引则使用表锁；4.不保存表的具体行数。5.聚集索引，使用B+树作为索引结构，数据文件和索引是绑在一起的。节点包含主键id索引列，叶子节点包含索引列和数据。  
   MyISAM特点：  
   1.不支持事务；2.不支持外键；3.支持全文索引，查询速度快；4.保存表的具体行数。5.非聚集索引，使用B+树作为索引结构，索引和数据文件是分离的，索引保存的是数据文件的指针。索引的叶子节点是数据文件的地址指针。
2. 锁：隐式-根据隔离级别自动加锁(update,delete,insert)；显式-通过sql语句(select)。  
   共享锁：S lock，读锁，这时候只能读不能写，读取完成锁释放。读锁实现：select * from t_user where id = 3 lock in share mode;  
   排他锁：X lock，写锁，会阻塞其他的写锁和读锁。从颗粒度来分为表锁、行锁。  
   表锁：会锁定整张表并阻塞对该表的所有读写，比如alter修改表结构时。  
   行锁：分为乐观锁、悲观锁。  
   乐观锁：假设不会冲突，只在提交时校验。实现：先读出当前version，再修改：update t_user set nums=10,version=version+1 where id=3 and version=0;  
   悲观锁：每次拿数据的时候都对数据上锁，整个事务提交释放锁。悲观锁实现：select * from t_user where id = 3 for update;  
   死锁：悲观锁会引起。A事务持有X1锁，申请X2锁，B事务持有X2锁，申请X1锁，造成循环等待。死锁处理：发现死锁进行回滚释放。  
   死锁避免：a.合理设计索引，通过索引定位更少的行，减少锁竞争；b.大事务拆分小事务；c.不同的事务以固定顺序访问表和行；d.复杂sql拆分。
3. 隔离级别  
   事务：start transaction; set session transaction isolation level xx;  
   Read Uncommitted(读取未提交)：A事务会读到B事务修改但未提交的数据。脏读。  
   Read Committed(读取已提交)：A事务会出现两次查询数据不一致，因为期间B事务更新并提交了。不可重复读。  
   Repeatable Read(可重读)：A事务两次查询数据一致，即使期间B事务更新的已经提交了。幻读：A查询name为jay的未查到，B插入了jay并提交，A再查jay未查到，A插入jay报错，就是jay像幻觉一样存在。  
   Serializable(可序列化)：强制事务排序，每个读取数据行加上共享锁，A事务未提交时，B事务必须等待，可能会出现超时。
4. MVCC：多版本并发控制   
   通过生成记录的历史版本解决幻读问题，无锁实现读写并发操作。mvcc的实现主要是通过三个隐藏字段、undo log、readView实现的。  
   三个隐藏字段：隐藏主键、事务id、回滚指针。  
   undo log：是各个事务修改同一条记录的时候生成的历史记录，方便回滚，同时会生成一条版本链。  
   readView：是事务在进行快照读的时候生成的记录快照，用于判断事务的可见性。
5. 主从同步：默认异步的  
   master提交完事务后写入binlog，推送binlog到slave，slave开启一个IO线程读取后记录到relay log中继日志中，slave再开启一个sql线程读取relay
   log并执行，完成同步。slave也记录自己的binlog。  
   全同步复制：所有的slave都执行完同步后才返回客户端；半同步复制：slave至少有一个返回ack确认给master就认定写操作完成。
6. sql语句  
   查询所有出现过的name：select distinct name from t_user;  
   查询至少出现两次的name：select name, count(name) from t_user group by name having count(name) > 1;  
   插入时如果原数据已存在则进行修改：replace into t_user (user_id, name) values (333, 'jay');  
   左连接：可以返回左边的全部字段：select t_a.*, t_b.* from t_a left join t_b on t_a.user_id=t_b.user_id;  
   右连接：可以返回右边的全部字段：select t_a.*, t_b.* from t_a right join t_b on t_a.user_id=t_b.user_id;  
   全连接：返回左右两边的全部字段：select t_a.*, t_b.* from t_a full join t_b on t_a.user_id=t_b.user_id;  
   内连接：只返回两边共有的字段：select t_a.*, t_b.* from t_a join t_b on t_a.user_id=t_b.user_id;

### Redis

1. 数据类型  
   基本数据类型：string、list、hash、set、zset
2. 速度快  
   1.完全基于内存操作；2.用C语言实现，支持的数据类型是做了大量优化之后的；3.使用单线程，无上下文切换的成本；4.基于非阻塞的IO多路复用机制。
3. 版本6.0之后的多线程  
   单线程处理客户端请求，多线程来处理数据的读写和协议解析，执行命令还是单线程。多线程提升IO读写效率。
4. 热key  
   突然有几十万请求访问同一个key，达到物理网卡上限，导致redis服务器宕机，直接打到db导致db服务不可用。  
   解决方案：1.利用二级缓存，jvm缓存，提前加载到jvm内存中；2.备份热key，打散到不同的redis服务器，热key+机器编号=新key。
5. 缓存击穿、缓存穿透、缓存雪崩  
   缓存击穿：单个key并发量过高，key过期时所有请求打到db上。解决方案：1.加锁更新，如果缓存中没有，对key加锁，去db读出来写入redis。  
   缓存穿透：缓存中的key不存在，每次请求都打到db上。解决方案：1.加一层布隆过滤器，存入redis的时候，通过散列函数将它映射成数组中的点，并且值为1。查询时如果布隆过滤器的值为0则直接返回。  
   缓存雪崩：大规模的缓存过期失效，大量请求打到db导致系统崩溃。解决方案：1.不同的key设置不同的过期时间，避免同时过期；2.限流，避免同时刻大量请求打到db；3.二级缓存，同热key。
6. 过期策略  
   惰性删除：当用到key的时候才会判读是否过期，如果过期则删除。  
   定期删除：定期扫描检查随机取一些key，删除过期的key。  
   redis的内存淘汰机制：如果还没删除并且内存达到界限触发。如：过期key中移除最少使用的；移除将要过期的。
7. 高可用  
   主从同步：1.slave发送命令到master；2.master接收之后执行bgsave生成RDB全量文件；3.master把slave的写命令记录到缓存中；4.master的bgsave执行完后发送RDB文件到slave，slave执行；5.master发送缓存中的写命令到slave，slave执行。  
   缺点：没有自动故障转移机制，假设master宕机，就不能写入数据了，slave就失去了作用，除非手动进行切换。  
   哨兵模式：自动故障转移、集群监控、消息通知等功能。同时监视多个主从服务器，哨兵没隔1秒向所有主从ping，如果master未回复，如果投票过半则认为master下线，故障转移选举其中一个slave为master。  
   redis集群：分布式数据存储方案，支持高并发同时容纳海量数据。集群通过数据分片sharding来进行数据的共享，同时提供复制和故障转移。
8. 相关命令  
   写入并设置过期时间，如果k存在则覆盖：set k v EX seconds; set k v PX milliseconds;  
   只有k不存在时才进行设置，K存在时设置失败，不存在时获取锁成功，存在则获取锁失败：set k v NX; setnx k v;  
   只有K存在时才进行设置：set old_k new_v XX;  
   自增1，如果不存在则先初始化0再+1：incr k;  
   自减1，如果不存在则先初始化0再-1：decr k;
9. 数据持久化  
   为什么要持久化：redis的数据存放在内存中，持久化是指存入到磁盘中，如果没有持久化，redis重启会数据丢失。  
   RDB持久化：指定时间间隔内将内存中数据快照写入磁盘。fork子进程将数据集写入临时文件，替换之前的文件，用二进制压缩存储。  
   AOF持久化：以文本的形式append记录每一个非查询操作。  
   混合持久化：先把当前数据快照写入文件头，再将后续的操作追加存入。

### ES
