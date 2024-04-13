import os
import sys
import time
import logging
import threading
import importlib.util

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from dataflow.core.renderer import PygameRenderer


class ScriptHandler(FileSystemEventHandler):
    def __init__(self, directory, filename, renderer):
        self.directory = directory
        self.filename = filename
        self.path = os.path.join(directory, filename)

        self.renderer = renderer
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
            elif hasattr(module, "draw"):
                logging.info("File change detected. Running draw...")
                self.renderer.set_draw_func(module.draw)
            else:
                logging.error(
                    "No Test class or draw method found in the script.",
                )
                self.renderer.set_draw_func(None)

        # pylint: disable=W0718
        except Exception as e:
            logging.error("Error loading script:\n%s: %s", type(e).__name__, e)
            self.renderer.set_draw_func(None)


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
