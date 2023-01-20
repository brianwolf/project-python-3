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


package pk:
	rm -fr build dist *.spec
	
	pyinstaller \
		--add-data "logic/resources:logic/resources" \
		--add-binary "logic:logic" \
		-n example \
		--onefile app.py 
	
	mv dist/example example
	rm -fr build dist *.spec