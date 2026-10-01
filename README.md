# Python Machine Vision Fundamentals

A collection of **machine vision and image-processing implementations developed in Python using OpenCV and NumPy** as part of my university Machine Vision coursework.

The project explores fundamental computer-vision operations including colour-space conversion, image thresholding, geometric transformations, smoothing filters, edge detection, intensity manipulation and histogram equalisation.

Rather than representing a single application, the repository documents a progression through the core image-processing techniques that underpin larger computer-vision and robotic-perception systems.

---

## Project Overview

The project is organised into four main areas:

```text
Machine Vision Fundamentals
│
├── 1. Image Basics
│   ├── Image loading
│   ├── Grayscale conversion
│   ├── HSL / HSV conversion
│   ├── Intensity thresholding
│   └── Hue thresholding
│
├── 2. Geometric Transformations
│   ├── Translation
│   └── Rotation
│
├── 3. Filtering & Edge Detection
│   ├── Mean filtering
│   ├── Gaussian filtering
│   └── Canny edge detection
│
└── 4. Intensity & Histogram Processing
    ├── Image property analysis
    ├── Grayscale normalisation
    ├── Intensity range reduction
    └── Histogram equalisation
```

Each script focuses on a particular machine-vision concept and provides a visual comparison of the resulting image transformations.

---

## Technologies

- Python
- OpenCV
- NumPy
- Digital Image Processing
- Computer Vision
- Machine Vision

---

## Repository Structure

```text
python-machine-vision-fundamentals/
│
├── README.md
├── LICENSE
├── requirements.txt
│
└── src/
    ├── 01_image_basics/
    │   ├── image_loading.py
    │   ├── colour_space_conversion.py
    │   ├── intensity_thresholding.py
    │   └── hue_thresholding.py
    │
    ├── 02_geometric_transformations/
    │   ├── image_translation.py
    │   └── image_rotation.py
    │
    ├── 03_filtering_and_edges/
    │   ├── mean_filtering.py
    │   ├── gaussian_filtering.py
    │   └── canny_edge_detection.py
    │
    └── 04_intensity_and_histograms/
        ├── image_properties.py
        ├── grayscale_normalisation.py
        ├── intensity_range_reduction.py
        └── histogram_equalisation.py
```

The filenames have been updated from the original coursework question numbering to describe the functionality demonstrated by each script more clearly.

---

# 1. Image Loading & Colour-Space Conversion

The first group of exercises introduces image loading and representation using OpenCV.

## Image Loading

`image_loading.py` demonstrates the basic OpenCV image-processing workflow:

```text
Image File
    |
    v
cv2.imread()
    |
    v
Image Array
    |
    v
cv2.imshow()
    |
    v
Display Window
```

An image is loaded into memory using:

```python
image = cv2.imread("Colosseum.JPG")
```

and displayed using an OpenCV window.

This forms the basic input pipeline used throughout the remainder of the project.

---

## Colour-Space Conversion

`colour_space_conversion.py` converts the original image into several different representations:

```text
                Original BGR Image
                       |
           +-----------+-----------+
           |           |           |
           v           v           v
       Grayscale      HSL         HSV
```

The conversions are performed using OpenCV's `cvtColor()` functionality.

### Grayscale

```python
grayscale = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
```

The three-channel colour image is converted into a single-channel intensity representation.

### HSL

```python
hsl = cv2.cvtColor(image, cv2.COLOR_BGR2HLS)
```

This separates image information into:

- Hue
- Lightness
- Saturation

### HSV

```python
hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
```

This separates the image into:

- Hue
- Saturation
- Value

These alternative representations can make particular visual characteristics easier to isolate than when working directly with BGR/RGB pixel values.

---

# Image Thresholding

Thresholding converts image information into a binary representation.

Conceptually:

```text
Pixel Value
     |
     v
Compare Against Threshold
     |
  +--+--+
  |     |
Below  Above
  |     |
  v     v
  0    255
```

