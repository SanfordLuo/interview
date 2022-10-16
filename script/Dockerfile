FROM registry.xk12.cn/devopsproj/python-distro:3.8
# Python App

WORKDIR /app

COPY requirements.txt .

RUN set -ex; \
	\
	savedAptMark="$(apt-mark showmanual)"; \
	apt-get update; \
	apt-get install -y --no-install-recommends \
		gcc \
		libc6-dev; \
	\
	pip install --no-cache-dir -i https://mirrors.aliyun.com/pypi/simple/ -r requirements.txt; \
	apt-mark auto '.*' > /dev/null; \
	[ -z "$savedAptMark" ] || apt-mark manual $savedAptMark; \
	find /usr/local -type f -executable -not \( -name '*tkinter*' \) -exec ldd '{}' ';' \
		| awk '/=>/ { print $(NF-1) }' \
		| sort -u \
		| xargs -r dpkg-query --search \
		| cut -d: -f1 \
		| sort -u \
		| xargs -r apt-mark manual; \
	apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false; \
	rm -rf /var/lib/apt/lists/*

# TODO project defined
RUN set -ex; \
	projectName="ailearn-okminicourse-service"; \
	mkdir -p /xdfapp/apps/$projectName /xdfapp/logs/$projectName /xdfapp/apps/${projectName}-envs/conf /xdfapp/monitor-data/$projectName; \
	chown app:app /xdfapp/apps/$projectName /xdfapp/logs/$projectName /xdfapp/apps/${projectName}-envs/conf /xdfapp/monitor-data/$projectName

COPY . .

COPY docker-entrypoint.sh /usr/local/bin/
ENTRYPOINT ["docker-entrypoint.sh"]

EXPOSE 8080
CMD ["gunicorn", "-c", "deploy/gunicorn_conf.py", "main:app"]
