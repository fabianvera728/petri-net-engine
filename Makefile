dep: requirements.txt
	python3 -m pip install -r requirements.txt

build:
	python3 -m build
	python3 -m twine upload dist/*


