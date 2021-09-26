APP_NAME ?= app
APP_PY ?= app.py

.SILENT:

install i:
	rm -fr env
	virtualenv -p python3.9 env
	sleep 1
	. env/bin/activate
	sleep 1
	pip install -r requirements.txt


build b:
	rm -fr dist/

	pyinstaller \
		$(APP_PY) \
		--clean \
		--onefile \
		--add-data="base-v0.1.0.postman_collection.json:base-v0.1.0.postman_collection.json" \
		--add-data="templates:templates" \
		--add-data="static:static"

	rm -fr build/ *.spec
