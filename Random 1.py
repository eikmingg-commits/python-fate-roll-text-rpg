import time
import random  

def type_text(text):
    for char in text:
        print(char, end='', flush=True)
        time.sleep(0.04)
    print()  # auto new line

def thinking_dots(cycles=3, delay=0.4):
    for _ in range(cycles):
        for dots in [".", "..", "..."]:
            print(dots, end="\r", flush=True)
            time.sleep(delay)
    print("   ", end="\r")  # clear line

def type_with_thinking_dots(text, cycles=3, delay=0.4):
    print(text, end="", flush=True)
    for _ in range(cycles):
        for dots in [".", "..", "..."]:
            print("\r" + text + dots + "   ", end="", flush=True)
            time.sleep(delay)
    print("\r" + text + "...")  # finish clean


type_text("The Entity appears before you...")
time.sleep(2)

type_text("Rolling your fate")
thinking_dots(3, 0.2)
time.sleep(.5)

roll = random.randint(1, 100)
type_text(f"You rolled a {roll}!")

if roll == 100:
    time.sleep(1)
    type_text("The Entity pulls strings from your mind and snaps them.")
    type_with_thinking_dots("it is not death yet", 3, 0.3)
    thinking_dots(3, 0.1)
    type_text("you are not alive either.")
elif roll <= 3:
    time.sleep(1)
    type_text("Death by the Soft Whisper of the Void. ")

elif roll >= 50:     
    time.sleep(1)
    type_text("The threads of fate remain calm...")

else:
    time.sleep(1)
    type_text("A rare event occurs! You have a JOB!!!")
