#!/usr/bin/make
.PHONY: buildout cleanall test instance

bootstrap.py:
	wget http://downloads.buildout.org/2/bootstrap.py

bin/pip:
	virtualenv-2.7 .
	touch $@

bin/buildout: buildout.cfg bin/pip
	./bin/pip install -r requirements.txt
	touch $@

buildout: bin/buildout
	./bin/buildout -t 7

test: buildout
	./bin/test

instance: buildout
	./bin/instance fg

cleanall:
	rm -rf bin develop-eggs downloads include lib parts .installed.cfg .mr.developer.cfg bootstrap.py parts/omelette

docker-test:
	docker pull docker-staging.imio.be/iasmartweb/test:$(shell id -u)
	docker run -u $(shell id -u):$(shell id -g) --rm -v "$(shell pwd):/src" -w /src docker-staging.imio.be/iasmartweb/test:$(shell id -u) bash -c 'virtualenv -p python2.7 . && bin/pip install -r requirements.txt && bin/buildout && /etc/init.d/xvfb start && bin/test --all'
