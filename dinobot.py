import pyautogui
import time
import keyboard

time.sleep(3)

# Add more coordinates as needed
spot_coords = [
    (521, 700), (540, 690), (560, 680),
    (400, 670), (408, 660), (416, 650), (424, 640), (432, 630), (440, 620),
    (448, 610), (456, 600), (464, 590), (472, 580), (480, 570), (488, 560),
    (496, 550), (504, 540), (512, 530), (520, 530), (528, 530), (536, 530)
]

space_pressed = False  # track if spacebar has been pressed

while True:
    ss = pyautogui.screenshot()

    # Check the color of each spot
    for spot in spot_coords:
        pixel_color = ss.getpixel(spot)
        print(pixel_color)
        if pixel_color[0] == 83 and not space_pressed:
            pyautogui.press('space')
            space_pressed = True  # Set the flag to True after pressing spacebar
            time.sleep(0.00001)
            break
        else:
            space_pressed = False  # Reset the flag if spacebar is not pressed

    if keyboard.is_pressed("q"):
        break
