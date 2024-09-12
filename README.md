[![Hits](https://hits.seeyoufarm.com/api/count/incr/badge.svg?url=https%3A%2F%2Fgithub.com%2Fcastilloglenn%2Fdataflow-animation&count_bg=%23328DF1&title_bg=%23555555&icon=myspace.svg&icon_color=%23E7E7E7&title=Visits&edge_flat=false)](https://hits.seeyoufarm.com)

# Dataflow Animation
**dataflow-animation** is an innovative Python library designed to simplify the visualization of data flows through **real-time animations**. Utilizing **Pygame** for rendering and **Watchdog** for live updates, Dataflow makes it effortless to develop, visualize, and refine complex data flow animations dynamically. This library is particularly useful for developers and analysts who need to create and present **data-driven animations and diagrams** that are both informative and visually engaging. With Dataflow, users can write Python code to define animations and see changes reflected **instantaneously** on the screen, making it an ideal tool for **rapid prototyping of data flow diagrams and animations**.

## Status
Currently in development. Not all features are complete, and significant changes might still be made.

## Installation

### Prerequisites
- Python 3.6 or higher
- pip
- git

### Setup Instructions

1. **Clone the repository**
   
   Clone the `dataflow-animation` repository to your local machine by running the following command:
```
git clone https://github.com/castilloglenn/dataflow-animation
```

2. **Navigate to the directory**
Change to the cloned directory:
```
cd dataflow-animation
```

3. **Create a virtual environment**
Set up a virtual environment to manage dependencies:
```
python3 -m venv venv
```

4. **Activate the virtual environment**
Activate the created virtual environment:
- On Windows:
  ```
  .\venv\Scripts\activate
  ```
- On macOS and Linux:
  ```
  source venv/bin/activate
  ```

5. **Install dependencies**
Install the necessary dependencies using the `setup` command provided in the Makefile:
```
make setup
```

## Running Examples

To run an example and see the library in action, use the following command:
```
make example
```

This will open a PyGame window displaying the animation specified in `examples/basic.py`. You can modify this file or just save it to see changes in real-time due to the live reloading feature provided by the library.


