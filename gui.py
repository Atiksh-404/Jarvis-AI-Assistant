import customtkinter as ctk
import threading
import customtkinter as ctk
from main import (wait_for_wake_word, listen_after_wake, processCommand, speak)
import main
import time
from datetime import datetime
from PIL import Image, ImageTk, ImageSequence

# -----------------------------
# Assistant Loop
# -----------------------------

def assistant_loop():

    while True:

        update_status("Ready")

        wait_for_wake_word()

        update_status("Listening")

        command = listen_after_wake()

        if not command:
            continue

        add_message("You", command)

        update_status("Thinking")

        answer = processCommand(command)

        if answer:
            add_message("Jarvis", answer)

        update_status("Ready")

# -----------------------------
# App Settings
# -----------------------------
ctk.set_appearance_mode("dark")       # dark / light
ctk.set_default_color_theme("blue")   # blue / green / dark-blue

# -----------------------------
# Create Window
# -----------------------------
app = ctk.CTk()
app.configure(fg_color="#0B1220")

main_frame = ctk.CTkFrame(
    app,
    fg_color="#111827",
    corner_radius=20
)

main_frame.pack(fill="both", expand=True, padx=20, pady=20)

app.title("Jarvis AI Assistant")
app.state("zoomed")
app.resizable(True, True)


header = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)

header.pack(fill="x", pady=(20,10))

weather_frame = ctk.CTkFrame(
    header,
    width=340,
    height=100,
    corner_radius=20,
    fg_color="#182233",
    border_width=2,
    border_color="#00E5FF"
)

weather_frame.pack(side="right", padx=30)

weather_frame.pack_propagate(False)

weather = ctk.CTkLabel(
    weather_frame,
    text="☀ 31°C\nNoida",
    font=("Segoe UI",20,"bold"),
    justify="left",
    text_color="white"
)


time_frame = ctk.CTkFrame(
    weather_frame,
    fg_color="transparent"
)

clock = ctk.CTkLabel(
    time_frame,
    text="08:34 PM",
    font=("Segoe UI", 18, "bold"),
    text_color="#00E5FF"
)

clock.pack(anchor="e")


time_frame = ctk.CTkFrame(
    weather_frame,
    fg_color="transparent"
)

weather.pack(side="left", padx=20)
time_frame.pack(side="right", padx=20)

date_label = ctk.CTkLabel(
    time_frame,
    text="15 July 2026",
    font=("Segoe UI", 14),
    text_color="#A5B4C7"
)

date_label.pack(anchor="e")

clock = ctk.CTkLabel(
    time_frame,
    text="08:34 PM",
    font=("Segoe UI", 18, "bold"),
    text_color="#00E5FF"
)

clock.pack(anchor="e")

# -----------------------------
# Title
# -----------------------------
# -----------------------------
# Left Header
# -----------------------------
left_header = ctk.CTkFrame(
    header,
    fg_color="transparent"
)

left_header.pack(side="left", padx=30)


title = ctk.CTkLabel(
    left_header,
    text="J.A.R.V.I.S",
    font=("Orbitron", 42, "bold"),
    text_color="#00E5FF"
)

title.pack(anchor="w")


subtitle = ctk.CTkLabel(
    left_header,
    text="Artificial Intelligence Desktop Assistant",
    font=("Segoe UI", 16),
    text_color="#8A8A8A"
)

subtitle.pack(anchor="w", pady=(5,0))


def update_clock():

    now = datetime.now()

    date_label.configure(
        text=now.strftime("%d %b %Y")
    )

    clock.configure(
        text=now.strftime("%I:%M:%S %p")
    )

    app.after(1000, update_clock)


# -----------------------------
# AI CORE FRAME
# -----------------------------
core_frame = ctk.CTkFrame(
    main_frame,
    fg_color="transparent"
)

core_frame.pack(pady=(0, 10))

gif_label = ctk.CTkLabel(
    core_frame,
    text=""
)

gif_label.pack()

gif = Image.open("jarvis_gif.gif")

frames = []

for frame in ImageSequence.Iterator(gif):

    frame = frame.resize((500,400))

    frames.append(ImageTk.PhotoImage(frame))

frame_index = 0

def animate_gif():

    global frame_index

    gif_label.configure(image=frames[frame_index])

    frame_index = (frame_index + 1) % len(frames)

    app.after(40, animate_gif)

pulse = True


separator = ctk.CTkFrame(
    main_frame,
    height=2,
    fg_color="#00E5FF"
)

separator.pack(fill="x", padx=40, pady=20)

# -----------------------------
# Chat Box
# -----------------------------

chat_frame = ctk.CTkFrame(
    main_frame,
    fg_color="#182233",
    corner_radius=25
)

chat_frame.pack(padx=40, fill="both", expand=True, pady=(5, 20))

chat_title = ctk.CTkLabel(
    chat_frame,
    text="💬 Conversation",
    font=("Segoe UI",18,"bold"),
    text_color="#00E5FF"
)

chat_title.pack(anchor="w", padx=20, pady=(15,5))

chatbox = ctk.CTkTextbox(
    main_frame,
    width=1350,
    height=1160,
    corner_radius=0,
    fg_color="#1A2333",
    border_width=2,
    border_color="#00E5FF",
    font=("Segoe UI",17)
)

chatbox.pack(in_=chat_frame,padx=15,pady=15, fill="both", expand=True,)

# -----------------------------
# Status
# -----------------------------

def update_status(state):

    colors = {

        "Ready":"#00FF99",

        "Listening":"#00BFFF",

        "Thinking":"yellow",

        "Speaking":"cyan",

        "Error":"red"

    }

# -----------------------------
# Speak Button
# -----------------------------

# button = ctk.CTkButton(
#     main_frame,
#     text="🎤",
#     width=90,
#     height=90,
#     corner_radius=45,
#     font=("Arial",36),
#     fg_color="#0099FF",
#     hover_color="#00CCFF",
#     border_width=2,
#     border_color="#00E5FF",
#     command=lambda: threading.Thread(target=start_listening).start()
# )

# button.configure(cursor="hand2")



def add_message(sender, message):
    chatbox.configure(state="normal")

    chatbox.insert("end", f"{sender}: {message}\n\n")

    chatbox.see("end")

    chatbox.configure(state="disabled")

# animate_core()
animate_gif()
update_clock()

add_message("Jarvis", "Initializing Jarvis...")
speak("Initializing Jarvis. Systems online. Hello Boss.")

threading.Thread(target=assistant_loop, daemon=True).start()

app.mainloop()