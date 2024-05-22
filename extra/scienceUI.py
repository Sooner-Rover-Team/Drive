import socket
import matplotlib.pyplot as plt
from collections import deque
from datetime import datetime
import select

# Set the IP address and port to bind the UDP server
# SELF_IP = "192.168.1.3"  # Your local IP address
SELF_PORT = 5969

# Create a UDP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sensor_values = [69,69,69,69]
# Bind the socket to the specified IP address and port
sock.bind(('0.0.0.0', SELF_PORT))

print(f"UDP server listening on port {SELF_PORT}")

# Initialize variables for peak detection
peak_threshold = 10  # Adjust as needed
peaks = []

# Initialize the plots
plt.ion()  # Turn on interactive mode
fig, axs = plt.subplots(3, 1, figsize=(10, 10))
plt.subplots_adjust(hspace=0.5)


# Initialize deque buffers for each plot
buffers = [deque(maxlen=20) for _ in range(3)]
lines = []
labels = ['Temperature (F)', 'Humidity (%)', 'Methane (ppm)']
# 82 - 94 F in Utah day time temp
ylims = [(50, 100), (0, 100), (0, 1023)]
# Initialize plots
for i, ax in enumerate(axs):
    line, = ax.plot([], [], marker='o', linestyle='-', label=f'Sensor {i+1}')
    ax.set_xlabel('Time (s)')
    ax.set_ylabel(f'{labels[i]}')
    ax.set_title(f'Live {labels[i]} Sensor  Plot')
    ax.set_ylim(ylims[i][0], ylims[i][1])  # Assuming sensor readings are in the range 0-1023
    ax.legend(loc='upper left')
    lines.append(line)

# Update the plots with new data
def update_plots(x, ys):
    for i, y in enumerate(ys):
        buffers[i].append(y)
        lines[i].set_xdata(range(1, len(buffers[i]) + 1))  # Use a continuous range for x-axis
        lines[i].set_ydata(buffers[i])
        axs[i].relim()
        axs[i].autoscale_view()
    fig.canvas.flush_events()

while True:
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    sock.bind(('0.0.0.0', SELF_PORT))
    msg = sock.recv(4096)
    sensor_values = msg
    # print(sensor_values)

    sensor_values = [(9/5) * sensor_values[0] + 32, sensor_values[1], (sensor_values[2] * 256 + sensor_values[3]) - 190]
    sensor_values[0] = float(str(round(sensor_values[0], 2)))
    if sensor_values[2] < 0: 
        sensor_values[2] = 0
    print(f"Received message: {sensor_values}")
    update_plots(len(buffers[0]) + 1, sensor_values)  # Increment the x-axis index

    # Check for peaks
    if max(sensor_values) > peak_threshold:
        peaks.append((datetime.now(), i + 1, sensor_values))  # Store timestamp, sensor index, and value of peak
