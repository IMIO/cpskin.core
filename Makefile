#!/usr/bin/make
.PHONY: buildout cleanall test instance

bootstrap.py:
	wget http://downloads.buildout.org/2/bootstrap.py

bin/python:
	virtualenv-2.7 .
	touch $@

bin/buildout: bootstrap.py buildout.cfg bin/python
	./bin/python bootstrap.py
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
	docker run --rm -v "$(shell pwd):/src" -w /src docker-staging.imio.be/cpskin.test:latest bash -c 'python bootstrap.py buildout:download-cache=/.buildout/buildout-cache/downloads buildout:eggs-directory=/.buildout/buildout-cache/eggs && bin/buildout buildout:download-cache=/.buildout/buildout-cache/downloads buildout:eggs-directory=/.buildout/buildout-cache/eggs && bin/test --all'
