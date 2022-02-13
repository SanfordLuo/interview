### 框架部分
1. [Django](/docs/framework.md#Django)
   [Tornado](/docs/framework.md#Tornado)

###### Django
客户端 <-> web 服务器(Nginx 为例) <-> socket <-> WSGI <-> Django


###### Tornado
1. Tornado四大组件  
   ioloop实例：它是全局的tornado事件循环，服务器的引擎核心。  
   app实例：核心应用类，它会挂接一个服务端套接字端口对外提供服务，一个ioloop实例可以有多个app实例。  
   handler类：用来处理业务逻辑的。  
   Route：它将指定的url规则与handler类挂接起来，形成一个路由映射表。  
   关系：一个ioloop包含多个app管理多个服务端口，一个app包含一个路由表，一个路由表包含多个handler。  
2. 生命周期  
   一个请求，ioloop接收请求解包成一个http请求对象，找到该套接字上对应的app的路由表，通过url在路由表找到对应的handler；  
   handler处理完业务后返回一个对象，ioloop将返回对象处理成http响应对象返回给客户端。  
3. 与nginx反向代理实现负载均衡，supervisor做进程管理  
   开启多个tornado实例，每个实例监听一个端口，对应一个进程。多个请求打过来时nginx反向代理分配到不同的app实例实现负载均衡。一个进程挂了也不影响其他进程。  
4. 如何实现异步，tornado默认是单进程单线程的  
   使用通过协程的方式实现异步：添加异步装饰器 @tornado.gen.coroutine，内部需要用到yield关键字。  
   python3.5以上可以使用async、await来实现。  
5. 优点  
   5.1 Tornado的核心是ioloop和iostream这两个模块，前者提供了一个高效的I/O事件循环，后者则封装了一个无阻塞的socket。  
   通过向ioloop中添加网络I/O事件，利用无阻塞的socket，再搭配相应的回调函数，便可达到梦寐以求的高效异步执行。  
   5.2 使用同一个TCP连接来发送和接收多个HTTP请求/应答，而不是为每一个新的请求/应答打开新的连接的方法。  
