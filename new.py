#background matters

#import the cv2 and numpy libraries.
import cv2
import numpy as np

#Start the video capture.
video = cv2.VideoCapture(0)

#Read the image which will be shown when the black object will get masked and save it in an “image” variable.
image = cv2.imread("me.jpeg")

while True:
#Start reading the frames of the video.  
  ret, frame = video.read()
  
#Resize the image and the video to 640, 480.
  frame = cv2.resize(frame, (640, 480)) 
  image = cv2.resize(image, (640, 480)) 
  
#Create an array of RGB of faint black color shade and dark shade of black and store in the l_black and u_black
  u_black= np.array([104, 153,70])
  l_black= np.array([30,30,0])
  
#Create a mask using cv’s inRange() function and pass the frame , l_black and u_black as the parameters
  mask = cv2.inRange(frame, l_black, u_black)
  res = cv2.bitwise_and(frame, frame, mask= mask)
  
#Using np.where() function to return frame or image if the value of f is 0.
  f = frame.resf = np.where(f==0,image,f)
  
#Show the real video and masked video.
  cv2.imshow("video", frame)
  cv2.imshow("mask", f)
  
#Break the loop if the user presses “Esc” or “Q”. 
  if cv2.waitKey(1) & 0xFF == ord('q'):
     break
     
video.release()
cv2.destroyAllWindows()