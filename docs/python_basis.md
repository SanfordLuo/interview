## python 基础

1. [垃圾回收](/docs/python_basis.md#垃圾回收)  
   [深浅拷贝](/docs/python_basis.md#深浅拷贝)  
   [闭包-装饰器](/docs/python_basis.md#闭包-装饰器)  
   [迭代器-生成器](/docs/python_basis.md#迭代器-生成器)  
   [静态方法-类方法-实例方法](/docs/python_basis.md#静态方法-类方法-实例方法)  
   [GIL-进程-线程-协程](/docs/python_basis.md#GIL-进程-线程-协程)  
   [设计模式](/docs/python_basis.md#设计模式)  
   [linux相关](/docs/python_basis.md#linux相关)

### 垃圾回收

引用计数为主，标记-清除和隔代回收为辅

1. 引用计数：每个对象维护一个计数字段，引用计数为0则回收。  
   新的引用指向该对象时 +1，如：对象被创建，对象被引用，对象当作参数传入函数中，对象作为一个元素存储在容器中。  
   对象的引用失效时 -1，如：对象的别名被显式销毁，对象的别名被赋予新的对象，离开它的作用域，所在容器被销毁或者从容器中删除对象。  
   优点：简单；实时性，一旦没有引用内存直接释放。  
   缺点：维护引用计数消耗资源；会出现循环引用导致内存泄漏。
2. 标记-清除：解决引用计数带来的循环引用的问题。  
   标记阶段：遍历所有的对象，如果还有对象引用它，则标记为可达。  
   清除阶段：再次遍历所有对象，如果没有标记为可达，则回收。
3. 分代回收：由于上述引用计数+标记清除比较耗时，分代回收以空间换时间来提高垃圾回收效率.(gc模块)。  
   内存分为3代，第0代，第1代，第2代，对应三个链表，扫描频率逐渐降低。当扫描其中其中一代时，比它年轻的代也都会被扫描。  
   新创建的对象被分配在第0代，首先进行扫描第0代，回收该回收的，不该回收的放到第1代。  
   依此类推第2代放的是最不容易被回收的，并且第2代扫描频率最低。

### 深浅拷贝

其实只针对可变类型才有作用

1. 对象的属性：存储地址(id)，类型(type)，变量名(对象地址的引用)，值。
2. 存储地址(id)。  
   不可变类型：数值，字符串，布尔，id和值不变。  
   eg：a = 'python', b = 'python', id(a) == id(b)  
   可变类型：字典，列表，集合。值可变但是id不可变。  
   eg: a = [1], a.append(2), 前后id是同一个；  
   b = [3], c = [3], id(b) != id(c)；  
   d = [4], e = d, id(d) == id(e)
3. 浅拷贝：只拷贝数据的最外层，不会拷贝子元素对象。  
   不可变类型：浅拷贝的对象和原对象id相同。  
   eg：a = 'python', b = copy.copy(a), id(a) == id(b)  
   可变类型：无论嵌套与否，本身的浅拷贝对象和原对象id不同，但里面子元素对象的id是相同的。  
   eg：a = [1,[2, 3]], b = copy.copy(a), id(a) != id(b), id(a[0]) == id(b[0]), id(a[1]) == id(b[1]), id(a[1][0]) == id(
   b[1][0])
4. 深拷贝：拷贝所有的可变数据类型，包含嵌套的子元素对象。  
   不可变类型：与浅拷贝一样，深拷贝的对象和原对象id相同。  
   eg：a = 'python', b = copy.deepcopy(a), id(a) == id(b)  
   可变类型：所有层级的子可变类型对象都会拷贝，子不可变类型对象不拷贝。  
   eg: a = [1, [2, 3]], b = copy.deepcopy(a), id(a) != id(b), id(a[0]) == id(b[0]), id(a[1]) != id(b[1]), id(a[1][0]) ==
   id(b[1][0])

### 闭包 装饰器

闭包

1. 定义：指在方法内引用方法外定义的非全局变量。内部方法使用外部方法中定义的非全局变量。  
   eg: [bi_bao_outer](/script/bibao_decorator.py)
2. 自由变量：如果一个变量在代码块中使用，但是没在代码快中定义，既未在本地作用域绑定的变量。
3. 修改变量值：如果变量值是可变的，如list，可直接进行append；如果变量值是不可变的，如int自增，需要nonlocal声明。(python2没有nonlocal，需要转变成可变类型)  
   eg: [bi_bao_nonlocal](/script/bibao_decorator.py)

装饰器

4. 定义：装饰器是闭包形式的一种实现，将函数作为一个参数，形成一个特殊的闭包。  
   eg: 耗时统计[decorator_outer](/script/bibao_decorator.py)  
   eg: 参数化装饰器，装饰器工厂函数[decorator_factory](/script/bibao_decorator.py)
5. 注意：增加@functools.wraps(func), 可以保持当前装饰器去装饰的函数的 __name__的值不变。

### 迭代器 生成器

迭代器

1. 可迭代对象：可以从中按一定的次序提取出其中的元素的对象，叫可迭代对象。如：字符串，列表，元组等。
2. 迭代器对象：迭代器可以记住遍历位置，从集合第一个元素开始访问，依次访问到最后，不能后退。
3. 创建迭代器对象：iter()， 输出迭代器对象的下一个元素：next()，如果没有了则会抛异常。也可用for循环遍历。  
   eg: [test_iterator](/script/iterator_generator.py)
4. 创建一个迭代器：把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__()。  
   __iter__() 方法返回一个特殊的迭代器对象，这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成；  
   __next__() 方法会返回下一个迭代器对象.  
   eg：创建一个返回数字的迭代器，初始值为1，逐步递增1 [MyIterator](/script/iterator_generator.py)

生成器

1. 使用了yield的函数被称为生成器，生成器不占内存，用多少取多少。
2. 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
3. 在调用生成器运行的过程中，每次遇到yield时函数会暂停并保存当前所有的运行信息，返回yield的值，并在下一次执行next()方法时从当前位置继续运行。
4. 调用一个生成器函数，返回的是一个迭代器对象。 eg:[test_generator](/script/iterator_generator.py)

### 静态方法 类方法 实例方法

1. 类与实例：类是创建实例的模板，实例则是一个个具体的对象。self指向实例对象， cls指向类对象。
2. 实例化的对象可以调静态方法，类方法，实例方法。
3. 类对象不可直接调实例方法，可直接调类方法，静态方法。
4. 实例方法和类方法，能够改变实例对象或类对象的状态，而静态方法不能。  
   eg: [MyClass](/script/some_method.py)

### GIL 进程 线程 协程

1. 进程：资源分配的最小单位；线程：程序执行的最小单位。协程：基于线程之上比线程更加轻量级。
2. 进程与进程之间是互相独立的，每个进程都会有一把GIL锁。
3. 线程使用：多线程下单个线程获取GIL锁，执行代码到sleep释放GIL锁。  
   科学计算需要持续使用cpu的任务，单线程比多线程快。  
   IO操作等可能引起阻塞的任务，多线程比单线程快。
4. [multiprocessing_pool](/script/multiprocessing_pool.py)，[concurrent_futures](/script/concurrent_futures.py)
   ，[gevent_pool](/script/gevent_pool.py)

### 设计模式

1. 单例模式：保证一个类仅有一个实例，而且在全局只有一个访问点。  
   eg: 使用__new__关键字实现 [MySingleton](/script/design_patterns.py)  
   使用函数装饰器实现单例 [my_singleton](/script/design_patterns.py)
2. 工厂模式：定义一个用于创建对象的接口，根据不同的参数来决定实例化哪个子类。  
   eg: [WhereHandler](/script/design_patterns.py)

### linux相关

1. 作用    
   实时查询最后100行日志  
   关键字搜索  
   关键字搜索显示上下5行  
   查询指定字符出现的行数  
   查询多个字符或出现的行数  
   查找指定文件的位置  
   指定字符串全部替换 查看所有正在运行的进程  
   查看端口号占用情况  
   查看进程信息  
   查看详细的进程信息  
   起服务  
   起定时脚本  
   查日志
2. 命令  
   tail -100f test.log  
   grep sanford test.log  
   grep -C 5 sanford test.log  
   grep -E sanford test.log | wc -l  
   grep -E "sanford｜luo" test.log | wc -l  
   find / -name test.log  
   sed 's/oldStr/newStr/g' test.log #(不带g只替换第一个)
   ps aux | less  
   netstat -apn | grep port  
   ps aux | grep python
   ps -aux | grep pid  
   sudo supervisorctl -c /etc/supervisor.conf  
   crontab -e  
   more test.log | grep -E "start|end" -C5  