This produces an image containing two output levels.

---

## Intensity Thresholding

`intensity_thresholding.py` first converts the source image into grayscale.

A threshold value of:

```text
90
```

is then applied using:

```python
cv2.threshold()
```

Pixels are classified according to their intensity.

```text
Original Image
      |
      v
   Grayscale
      |
      v
Threshold = 90
      |
      v
 Binary Image
```

This demonstrates basic image segmentation using pixel intensity.

---

## Hue Thresholding

`hue_thresholding.py` explores thresholding using colour information rather than grayscale intensity.

The source image is converted into HSV:

```text
BGR Image
    |
    v
HSV Image
    |
    v
Extract Hue Channel
    |
    v
Hue Threshold
    |
    v
Binary Image
```

The Hue channel is extracted using:

```python
hue_channel = hsv[:, :, 0]
```

and a threshold value is applied to generate a binary representation.

This demonstrates how colour information can be used as the basis for image segmentation.

---

# 2. Geometric Transformations

The second section explores transformations that modify the spatial position or orientation of an image.

The project implements:

```text
Geometric Transformations
│
├── Translation
│
└── Rotation
```

Both transformations use affine transformation matrices with OpenCV.

---

## Image Translation

`image_translation.py` translates the image:

```text
50 pixels right
30 pixels down
```

using the affine transformation matrix:

```text
┌            ┐
│ 1   0   tx │
│ 0   1   ty │
└            ┘
```

where:

```text
tx = 50
ty = 30
```

The transformation is applied using:

```python
cv2.warpAffine()
```

Conceptually:

```text
Original Image
      |
      v
Translation Matrix
      |
      v
cv2.warpAffine()
      |
      v
Translated Image
```

---

## Image Rotation

`image_rotation.py` rotates the source image by:

```text
45°
```

around the centre of the image.

The rotation matrix is generated using:

```python
cv2.getRotationMatrix2D()
```

and then applied using:

```python
cv2.warpAffine()
```

Two versions of the result are generated.

### Fixed Image Bounds

The first rotation retains the dimensions of the original image.

```text
Original Bounds
+----------------+
|      /\        |
|     /  \       |
|    /    \      |
|   /      \     |
+----------------+
```

Parts of a rotated image may therefore fall outside the original frame.

### Expanded Bounds

The second implementation calculates new dimensions based on the sine and cosine components of the rotation matrix.

```text
Original Image
      |
      v
45° Rotation Matrix
      |
      v
Calculate New Bounds
      |
      v
Adjust Translation
      |
      v
Rotate Into Larger Frame
```

The translation components of the rotation matrix are then adjusted so the rotated image is repositioned within the enlarged output frame.

This prevents the rotated image from being unnecessarily cropped.

---

# 3. Smoothing Filters & Edge Detection

The third section explores image filtering.

```text
Original Image
      |
      +------------------+
      |                  |
      v                  v
  Smoothing          Edge Detection
      |                  |
  +---+---+              |
  |       |              |
  v       v              v
 Mean   Gaussian       Canny
```

---

# Mean Filtering

`mean_filtering.py` applies averaging filters with several kernel sizes:

```text
5 × 5
10 × 10
15 × 15
```

A mean filter replaces each pixel using the average intensity of neighbouring pixels within the kernel.

Conceptually:

```text
Neighbourhood

+---+---+---+
|   |   |   |
+---+---+---+
|   | X |   |  -> Average values
+---+---+---+
|   |   |   |
+---+---+---+
        |
        v
   New Pixel Value
```

Increasing the kernel size causes progressively stronger smoothing because a larger neighbourhood contributes to each output pixel.

---

# Gaussian Filtering

`gaussian_filtering.py` applies Gaussian smoothing using several standard-deviation values:

```text
σ = 10
σ = 20
σ = 40
```

Unlike a simple mean filter, a Gaussian filter gives different weights to neighbouring pixels based on their distance from the centre of the kernel.

