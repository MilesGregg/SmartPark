import cv2
import csv

import numpy as np


class SpotGenerator:
    def __init__(self, color, image):
        self.id = 0
        self.color = color
        self.mouse_clicks = 0
        self.image_cap = image
        self.image_copy = cv2.imread(image).copy()
        self.spots = []

        cv2.namedWindow(self.image_cap, cv2.WINDOW_GUI_EXPANDED)
        cv2.setMouseCallback(self.image_cap, self.mouse_listener)

    def generate_spots(self):
        while True:
            cv2.imshow(self.image_cap, self.image_copy)
            keyboard = cv2.waitKey(0) & 0xFF
            if keyboard == ord('r'):
                self.spots = []
            elif keyboard == ord('e'):
                cv2.destroyWindow(self.image_cap)
                break

    def mouse_listener(self, event, x, y, flags, param):
        if event == cv2.EVENT_LBUTTONDOWN:
            self.spots.append((x, y))
            self.mouse_clicks += 1
            if self.mouse_clicks >= 4:
                self.finish_spot()
            if self.mouse_clicks > 1:
                cv2.line(self.image_copy, self.spots[-2], self.spots[-1], (0, 255, 0), 1)

            print("Pressed at: " + str((x, y)))

        cv2.imshow(self.image_cap, self.image_copy)

    def finish_spot(self):
        cv2.line(self.image_copy, self.spots[2], self.spots[3], self.color, 1)
        cv2.line(self.image_copy, self.spots[3], self.spots[0], self.color, 1)

        with open('data/spots.csv', 'w', encoding='UTF8') as f:
            writer = csv.writer(f)
            writer.writerow(self.spots)

        self.draw_contours(self.image_copy, np.array(self.spots), str(self.id + 1), (255, 255, 255))

        self.mouse_clicks = 0
        self.spots = []
        self.id += 1

    @staticmethod
    def draw_contours(image,
                      coordinates,
                      label,
                      font_color,
                      border_color=(0, 255, 0),
                      line_thickness=1,
                      font=cv2.FONT_HERSHEY_SIMPLEX,
                      font_scale=0.5):
        cv2.drawContours(image,
                         [coordinates],
                         contourIdx=-1,
                         color=border_color,
                         thickness=2,
                         lineType=cv2.LINE_8)
        moments = cv2.moments(coordinates)

        center = (int(moments["m10"] / moments["m00"]) - 3,
                  int(moments["m01"] / moments["m00"]) + 3)

        cv2.putText(image,
                    label,
                    center,
                    font,
                    font_scale,
                    font_color,
                    line_thickness,
                    cv2.LINE_AA)
