import cv2
import mediapipe as mp
import time
import pyautogui

pyautogui.FAILSAFE = False

# Keys
break_key = 'left'
accelerator_key = 'right'

# Wait before starting
time.sleep(2.0)
current_key_pressed = set()

# Mediapipe hands
mp_hands = mp.solutions.hands
mp_drawing = mp.solutions.drawing_utils
tipIds = [4, 8, 12, 16, 20]

# Start video capture
video = cv2.VideoCapture(0)

with mp_hands.Hands(min_detection_confidence=0.5,
                    min_tracking_confidence=0.5) as hands:
    while True:
        keyPressed = False
        key_count = 0
        key_pressed = 0

        ret, image = video.read()
        if not ret:
            break

        # Convert to RGB for Mediapipe
        image_rgb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
        image_rgb.flags.writeable = False
        results = hands.process(image_rgb)
        image_rgb.flags.writeable = True
        image = cv2.cvtColor(image_rgb, cv2.COLOR_RGB2BGR)

        lmList = []

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                for id, lm in enumerate(hand_landmarks.landmark):
                    h, w, c = image.shape
                    cx, cy = int(lm.x * w), int(lm.y * h)
                    lmList.append([id, cx, cy])
                mp_drawing.draw_landmarks(image, hand_landmarks, mp_hands.HAND_CONNECTIONS)

        fingers = []
        if lmList:
            # Thumb
            if lmList[tipIds[0]][1] > lmList[tipIds[0]-1][1]:
                fingers.append(1)
            else:
                fingers.append(0)
            # Other fingers
            for id in range(1, 5):
                if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                    fingers.append(1)
                else:
                    fingers.append(0)

            total = fingers.count(1)

            if total == 0:
                # Brake
                cv2.rectangle(image, (20, 300), (270, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "BRAKE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
                if break_key not in current_key_pressed:
                    pyautogui.keyDown(break_key)
                key_pressed = break_key
                keyPressed = True
                current_key_pressed.add(break_key)
                key_count += 1

            elif total == 5:
                # Accelerate
                cv2.rectangle(image, (20, 300), (470, 425), (0, 255, 0), cv2.FILLED)
                cv2.putText(image, "ACCELERATE", (45, 375), cv2.FONT_HERSHEY_SIMPLEX,
                            2, (255, 0, 0), 5)
                if accelerator_key not in current_key_pressed:
                    pyautogui.keyDown(accelerator_key)
                key_pressed = accelerator_key
                keyPressed = True
                current_key_pressed.add(accelerator_key)
                key_count += 1

        # Release keys if none pressed
        if not keyPressed and current_key_pressed:
            for key in current_key_pressed:
                pyautogui.keyUp(key)
            current_key_pressed.clear()
        elif key_count == 1 and len(current_key_pressed) == 2:
            for key in current_key_pressed:
                if key != key_pressed:
                    pyautogui.keyUp(key)
            current_key_pressed = {key_pressed}

        # Display
        cv2.imshow("Gesture Control Frame", image)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

video.release()
cv2.destroyAllWindows()