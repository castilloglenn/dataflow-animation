import os
import sys
import time
import logging
import importlib.util

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class ScriptHandler(FileSystemEventHandler):
    def __init__(self, directory, filename):
        self.directory = directory
        self.filename = filename
        self.path = os.path.join(directory, filename)

        self.last_known_version = None

    def on_modified(self, event):
        if event.src_path == self.path:
            self.load_and_run()

    def load_and_run(self):
        spec = importlib.util.spec_from_file_location(
            "current_module",
            self.path,
        )
        module = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(module)
            if hasattr(module, "Test"):
                logging.info("File change detected. Running Test...")
                module.Test()
            else:
                logging.error("No Test class found in the script.")

        # pylint: disable=W0718
        except Exception as e:
            logging.error("Error loading script:\n%s: %s", type(e).__name__, e)


def main(path):
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
    )

    directory, filename = os.path.split(path)
    event_handler = ScriptHandler(directory, filename)
    observer = Observer()
    observer.schedule(event_handler, path=directory, recursive=False)
    observer.start()

    logging.info("Watching for changes. Press Ctrl+C to stop.")
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        pass
    finally:
        observer.stop()
        observer.join()
        logging.info("Stopped watching.")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        logging.error("Usage: dataflow <full_path_to_file.py>")
        sys.exit(1)

    main(sys.argv[1])
