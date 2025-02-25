clean:
	rm -rf pymiele.egg-info dist build

lint:
	isort pymiele
	black pymiele
	flake8 pymiele

install_dev:
	pip install -r requirements-dev.txt

test:
	pytest -s -v

bump:
	bump2version --allow-dirty patch setup.cfg pymiele/const.py

bump_minor:
	bump2version --allow-dirty minor setup.cfg pymiele/const.py

bump_major:
	bump2version --allow-dirty major setup.cfg pymiele/const.py

doc:
	rm -rf html
	pdoc --html --config show_source_code=False pyeasee

publish_docs: doc
	git subtree push --prefix html origin gh-pages
	# git push origin `git subtree split --prefix html master`:gh-pages --force

build: clean
	python -m build

publish_test:
	twine upload --repository testpypi dist/*

publish:
	# build publish_docs
	twine upload --repository pymiele dist/*

