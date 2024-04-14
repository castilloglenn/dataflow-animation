from setuptools import setup, find_packages

DESCRIPTION = ""
with open("README.md", "r", encoding="utf-8") as f:
    DESCRIPTION = f.read()

setup(
    name="dataflow-animation",
    version="0.1.0",
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
    python_requires=">=3.6",
    include_package_data=True,
    keywords="pygame watchdog live-coding development",
    license="MIT",
)
