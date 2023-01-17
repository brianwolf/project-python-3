VERSION := local

compile c:
	python -m compile -b -f -o dist/ .
	cp -rf logic/resources/ dist/logic/
	rm -fr dist/env/


build b:
	docker build . -t docker.io/brianwolf94/python-example:$(VERSION)


push p:
	docker push docker.io/brianwolf94/python-example:$(VERSION)


run r:
	docker run -it --rm -p 5000:5000 docker.io/brianwolf94/python-example:$(VERSION)