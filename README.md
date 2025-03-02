## Camera Calibration

##### About Camera and Camera Calibration Ref: https://3dvision.princeton.edu/courses/COS429/2015fa/slides/02_camera/

<p align="center">
  <img src="./asset/0212_camera.jpg" width="40%">
</p>

##### <p align="center">Figure 1: Camera, generated with Leonardo.ai</p>
###### prompt: On the left side, a person is staring at the sky and the sky is full of stars and also the Saturn is there. And the chair and trees are, too. And a 3D coordinate system axes are passing through the view. The three axes, x, y, and z should be all shown. Following one of the axes, there's a camera. Starting from the point where the camera is, the view is converted to a 2D world. There should be a coordinate system representation including 2 axes. On the right side, where axes for 2D are, the image frames are flying and piled up.

  Cameras capture the 3D world and record the view into a 2D image, also called frame in video. 
  <br>
  While converting the dimesion, distortion occurs and to correct it, we use 'calibration'. It's getting camera matrix and distortion coefficients, necessary for undistortion process.
  <br>
  This Repository contains the basic source codes for camera calibration and image undistortion using OpenCV.

<br>

## Installation

### 1. Install the packages from the `requirements.txt`

while installing the packages, if the errors occur, please refer to `ERROR_REFERENCE.md`.

    
    $ python -m venv .venv
    $ source .venv/bin/activate (Mac)
      .venv\Scripts\Activate.ps1 (Windows)
    $ pip install --upgrade pip
    $ pip install -r requirements.txt

<br>

### 2. Install OpenCV </br>
The file, `requirements.txt` doesn't contain `opencv-python`. It's because we can also install it with `pip install` but for better stability to use `gstreamer`, downloading the source file from the OpenCV website and building the codes manually is recommended. 
<br><br>
The link for the source code and the guidance to use it is as follows:
<br>
https://docs.opencv.org/4.x/da/df6/tutorial_py_table_of_contents_setup.html

<br>

## Usage

run the final cell of the `ipynb file` or execute the `py file`.

#### 1. to Correct the distortion of an image:
- source code: `calibration.py`
- source code with comments to understand the process: `calibration.ipynb`

#### 2. to Calibrate the camera with a video file:
- source code: `calibration_with_mp4.py`
- source code with comments to understand the process: `calibration_with_mjepg.ipynb`

#### 3. to record a video with a camera
- source code: `video_recording.py`
- source code with comments to understand the process: `video_recording.ipynb`
