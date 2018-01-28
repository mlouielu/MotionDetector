# MotionDetector

This is a short but convenient Python (3) script to detect motion in recorded videos. (You can also use it with your webcam, with minor modification).

## Benchmark

Processing an one-hour-long 30 fps mp4 file (H264, no audio, 640 * 480) requires around 12 minutes on my Core i5 laptop.

## Reference

Some code are ported from [Basic motion detection and tracking with Python and OpenCV](https://www.pyimagesearch.com/2015/05/25/basic-motion-detection-and-tracking-with-python-and-opencv/) by Adrian Rosebrock. Modification is about upgrading from openCV 2 to openCV 3, and outputting start / end frame of the motion.

The idea of comparing current frame with the fifth previous frame (or any other frame) is borrowed from [Motion Detection Algorithms](https://www.codeproject.com/articles/10248/motion-detection-algorithms), although the original article is about coding in .NET.
