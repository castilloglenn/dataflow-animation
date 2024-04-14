setup:
	clear
	pip install -r requirements.txt
	pip install -e .

run_watchdog_test:
	clear
	dataflow /Users/mb-02/Documents/personal/dataflow-animation/tests/watchdog/test_realtime_file_updates.py

run_example:
	clear
	dataflow /Users/mb-02/Documents/personal/dataflow-animation/examples/simple.py