Conceptually:

```text
          Lower Weight
              |
              v
        +-------------+
        |             |
        |    +---+    |
        |    | X |    | <- Greater Weight
        |    +---+    |
        |             |
        +-------------+
```

The implementation dynamically calculates a kernel size from sigma:

```python
kernel_size = int(6 * sigma + 1)
```

The resulting configurations for the values used in the coursework are:

```text
Sigma 10 -> 61 × 61 kernel
Sigma 20 -> 121 × 121 kernel
Sigma 40 -> 241 × 241 kernel
```

The results demonstrate the effect of increasing Gaussian smoothing strength.

---

# Canny Edge Detection

`canny_edge_detection.py` applies the Canny edge detector to a grayscale image.

Three threshold configurations are compared:

```text
Low:       50, 100

Medium:   100, 200

High:     150, 250
```

The basic processing pipeline is:

```text
Original Image
      |
      v
   Grayscale
      |
      v
 Canny Detector
      |
      v
Detected Edges
```

Comparing multiple threshold values demonstrates how the detector's sensitivity affects which image gradients are retained as edges.

Lower thresholds detect more potential edges, while higher thresholds produce a more selective result.

---

# 4. Intensity Range & Histogram Processing

The final group of exercises investigates pixel intensity representation and contrast.

```text
Intensity Processing
│
├── Image Properties
├── Grayscale Conversion
├── Normalisation
├── Intensity Reduction
└── Histogram Equalisation
```

---

# Image Properties

`image_properties.py` examines basic properties of a colour image.

Using:

```python
height, width, channels = image.shape
```

the program reports:

```text
Image Dimensions
│
├── Width
├── Height
└── Number of Channels
```

This demonstrates the underlying array representation used by OpenCV images.

---

# Grayscale Normalisation

`grayscale_normalisation.py` converts the source image into grayscale and normalises the resulting intensity values into the range:

```text
[0, 255]
```

using:

```python
cv2.normalize()
```

Conceptually:

```text
Original Image
      |
      v
   Grayscale
      |
      v
Find Intensity Range
      |
      v
   Normalise
      |
      v
    0 - 255
```

This demonstrates intensity scaling across the available 8-bit grayscale range.

---

# Intensity Range Reduction

`intensity_range_reduction.py` explores the visual effect of representing an image using progressively reduced intensity ranges.

The project tests:

```text
255
128
64
32
16
8
```

as the upper intensity value.

Conceptually:

```text
Original Grayscale
        |
        +--> [0,255]
        |
        +--> [0,128]
        |
        +--> [0,64]
        |
        +--> [0,32]
        |
        +--> [0,16]
        |
        +--> [0,8]
```

The implementation scales the original grayscale image using NumPy.

This provides a visual demonstration of how reducing available intensity information affects image representation.

---

# Histogram Equalisation

`histogram_equalisation.py` applies histogram equalisation to a grayscale image using:

```python
cv2.equalizeHist()
```

The original grayscale image and equalised result are displayed for comparison.

Conceptually:

```text
Original Grayscale
        |
        v
Intensity Distribution
        |
        v
Histogram Equalisation
        |
        v
Redistributed Intensities
        |
        v
Equalised Image
```

Histogram equalisation can increase contrast by redistributing grayscale intensities across the available range.

---

# Machine Vision Pipeline

Although the scripts are individual exercises, the techniques explored form parts of a typical machine-vision processing pipeline.

```text
              IMAGE / CAMERA
                    |
                    v
             Image Acquisition
                    |
                    v
           Colour-Space Conversion
                    |
                    v
                Filtering
                    |
                    v
          +---------+---------+
          |                   |
          v                   v
     Thresholding         Edge Detection
          |                   |
          +---------+---------+
                    |
                    v
             Feature Extraction
                    |
                    v
              Perception
                    |
                    v
          Higher-Level System
```

