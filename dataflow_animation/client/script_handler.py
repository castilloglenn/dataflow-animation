from importlib.machinery import ModuleSpec
import os
import logging
import importlib.util
import traceback
from types import ModuleType

from watchdog.events import FileSystemEventHandler, FileModifiedEvent

from dataflow_animation.core.renderer import PygameRenderer
from dataflow_animation import Dataflow


class ScriptHandler(FileSystemEventHandler):
    def __init__(
        self,
        directory: str,
        filename: str,
        renderer: PygameRenderer,
    ):
        self.directory = directory
        self.filename = filename
        self.path = os.path.join(directory, filename)

        self.renderer = renderer
        self.last_known_version = None

    def on_modified(self, event: FileModifiedEvent):
        if event.src_path == self.path:
            self.load_and_run()

    def load_and_run(self):
        spec: ModuleSpec = importlib.util.spec_from_file_location(
            "current_module",
            self.path,
        )
        module: ModuleType = importlib.util.module_from_spec(spec)
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
        except Exception:
            logging.error("Error loading script:\n%s", traceback.format_exc())

            self.renderer.set_animation(None)
