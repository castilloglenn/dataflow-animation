setup:
	clear
	pip install -r requirements.txt
	pip install -e .

run:
	clear
	dataflow /Users/mb-02/Documents/personal/dataflow-animation/examples/basic.py

run_watchdog_test:
	clear
	dataflow /Users/mb-02/Documents/personal/dataflow-animation/tests/watchdog/realtime_file_updates.py

run_example:
	clear
	dataflow /Users/mb-02/Documents/personal/dataflow-animation/examples/simple.py

test:
	clear
	pytest tests
