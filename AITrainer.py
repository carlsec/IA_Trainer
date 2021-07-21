import cv2
import mediapipe as mp
import time
import math
import numpy as np
import Training as tr


class AITrainer:
    """
    Classe para inicializar Mediapipe Pose object.

    Veja detalhes: https://google.github.io/mediapipe/solutions/pose
    """

    def __init__(self, static_image_model=False, model_complexity=False, smooth_landmarks=True,
                 min_detection_confidence=0.5, min_tracking_confidence=0.5):
        """
        Metodo principal da Classe..

        :param static_image_model: Se definido como false a solucao trata as imagens de entrada como streming de video,
        para imagens estaticas usar True. - Default: False
        :param model_complexity: Complexidade da pose. - Default: 1
        :param smooth_landmarks: Filtros de solucao para reduzir o jiter, ignorado se static_image_model estiver
        definido como True. Default: True
        :param min_detection_confidence: A confiança minima para detectar a pose. Default: 0.5
        :param min_tracking_confidence: A confiança minima para fazer o rastreamento da deteccao. Default: 0.5
        """
        self.static_image_model = static_image_model
        self.model_complexity = model_complexity
        self.smooth_landmarks = smooth_landmarks
        self.min_detection_confidence = min_detection_confidence
        self.min_tracking_confidence = min_tracking_confidence
        self.mp_drawing = mp.solutions.drawing_utils
        self.mp_pose = mp.solutions.pose
        self.pose = self.mp_pose.Pose(self.static_image_model, self.model_complexity, self.smooth_landmarks,
                                      self.min_detection_confidence, self.min_tracking_confidence)
        
    def mPose(self, image, draw=True):
        """
        Metodo que processa uma imagem em RGB e retorna as poses landmarks.
        """
        img_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        self.results = self.pose.process(img_rgb)
        if self.results.pose_landmarks:
            if draw:
                self.mp_drawing.draw_landmarks(image, self.results.pose_landmarks, self.mp_pose.POSE_CONNECTIONS)
        return image

    def mpPosition(self, image, draw=True):
        """
        Metodo para encontrar as posicoes da deteccao.

        :param image: Imagem de entrada
        :param draw: Para desenhar defina True, False para nao desenhar.
        :return: Imagem e as coordenadas das posicoes
        """
        self.lmList = []
        if self.results.pose_landmarks:
            for id, lm in enumerate(self.results.pose_landmarks.landmark):
                h, w, c = image.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                self.lmList.append([id, cx, cy])
                if draw:
                    cv2.circle(image, (cx, cy), 5, (255, 0, 0), cv2.FILLED)
        return self.lmList


    def train(self, image, ex, draw=True):
        """
        :param image: Imagem
        :param ex: Treino escolhido
        :param draw: Se True faz o desenho dos pontos na imagem
        :return: retorna a intepolaçao linear dos angulos.
        """

        train = tr.Training(self.lmList)
        if ex == '0':
            per, bar = train.screwThread(image, True)

        elif ex == '1':
            per, bar = train.benchPress(image, True)

        return per, bar


def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    trainer = AITrainer()
    while True:
        success, image = cap.read()
        image = trainer.mPose(image, True)
        lmList = trainer.mpPosition(image, True)
        if len(lmList) != 0:
            cv2.circle(image, (lmList[14][1], lmList[14][2]), 15, (0, 0, 255), cv2.FILLED)

        cTime = time.time()
        fps = 1 / (cTime - pTime)
        pTime = cTime

        cv2.putText(image, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 0, 0), 3)

        cv2.imshow("Image", image)
        cv2.waitKey(1)


if __name__ == "__main__":
    main()
