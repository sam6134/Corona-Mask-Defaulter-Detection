import cv2
import os
# Importing necessary files
cascPath = 'haarcascade_frontalface_dataset.xml'
faceCascade = cv2.CascadeClassifier(cascPath)
# making a cascade classfier to detect faces



# start video capturing
video_capture = cv2.VideoCapture(0)

def camera_stream():
    # varibale to process alternate frames
    process_this_frame = True
    while True:
        ret, frame = video_capture.read()
        # scale the frame for achieving faster processing thus higher fps
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        rgb_small_frame = small_frame[:, :, ::-1]

        if process_this_frame:
            # get valid face locations if a defaulter is found or uncovered face is found
            gray = cv2.cvtColor(rgb_small_frame, cv2.COLOR_BGR2GRAY)
            face_locations = faceCascade.detectMultiScale(
                gray,
                minNeighbors=5,
                minSize=(30, 30),
                flags=cv2.CASCADE_SCALE_IMAGE)

         # Make the next frame as non processable

        process_this_frame = not process_this_frame

        face_found=False
        for (x, y, w, h) in face_locations:
            # rescale the face locations
            face_found = True
            x *= 4
            y *= 4
            w *= 4
            h *= 4

            # draw bounding box around defaulters
            cv2.rectangle(frame, (x, y+h), (x+w, y), (0, 0, 255), 2)
            # draw text box
            cv2.rectangle(frame, (x, y - 35), (x+w, y), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            # put text inside the box
            cv2.putText(frame, "Alert!!", (x + 6, y - 6), font, 1.0, (255, 255, 255), 1)

         # if no defaulters are found
        if(face_found== False):
            # draw green box to show ok status
            frame = cv2.rectangle(frame, (50, 50), (1200, 650), (0, 255, 0), 3)
            cv2.rectangle(frame, (50, 650 - 35), (1200, 650), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, "No Defaulters Found!", (50, 650 - 6), font, 1.0, (0, 255, 0), 1)

        # return frame to the calling function
        return cv2.imencode('.jpg', frame)[1].tobytes()
