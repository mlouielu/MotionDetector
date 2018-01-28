# import the necessary packages
import datetime
import imutils
import time
import cv2

def transformImage(frame):
	# resize the frame, convert it to grayscale, and blur it
	frame = imutils.resize(frame, width=500)
	gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
	gray = cv2.GaussianBlur(gray, (21, 21), 0)
	return gray

def recordMotion(contours, currentFrameNum = 5, start = None, end = None):
	# loop over the contours
	if contours != None:
		for i, c in enumerate(contours):
			# if the contour is too small, ignore it
			if cv2.contourArea(c) > 500:
				if start == None:
					start = currentFrameNum
				end = currentFrameNum
				return start, end

	if start != None and end != None:
		print('Motion detected from frame {} to frame {}. \n'.format(start, end))
		start = None
		end = None
	return start, end

videoPath = "D:\\Rec\\output10.mp4" # Your file here.

# otherwise, we are reading from a video file
camera = cv2.VideoCapture(videoPath)

# initialize the first frame in the video stream

frameList = []

for i in range(0,5):
	(grabbed, frame) = camera.read()
	if grabbed:
		frameList.append(transformImage(frame))
	else:
		print("The script does not process video of less than five frames length.")
		break
cnt = 5
motionStart = None
motionEnd = None

# loop over the frames of the video
while True:
	# compute the absolute difference between the current frame and
	# first frame
	if cnt % 1800 == 0:
		print('Currently processing {}th frame.'.format(cnt))
	frameDelta = cv2.absdiff(frameList[0], frameList[-1])
	thresh = cv2.threshold(frameDelta, 25, 255, cv2.THRESH_BINARY)[1]

	# dilate the thresholded image to fill in holes, then find contours
	# on thresholded image
	thresh = cv2.dilate(thresh, None, iterations=2)
	(_, cnts, _) = cv2.findContours(thresh.copy(), cv2.RETR_EXTERNAL,
		cv2.CHAIN_APPROX_SIMPLE)

	motionStart, motionEnd = recordMotion(cnts, cnt, motionStart, motionEnd)
	
	key = cv2.waitKey(1) & 0xFF

	# if the `q` key is pressed, break from the lop
	if key == ord("q"):
		break

	# grab the current frame and initialize the occupied/unoccupied
	# text
	(grabbed, frame) = camera.read()

	# if the frame could not be grabbed, then we have reached the end
	# of the video
	if not grabbed:
		if motionStart != None and motionEnd != None:
			print('Motion detected from frame {} to frame {}'.format(motionStart, motionEnd))
		break
	else:
		frameList.append(transformImage(frame))
		frameList.pop(0)
		cnt += 1

# cleanup the camera and close any open windows
camera.release()
cv2.destroyAllWindows()
