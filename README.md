# DDoS Attack Tool

This program simulates a **DDoS (Distributed Denial of Service)** attack using UDP packets. It leverages the **Tkinter** graphical interface to configure the target IP, port, and the number of threads used for the attack.

⚠️ **Warning:** Only use this script on servers where you have explicit permission. DDoS attacks are illegal and can cause significant damage to infrastructure. Use this tool solely for educational purposes or for testing your own systems legally.

## Features

- **Tkinter Graphical Interface:** Allows you to define the target IP, port, and the number of threads.
- **UDP Packet Sending:** Uses the **UDP** protocol to send packets to the specified target address.
- **Real-time Tracking:** Displays the number of requests sent in real-time on the interface.

## Prerequisites

- Python 3.x
- Tkinter (usually bundled with Python)
- `socket` library (bundled with Python)
- `threading` library (bundled with Python)

## Installation

Clone the repository to your local machine:

```bash
git clone https://github.com/MaybeAnge/ddos-attack.git
cd ddos-attack
