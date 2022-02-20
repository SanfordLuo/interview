### 数据库

&emsp;[Mysql](/docs/database.md#Mysql)  
&emsp;[Redis](/docs/database.md#Redis)  
&emsp;[ES](/docs/database.md#ES)

###### Mysql

1. 存储引擎  
   &emsp;InnoDB特点：  
   &emsp;&emsp;1.支持事务；2.支持外键约束；3.支持表、行级锁，行锁是实现在索引上的。命中索引则使用行锁，未命中索引则使用表锁；4.不保存表的具体行数。5.聚集索引，使用B+树作为索引结构，数据文件和索引是绑在一起的。节点包含主键id索引列，叶子节点包含索引列和数据。  
   &emsp;MyISAM特点：  
   &emsp;&emsp;1.不支持事务；2.不支持外键；3.支持全文索引，查询速度快；4.保存表的具体行数。5.非聚集索引，使用B+树作为索引结构，索引和数据文件是分离的，索引保存的是数据文件的指针。索引的叶子节点是数据文件的地址指针。  
2. 锁：隐式-根据隔离级别自动加锁(update,delete,insert)；显式-通过sql语句(select)。  
   &emsp;共享锁：S lock，读锁，这时候只能读不能写，读取完成锁释放。读锁实现：select * from t_user where id = 3 lock in share mode;  
   &emsp;排他锁：X lock，写锁，会阻塞其他的写锁和读锁。从颗粒度来分为表锁、行锁。  
   &emsp;&emsp;表锁：会锁定整张表并阻塞对该表的所有读写，比如alter修改表结构时。  
   &emsp;&emsp;行锁：分为乐观锁、悲观锁。  
   &emsp;&emsp;&emsp;乐观锁：假设不会冲突，只在提交时校验。实现：先读出当前version，再修改：update t_user set nums=10,version=version+1 where id=3 and version=0;  
   &emsp;&emsp;&emsp;悲观锁：每次拿数据的时候都对数据上锁，整个事务提交释放锁。悲观锁实现：select * from t_user where id = 3 for update;  
   &emsp;死锁：悲观锁会引起。A事务持有X1锁，申请X2锁，B事务持有X2锁，申请X1锁，造成循环等待。死锁处理：发现死锁进行回滚释放。  
   &emsp;死锁避免：a.合理设计索引，通过索引定位更少的行，减少锁竞争；b.大事务拆分小事务；c.不同的事务以固定顺序访问表和行；d.复杂sql拆分。  
3. 隔离级别  
   &emsp;事务：start transaction; set session transaction isolation level xx;  
   &emsp;Read Uncommitted(读取未提交)：A事务会读到B事务修改但未提交的数据。脏读。  
   &emsp;Read Committed(读取已提交)：A事务会出现两次查询数据不一致，因为期间B事务更新并提交了。不可重复读。  
   &emsp;Repeatable Read(可重读)：A事务两次查询数据一致，即使期间B事务更新的已经提交了。幻读：A查询name为jay的未查到，B插入了jay并提交，A再查jay未查到，A插入jay报错，就是jay像幻觉一样存在。  
   &emsp;Serializable(可序列化)：强制事务排序，每个读取数据行加上共享锁，A事务未提交时，B事务必须等待，可能会出现超时。  
4. MVCC：多版本并发控制   
   &emsp;通过生成记录的历史版本解决幻读问题，无锁实现读写并发操作。mvcc的实现主要是通过三个隐藏字段、undo log、readView实现的。  
   &emsp;&emsp;三个隐藏字段：隐藏主键、事务id、回滚指针。  
   &emsp;&emsp;undo log：是各个事务修改同一条记录的时候生成的历史记录，方便回滚，同时会生成一条版本链。  
   &emsp;&emsp;readView：是事务在进行快照读的时候生成的记录快照，用于判断事务的可见性。  
5. 主从同步：默认异步的  
   &emsp;主库提交完事务后写入binlog，推送binlog到从库，从库开启一个IO线程读取后记录到relay log中继日志中，从库再开启一个sql线程读取relay log并执行，完成同步。从库也记录自己的binlog。  
   &emsp;全同步复制：所有的从库都执行完同步后才返回客户端；半同步复制：从库至少有一个返回ack确认给主库就认定写操作完成。  
6. sql语句  
   &emsp;查询所有出现过的name：select distinct name from t_user;  
   &emsp;查询至少出现两次的name：select name, count(name) from t_user group by name having count(name) > 1;  
   &emsp;插入时如果原数据已存在则进行修改：replace into t_user (user_id, name) values (333, 'jay');  
   &emsp;左连接：可以返回左边的全部字段：select t_a.*, t_b.* from t_a left join t_b on t_a.user_id=t_b.user_id;  
   &emsp;右连接：可以返回右边的全部字段：select t_a.*, t_b.* from t_a right join t_b on t_a.user_id=t_b.user_id;  
   &emsp;全连接：返回左右两边的全部字段：select t_a.*, t_b.* from t_a full join t_b on t_a.user_id=t_b.user_id;  
   &emsp;内连接：只返回两边共有的字段：select t_a.*, t_b.* from t_a join t_b on t_a.user_id=t_b.user_id;  

###### Redis

###### ES
