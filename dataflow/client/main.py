import os
import sys
import time
import logging
import threading

from watchdog.observers import Observer

from dataflow.core.renderer import PygameRenderer
from dataflow.client.script_handler import ScriptHandler


def observe(path, renderer):
    directory, filename = os.path.split(path)
    event_handler = ScriptHandler(directory, filename, renderer)
    observer = Observer()
    observer.schedule(event_handler, path=directory, recursive=False)
    logging.info("File: %s", filename)
    logging.info("Watching for changes. Press Ctrl+C to stop.")
    observer.start()

    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        logging.info("Stopping watcher...")
    finally:
        renderer.stop()
        observer.stop()
        observer.join()
        logging.info("Stopped watching.")


def setup(filepath):
    renderer = PygameRenderer()
    watcher_thread = threading.Thread(
        target=observe, args=(filepath, renderer), daemon=True
    )
    watcher_thread.start()
    renderer.init()

    try:
        renderer.run()
    finally:
        renderer.stop()


def main():
    logging.basicConfig(
        level=logging.INFO,
        format="[%(asctime)s] %(message)s",
        datefmt="%Y/%m/%d %H:%M:%S",
    )

    if len(sys.argv) != 2:
        logging.error(
            "Invalid number of arguments. "
            + "Usage: dataflow "
            + "<full_path_to_file_to_watch.py>",
        )
        sys.exit(1)

    path_arg = sys.argv[1]
    if not os.path.exists(path_arg):
        logging.error("File does not exist: %s", path_arg)
        sys.exit(1)

    setup(path_arg)
