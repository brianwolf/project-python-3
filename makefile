VERSION := local

compile c:
	python -m compile -b -f -o dist/ .
	cp -rf logic/resources/ dist/logic/
	rm -fr dist/env/
