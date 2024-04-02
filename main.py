### IMPORT DEPENDENCIES

import cv2
import mediapipe as mp
import numpy as np
import time
import functions
import settings

mp_drawing = mp.solutions.drawing_utils
mp_pose = mp.solutions.pose


### MAKE DETECTIONS

cap = cv2.VideoCapture(0) # if there are errors due to the video stream, modify this value

# variable counter
counter = 0
stage = None



## Setup mediapipe instance
with mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5) as pose:
    while cap.isOpened():
        ret, frame = cap.read()
        
        # recolor image into RGB
        image = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image.flags.writeable = False
        
        # detection
        results = pose.process(image)
        
        # recolor image back to BGR
        image.flags.writeable = True
        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
        
        # extract landmarks
        try :
            landmarks = results.pose_landmarks.landmark
            
            # get coordinates
            left_shoulder = [landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.LEFT_SHOULDER.value].y]
            left_elbow = [landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.LEFT_ELBOW.value].y]
            left_wrist = [landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.LEFT_WRIST.value].y]
            
            right_shoulder = [landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_SHOULDER.value].y]
            right_elbow = [landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_ELBOW.value].y]
            right_wrist = [landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].x,landmarks[mp_pose.PoseLandmark.RIGHT_WRIST.value].y]
            
            # calculate angle
            left_elbow_angle = round(functions.calculate_angle(left_shoulder,left_elbow,left_wrist))
            left_shoulder_angle = round(functions.calculate_angle(right_shoulder,left_shoulder,left_elbow))

            right_elbow_angle = round(functions.calculate_angle(right_shoulder,right_elbow,right_wrist))
            right_shoulder_angle = round(functions.calculate_angle(left_shoulder,right_shoulder,right_elbow))           
            
            # visualize angle
            cv2.putText(image,str(left_elbow_angle),
                         tuple(np.multiply(left_elbow, [640,480]).astype(int)), 
                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA
                         )
            cv2.putText(image,str(left_shoulder_angle),
                         tuple(np.multiply(left_shoulder, [640,480]).astype(int)), 
                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA
                         )
            
            cv2.putText(image,str(right_elbow_angle),
                         tuple(np.multiply(right_elbow, [640,480]).astype(int)), 
                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA
                         )
            cv2.putText(image,str(right_shoulder_angle),
                         tuple(np.multiply(right_shoulder, [640,480]).astype(int)), 
                         cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 2, cv2.LINE_AA
                         )


         
            print('time :',time.time())

            
            # Counter logic
            if left_elbow_angle > 160:
                stage = "down"
            if left_elbow_angle < 30 and stage == 'down':
                stage = 'up'
                counter +=1

        except :
            pass
        
        # render counter
        # setup the box
        cv2.rectangle(image, (0,0), (225,73), (245,117,16), -1)
        
        # data
        cv2.putText(image, 'REPS', (15,12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, str(counter), (10,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        # stage
        cv2.putText(image, 'STAGE', (65,12),
                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0,0,0), 1, cv2.LINE_AA)
        cv2.putText(image, stage, (60,60),
                    cv2.FONT_HERSHEY_SIMPLEX, 2, (255,255,255), 2, cv2.LINE_AA)
        
        
        # render detection
        mp_drawing.draw_landmarks(image, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                                  mp_drawing.DrawingSpec(color=(245,117,66), thickness = 2, circle_radius = 2),
                                  mp_drawing.DrawingSpec(color=(245,66,230), thickness = 2, circle_radius = 2)
                                  )
        
        cv2.imshow('Mediapipe Feed', image)
    
        if cv2.waitKey(10) & 0xFF == ord('q'): # press 'q' to end the video capture 
            break
    
    cap.release()
    cv2.destroyAllWindows()





##choses à faire pour le 22 Avril
##- définir l alphabet
##- la fonction Code 
##- afficher l image après code bon