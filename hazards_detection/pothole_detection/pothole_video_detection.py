import msvcrt
import os
import time

import cv2 as cv
import geocoder

from geolocation.gps_mock import LocationMock
from utils.consts import HAZARD_TYPE, RESULT_PATH, PROJ_FILE_PATH


def analyze_potholes_video(video_path: str = 0):
    gps_mock = LocationMock()
    results = []
    # reading label name from obj.names file
    class_name = []
    with open(os.path.join(PROJ_FILE_PATH, 'obj.names'), 'r') as f:
        class_name = [cname.strip() for cname in f.readlines()]

    # importing model weights and config file
    # defining the model parameters
    net1 = cv.dnn.readNet(PROJ_FILE_PATH + '/yolov4_tiny.weights', PROJ_FILE_PATH + '/yolov4_tiny.cfg')
    net1.setPreferableBackend(cv.dnn.DNN_BACKEND_CUDA)
    net1.setPreferableTarget(cv.dnn.DNN_TARGET_CUDA_FP16)
    model1 = cv.dnn_DetectionModel(net1)
    model1.setInputParams(size=(640, 480), scale=1 / 255, swapRB=True)

    # defining the video source (0 for camera or file name for video)
    cap = cv.VideoCapture(
        video_path)
    width = cap.get(3)
    height = cap.get(4)
    result = cv.VideoWriter('result.avi',
                            cv.VideoWriter_fourcc(*'MJPG'),
                            10, (int(width), int(height)))

    # defining parameters for result saving and get coordinates
    # defining initial values for some parameters in the script
    g = geocoder.ip('me')
    starting_time = time.time()
    Conf_threshold = 0.5
    NMS_threshold = 0.4
    frame_counter = 0
    i = 0
    b = 0
    # print("press q to stop:\n")
    # detection loop
    while True:
        if msvcrt.kbhit():
            key = msvcrt.getch()
            if key == 'q':
                break
        ret, frame = cap.read()
        frame_counter += 1
        if ret is False:
            break
        # analysis the stream with detection model
        classes, scores, boxes = model1.detect(frame, Conf_threshold, NMS_threshold)
        for (classid, score, box) in zip(classes, scores, boxes):
            label = "pothole"
            x, y, w, h = box
            recarea = w * h
            area = width * height
            # drawing detection boxes on frame for detected potholes and saving coordinates txt and photo
            if (len(scores) != 0 and scores[0] >= 0.7):
                if ((recarea / area) <= 0.1 and box[1] < 600):
                    cv.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 1)
                    cv.putText(frame, "%" + str(round(scores[0] * 100, 2)) + " " + label, (box[0], box[1] - 10),
                               cv.FONT_HERSHEY_COMPLEX, 0.5, (255, 0, 0), 1)
                    if (i == 0):
                        photo_path = os.path.join(RESULT_PATH, HAZARD_TYPE + str(i) + '.jpg')
                        cv.imwrite(photo_path, frame)
                        # coordinates = g.latlng
                        coordinates = gps_mock.location_mock()

                        results.append((photo_path, coordinates, HAZARD_TYPE))
                        coordinates = str(g.latlng)
                        with open(os.path.join(RESULT_PATH, HAZARD_TYPE + str(i) + '.txt'), 'w') as f:
                            f.write(coordinates)
                            i = i + 1
                    if (i != 0):
                        if ((time.time() - b) >= 2):
                            photo_path = os.path.join(RESULT_PATH, HAZARD_TYPE + str(i) + '.jpg')
                            cv.imwrite(photo_path, frame)
                            # coordinates = g.latlng
                            coordinates = gps_mock.location_mock()
                            results.append((photo_path, coordinates, HAZARD_TYPE))
                            coordinates = str(g.latlng)
                            with open(os.path.join(RESULT_PATH, HAZARD_TYPE + str(i) + '.txt'), 'w') as f:
                                f.write(coordinates)
                                i = i + 1
        # writing fps on frame
        endingTime = time.time() - starting_time
        fps = frame_counter / endingTime
        cv.putText(frame, f'FPS: {fps}', (20, 50),
                   cv.FONT_HERSHEY_COMPLEX, 0.7, (0, 255, 0), 2)
        # showing and saving result
        # cv.imshow('frame', frame)
        result.write(frame)
        key = cv.waitKey(1)
        if key == ord('q'):
            break

    # end
    cap.release()
    result.release()
    cv.destroyAllWindows()
    return results


if __name__ == "__main__":
    pass
