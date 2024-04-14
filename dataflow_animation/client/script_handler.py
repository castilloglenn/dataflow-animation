import os
import logging
import importlib.util

from watchdog.events import FileSystemEventHandler

from dataflow_animation import Dataflow


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
            elif hasattr(module, "Animation"):
                if not issubclass(module.Animation, Dataflow):
                    logging.error(
                        "Animation class must inherit from Dataflow.",
                    )
                    self.renderer.set_animation(None)
                    return
                logging.info("File change detected. Applying animation...")
                self.renderer.set_animation(module.Animation())
            else:
                logging.error(
                    "No Animation class found in the script.",
                )
                self.renderer.set_animation(None)

        # pylint: disable=W0718
        except Exception as e:
            logging.error("Error loading script:\n%s: %s", type(e).__name__, e)
            self.renderer.set_animation(None)
