import numpy as np
import cv2
import cv2.aruco as aruco
import glob
import socket
import math
from polylabel import polylabel

#Setting variables
#TCP_IP = '169.254.137.76'
#ser = serial.Serial('/dev/ttyUSB0')
TCP_IP = '127.0.0.1'
TCP_PORT = 5005
BUFFER_SIZE = 1024
FRAME_WIDTH = 480
FRAME_HEIGHT = 640

#Setting up socket connection
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

#Setting up video-capture on camera with ID = 0
cap = cv2.VideoCapture(0)

# termination criteria
criteria = (cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001)

# prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(6,5,0)
objp = np.zeros((6*7,3), np.float32)
objp[:,:2] = np.mgrid[0:7,0:6].T.reshape(-1,2)

# Arrays to store object points and image points from all the images.
objpoints = [] # 3d point in real world space
imgpoints = [] # 2d points in image plane.

def find_1D_midpoint(first_loc, second_loc):
    return (first_loc + second_loc) / 2
    
def floor_midpoint(midpoint):
    return (math.floor(midpoint[0]), math.floor(midpoint[1]))

#Aruco image calibration
images = glob.glob('calib_images/*.jpg')
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

    ret, corners = cv2.findChessboardCorners(gray, (7,6),None)

    # If found, add object points, image points (after refining them)
    if ret == True:
        objpoints.append(objp)

        corners2 = cv2.cornerSubPix(gray,corners,(11,11),(-1,-1),criteria)
        imgpoints.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, (7,6), corners2,ret)


ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(objpoints, imgpoints, gray.shape[::-1],None,None)

while (True):
    ret, frame = cap.read()
    # operations on the frame come here
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    aruco_dict = aruco.Dictionary_get(aruco.DICT_6X6_250)
    parameters = aruco.DetectorParameters_create()

    #lists of ids and the corners beloning to each id
    corners, ids, rejectedImgPoints = aruco.detectMarkers(gray, aruco_dict, parameters=parameters)

    
   # print(ids)

    font = cv2.FONT_HERSHEY_SIMPLEX #font for displaying text (below)

    if np.all(ids != None):
        rvec, tvec,_ = aruco.estimatePoseSingleMarkers(corners, 0.05, mtx, dist) #Estimate pose of each marker and return the values rvet and tvec---different from camera coefficients
        marker_midpoints = []
        for index, id in zip(range(len(ids)), ids):
            topleftX = math.floor(corners[index][0][0][0])
            topleftY = math.floor(corners[index][0][0][1])
            toprightX = math.floor(corners[index][0][1][0])
            toprightY = math.floor(corners[index][0][1][1])
            bottomrightX = math.floor(corners[index][0][2][0])
            bottomrightY = math.floor(corners[index][0][2][1])
            bottomleftX = math.floor(corners[index][0][3][0])
            bottomlextY = math.floor(corners[index][0][3][1])
            midpoint = polylabel([[[topleftX, topleftY], [toprightX, toprightY], [bottomrightX, bottomrightY], [bottomleftX, bottomlextY]]])
            ###### DRAW ID #####
            cv2.putText(frame, "Id: " + str(id), floor_midpoint(midpoint), font, 1, (0,255,0),2,cv2.LINE_AA)
            marker_midpoints.append([math.floor(midpoint[0]), math.floor(midpoint[1])])

        num_of_markers = len(marker_midpoints)
        visual_center_of_markers = (-1, -1)
     
        if num_of_markers == 0:
            pass
        elif num_of_markers == 1:
            visual_center_of_markers = floor_midpoint(marker_midpoints[0])
        elif num_of_markers == 2:
            visual_center_of_markers = floor_midpoint((find_1D_midpoint(marker_midpoints[0][0], marker_midpoints[1][0]), find_1D_midpoint(marker_midpoints[0][1], marker_midpoints[1][1])))
        else: 
            visual_center_of_markers = floor_midpoint(polylabel([marker_midpoints]))
 
        if visual_center_of_markers != (-1, -1):
            cv2.circle(frame, visual_center_of_markers, 30, (255, 0, 0)) 

        #MORE DRAWING
        for r, t in zip(rvec, tvec):
            aruco.drawAxis(frame, mtx, dist, r, t, 0.1) #Draw Axis
        	
        aruco.drawDetectedMarkers(frame, corners) #Draw A square around the markers

    else:
        #print("Markers not found") 
        #print("midpoint X: n, Y: n")
        s.send(b"/n/n/n")



        # Display the resulting frame
    cv2.imshow('frame',frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
