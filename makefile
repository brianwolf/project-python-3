VERSION := local

compile c:
	python -m compile -b -f -o dist/ .
	cp -rf variables.yaml dist/

package:
	rm -fr build dist *.spec
	pyinstaller --add-binary logic:logic -n python-example --onefile app.py 
	mv dist/python-example python-example
	rm -fr build dist *.spec
	