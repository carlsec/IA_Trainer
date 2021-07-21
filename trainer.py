import cv2
import time
import AITrainer as at
import argparse

count = 0
dir = 0
pTime = 0
last_take = time.time() + 10
seri_count = 1
se_time = 1
last_serie = 0
trainer = at.AITrainer()
time.sleep(0.3)

# Create the parser and add arguments
parser = argparse.ArgumentParser()
parser.add_argument('ex', choices=['0', '1'], default='0')
parser.add_argument('--serie', help="Quantidade de Series", type=float, default=4, required=False)
parser.add_argument('--repe', help="Quantidade de Repeticoes", type=float, default=10, required=False)
parser.add_argument('--tempo', help="Tempo de descanso entre as series", type=float, default=30, required=False)
parser.add_argument('--imagem', help="Imagem de entrada - Webcam ou Path do video", type=float, default=1,
                    required=False)

args = parser.parse_args()
try:
    cap = cv2.VideoCapture(int(args.imagem))
except:
    cap = cv2.VideoCapture(str(args.imagem))

while True:
    time_stop = time.time()
    success, image, = cap.read()
    image = cv2.resize(image, (1200, 720))
    image = trainer.mPose(image, False)

    if last_serie < time_stop:
        lmList = trainer.mpPosition(image, False)
        if len(lmList) == 0:
            lmList = None
    else:
        cv2.putText(image, str(f'Aguarde {se_time} - Segundos para a proxima serie'), (50, 150),
                    cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
        time.sleep(1)
        se_time = se_time - 1
        lmList = None

    if lmList is not None:
        per, bar = trainer.train(image, args.ex, draw=True)

        color = (255, 0, 0)
        if per == 100:
            last_take = time.time() + 5
            color = (0, 255, 0)
            if dir == 0:
                count += 0.5
                dir = 1
        if per == 0:
            color = (0, 0, 255)
            if dir == 1:
                count += 0.5
                dir = 0

        if time_stop > last_take:
            cv2.putText(image, str("EXECUCAO INCORRETA"), (100, 670), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        cv2.rectangle(image, (280, 100), (990, 7), color, 3)
        cv2.rectangle(image, (int(bar), 100), (990, 7), color, cv2.FILLED)
        cv2.putText(image, f'{int(per)}%', (1000, 75), cv2.FONT_HERSHEY_SIMPLEX, 2, color, 2)

        # cv2.rectangle(img, (0, 450), (250, 720), (0, 255, 0), cv2.FILLED)
        cv2.putText(image, 'Repeticoes: ' + str(int(count)) + '/' + str(int(args.repe)), (13, 160),cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)
        cv2.putText(image, 'Serie: ' + str(int(seri_count)), (13, 100), cv2.FONT_HERSHEY_SIMPLEX, 2, (255, 0, 0), 2)

    if count == args.repe:
        count = 0
        se_time = args.tempo
        last_serie = time.time() + se_time
        last_take = time.time() + se_time + 5
        seri_count += 1

    if args.serie < seri_count:
        cv2.putText(image, str('Treino Finalizado'), (100, 670), cv2.FONT_HERSHEY_PLAIN, 1, (255, 0, 0), 2)
        time.sleep(2)
        break

    cTime = time.time()
    fps = 1 / (cTime - pTime)
    pTime = cTime
    cv2.putText(image, 'FPS' + str(int(fps)), (15, 20), cv2.FONT_HERSHEY_PLAIN, 2,
                (255, 0, 0), 1)

    cv2.imshow("image", image)
    cv2.waitKey(1)
