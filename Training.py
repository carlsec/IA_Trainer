import cv2
import math
import numpy as np


class Training:
    """
    Classe com os metodos de cada treino.
    """
    def __init__(self, lmList):
        self.lmList = lmList

    def screwThread(self, img, draw=True):
        x1, y1 = self.lmList[12][1:]
        x2, y2 = self.lmList[14][1:]
        x3, y3 = self.lmList[22][1:]
        x4, y4 = self.lmList[21][1:]
        x5, y5 = self.lmList[13][1:]
        x6, y6 = self.lmList[11][1:]

        angle1 = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                              math.atan2(y1 - y2, x1 - x2))
        angle2 = math.degrees(math.atan2(y6 - y5, x6 - x5) -
                              math.atan2(y4 - y5, x4 - x5))

        if angle1 < 0:
            angle1 += 360

        if angle2 < 0:
            angle2 += 360

        if draw:
            #cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            #cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            #cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
            #cv2.circle(img, (x1, y1), 15, (255, 0, 0), 2)
            cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 0), 2)
            cv2.circle(img, (x3, y3), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (255, 0, 0), 2)
            cv2.putText(img, str(int(angle1)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

            #cv2.line(img, (x4, y4), (x5, y5), (255, 255, 255), 3)
            #cv2.line(img, (x6, y6), (x5, y5), (255, 255, 255), 3)
            cv2.circle(img, (x4, y4), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x4, y4), 15, (255, 0, 0), 2)
            cv2.circle(img, (x5, y5), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x5, y5), 15, (255, 0, 0), 2)
            #cv2.circle(img, (x6, y6), 10, (255, 0, 0), cv2.FILLED)
            #cv2.circle(img, (x6, y6), 15, (255, 0, 0), 2)
            cv2.putText(img, str(int(angle2)), (x5 - 50, y5 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        # Interpolaçao linear
        per_1 = np.interp(angle1, (210, 310), (0, 100))
        bar_1 = np.interp(angle1, (210, 310), (990, 280))

        per_2 = np.interp(angle2, (210, 310), (0, 100))
        bar_2 = np.interp(angle2, (210, 310), (990, 280))

        per = (per_1 + per_2) / 2
        bar = (bar_1 + bar_2) / 2

        return per, bar

    def benchPress(self, img, draw=True):
        # Get the landmarks
        x1, y1 = self.lmList[8][1:]
        x2, y2 = self.lmList[12][1:]
        x3, y3 = self.lmList[14][1:]
        x4, y4 = self.lmList[13][1:]
        x5, y5 = self.lmList[11][1:]
        x6, y6 = self.lmList[7][1:]

        angle1 = math.degrees(math.atan2(y3 - y2, x3 - x2) -
                              math.atan2(y1 - y2, x1 - x2))
        angle2 = math.degrees(math.atan2(y6 - y5, x6 - x5) -
                              math.atan2(y4 - y5, x4 - x5))

        if angle1 < 0:
            angle1 += 360

        if angle2 < 0:
            angle2 += 360

        if draw:
            #cv2.line(img, (x1, y1), (x2, y2), (255, 255, 255), 3)
            #cv2.line(img, (x3, y3), (x2, y2), (255, 255, 255), 3)
            #cv2.circle(img, (x1, y1), 10, (255, 0, 0), cv2.FILLED)
            #cv2.circle(img, (x1, y1), 15, (255, 0, 0), 2)
            cv2.circle(img, (x2, y2), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x2, y2), 15, (255, 0, 0), 2)
            cv2.circle(img, (x3, y3), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x3, y3), 15, (255, 0, 0), 2)
            cv2.putText(img, str(int(angle1)), (x2 - 50, y2 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

            #cv2.line(img, (x4, y4), (x5, y5), (255, 255, 255), 3)
            #cv2.line(img, (x6, y6), (x5, y5), (255, 255, 255), 3)
            cv2.circle(img, (x4, y4), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x4, y4), 15, (255, 0, 0), 2)
            cv2.circle(img, (x5, y5), 10, (255, 0, 0), cv2.FILLED)
            cv2.circle(img, (x5, y5), 15, (255, 0, 0), 2)
            #cv2.circle(img, (x6, y6), 10, (255, 0, 0), cv2.FILLED)
            #cv2.circle(img, (x6, y6), 15, (255, 0, 0), 2)
            cv2.putText(img, str(int(angle2)), (x5 - 50, y5 + 50), cv2.FONT_HERSHEY_PLAIN, 2, (255, 0, 0), 2)

        # Interpolaçao linear
        per_1 = np.interp(angle1, (220, 250), (0, 100))
        bar_1 = np.interp(angle1, (220, 250), (990, 280))

        per_2 = np.interp(angle2, (220, 250), (0, 100))
        bar_2 = np.interp(angle2, (220, 250), (990, 280))

        per = (per_1 + per_2) / 2
        bar = (bar_1 + bar_2) / 2

        return per, bar