Image processing techniques such as these provide the foundation for more advanced perception systems.

---

# Installation

Clone the repository and install the Python dependencies:

```bash
pip install -r requirements.txt
```

The project requires:

```text
opencv-python
numpy
```

---

# Running the Scripts

Each example can be run independently.

For example:

```bash
python src/01_image_basics/colour_space_conversion.py
```

or:

```bash
python src/03_filtering_and_edges/canny_edge_detection.py
```

The scripts use OpenCV display windows and wait for a keyboard input before closing.

---

# Source Images

The original coursework used two image files:

```text
Colosseum.JPG
peppers.png
```

These images are not included in this repository unless redistribution rights have been confirmed.

To run the examples, suitable replacement images can be provided and the image paths within the scripts updated accordingly.

---

# Concepts Demonstrated

This project provided practical experience with:

- Python
- OpenCV
- NumPy
- Image acquisition
- Image arrays
- Colour spaces
- BGR
- Grayscale
- HSL / HLS
- HSV
- Image thresholding
- Binary images
- Colour-based segmentation
- Affine transformations
- Translation matrices
- Rotation matrices
- Image-bound calculations
- Mean filtering
- Gaussian filtering
- Kernel sizing
- Canny edge detection
- Intensity normalisation
- Intensity-range manipulation
- Histogram equalisation
- Digital image processing
- Machine vision fundamentals

---

# Original Coursework

The implementations in this repository originate from university Machine Vision coursework.

The original scripts were organised according to individual assignment questions and parts.

For portfolio presentation, the filenames and directory structure have been reorganised according to their actual machine-vision functionality.

The underlying implementations remain representative of the work completed during the course, with only minor corrections and repository organisation applied during portfolio preparation.

---

# Retrospective

This project represents foundational machine-vision work.

The individual operations are relatively simple in isolation, but they form important building blocks for larger perception systems.

For example:

```text
Colour Conversion
       +
   Thresholding
       +
    Filtering
       +
 Edge Detection
       |
       v
Basic Visual Perception
```

A more advanced system could combine these operations with:

- Contour detection
- Connected-component analysis
- Feature extraction
- Object tracking
- Camera calibration
- Perspective transformation
- Classical object detection
- Machine learning
- Deep-learning-based perception

---

# How I Would Develop It Further

Rather than maintaining each operation as an entirely separate script, a modern version could expose the processing operations through reusable functions or classes.

For example:

```text
                  VisionPipeline
                        |
       +----------------+----------------+
       |                |                |
       v                v                v
ColourProcessor    ImageFilter     EdgeDetector
       |                |                |
       +----------------+----------------+
                        |
                        v
                   Processed
                     Image
```

Configuration could then determine which processing stages are enabled.

For example:

```python
pipeline = VisionPipeline()

pipeline.to_grayscale()
pipeline.gaussian_blur()
pipeline.detect_edges()
```

This would make the code easier to reuse within larger machine-vision applications.

---

# Robotics Context

These fundamental image-processing techniques are particularly relevant to robotics because camera data usually requires processing before it can be used for decision-making.

```text
Camera
   |
   v
Raw Image
   |
   v
Pre-Processing
   |
   v
Segmentation / Features
   |
   v
Object / Environment Understanding
   |
   v
Robot Decision Making
   |
   v
Control
```

Operations explored in this repository — particularly colour-space conversion, filtering, thresholding and edge detection — can therefore form the early stages of a robotic perception pipeline.

---

# Portfolio Context

This project documents part of my progression into computer vision and robotic perception.

It demonstrates the underlying image-processing concepts on which more advanced computer-vision systems are built:

```text
Image Processing Fundamentals
             |
             v
       Machine Vision
             |
             v
     Computer Vision
             |
             v
   Robotic Perception
             |
             v
 Autonomous Systems
```

The project therefore complements my wider robotics work by demonstrating the image-processing foundations behind camera-based perception systems.
