import re

from setuptools import setup, find_packages


DESCRIPTION = ""
with open("README.md", "r", encoding="utf-8") as readme_file:
    DESCRIPTION = readme_file.read()


def find_version():
    with open(
        "dataflow_animation/__init__.py",
        "r",
        encoding="utf-8",
    ) as init_file:
        version_match = re.search(
            r"^__version__ = ['\"]([^'\"]*)['\"]",
            init_file.read(),
            re.M,
        )
        if version_match:
            return version_match.group(1)
        raise RuntimeError("Unable to find version string.")


setup(
    name="dataflow-animation",
    version=find_version(),
    description="Python library that draws data flow animations.",
    long_description=DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Allen Glenn E. Castillo",
    author_email="allenglenn.castillo@gmail.com",
    url="https://github.com/castilloglenn/dataflow-animation",
    packages=find_packages(),
    install_requires=["pygame", "watchdog"],
    entry_points={
        "console_scripts": [
            "dataflow=dataflow_animation.client.main:main",
        ],
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Build Tools",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
    ],
    python_requires=">=3.8",
    include_package_data=True,
    keywords="pygame watchdog live-coding development",
    license="MIT",
)
