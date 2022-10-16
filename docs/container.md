## 容器

[Docker](/docs/container.md#Docker)  
[k8s](/docs/container.md#k8s)

### Docker

1. 相关概念  
   镜像：是文件，是一堆只读层的集合，像类；  
   静态容器：是镜像只读层+读写层，容器是镜像的运行实例；  
   运行态容器：静态容器+隔离的进程空间+进程  
   DockerFile：文本文件，使用其中的指令自动构建镜像，每一条指令构建一层。

2. Dockerfile相关指令  
   FROM：第一条指令，为后续的指令建立基础镜像。eg：`FROM python:3.7.9`  
   WORKDIR：为其他指令设置工作目录。eg：`WORKDIR /app`  
   COPY：复制本地文件到镜像中。eg：`COPY requirements.txt .`  
   RUN：在映像层中添加功能层，比如更新包。eg：`RUN apt-get update`  
   ENTRYPOINT：设定容器启动时第一个运行的命令及其参数。eg：`ENTRYPOINT ["/docker-entrypoint.sh"]`  
   EXPOSE：暴露容器的端口，docker run的时候不用-p指定端口了。eg：`EXPOSE 8080`  
   CMD：为执行的容器提供默认值，最后一个cmd才会生效。eg：`CMD ["gunicorn", "-c", "deploy/gunicorn_conf.py", "main:app"]`  
   示例文件：[Dockerfile](/script/Dockerfile)；[docker-entrypoint.sh](/script/docker-entrypoint.sh)

3. docker常用命令  
   使用Dockerfile创建镜像：`docker build`  
   下载镜像：`docker pull mysql:5.7`  
   查看所有镜像：`docker images`  
   删除镜像：`docker rmi -f 镜像id`  
   新建容器并启动：`docker run 镜像id`  
   查看所有正在运行的容器：`docker ps`  
   启动容器：`docker start/restart 容器id`  
   停止容器：`docker stop/kill 容器id`  
   删除容器：`docker rm 容器id`  
   进入容器：`docker exec -it 容器id /bin/bash(/bin/sh)`

4. 搭建私有仓库  
   安装指令：`docker pull registry`  
   配置私有仓库地址：`vim /etc/docker/daemon.json`  
   daemon.json中加上自己的ip地址：`"insecure-registries": ["127.0.0.1:5000"]`  
   创建私有仓库的容器：`docker run -d -p 5000:5000 --name registry docker.io/registry`  
   浏览器访问：`http://127.0.0.1:5000/v2/_catalog`  
   标记要推送到私有仓库的镜像：`docker tag test_my:1.1 127.0.0.1:5000/test_my:1.1`  
   推送到私有仓库：`docker push 127.0.0.1:5000/test_my:1.1`  
   从私有仓库下载：`docker pull 127.0.0.1:5000/test_my:1.1`

### k8s