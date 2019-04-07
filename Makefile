clean:
	find . -name '*.py[co]' -delete

virtualenv:
	virtualenv --prompt '>< Organizer >< ' --python=python3 env
	env/bin/pip install -r requirements.txt
	@echo
	@echo "VirtualENV Setup Complete. Now run: source env/bin/activate"
	@echo

test:
	python -m pytest \
		-v \
		--cov=organizer \
		--cov-report=term \
		--cov-report=html:coverage-report \
		tests/
build:
	pyinstaller --onefile organizer.py
install:
	if [ -f "~/.local/bin/or" ]; then rm -rf ~/.local/bin/or; fi
	cp dist/organizer ~/.local/bin/or
	if [ -d "build" ]; then rm -rf build; fi
	if [ -d "dist" ]; then rm -rf dist; fi
