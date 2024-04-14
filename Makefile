setup:
	clear
	pip install -r requirements.txt
	pip install -e .

example:
	clear
	dataflow /Users/mb-02/Documents/personal/dataflow-animation/examples/basic.py

test:
	clear
	pytest tests
