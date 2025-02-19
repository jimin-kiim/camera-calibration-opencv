# camera-calibration-trial

## Installation

1. Install the packages from the `requirements.txt`
    ```
    $ python -m venv .venv
    $ source .venv/bin/activate (Mac)
      .venv\Scripts\Activate.ps1 (Windows)
    $ pip install --upgrade pip
    $ pip install -r requirements.txt
    ```

2. Install OpenCV </br>
The file, requirements.txt doesn't contain `opencv-python`. It's because we may also install it with `pip install` but for better stability while using `gstreamer`, downloading the source file from the OpenCV website and building the codes manually is recommended. The link for the source code and the guidance to use it is as follows:
    https://docs.opencv.org/4.x/da/df6/tutorial_py_table_of_contents_setup.html
