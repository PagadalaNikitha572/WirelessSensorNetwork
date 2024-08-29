n, d = map(int, input().split())
sensors = {}
for i in range(1, n + 1):
    x, y = map(int, input().split())
    sensors[i] = [x, y]

def communicating_sensors(sensors, d, n):
    communicable_sensors = []
    for i in range(1, n):
        set_sensors = []
        for j in range(i + 1, n + 1):
            [x1, y1] = sensors[i]
            [x2, y2] = sensors[j]
            distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
            if distance <= d:
                if i in set_sensors:
                    set_sensors.append(j)
                else:
                    set_sensors.append(i)
                    set_sensors.append(j)
        communicable_sensors.append(set_sensors)

    max_size = 0
    max_sensor = []
    for i in communicable_sensors:
        length = len(i)
        if length > max_size:
            max_size = length
            max_sensor = i
    print(max_size)
    print(max_sensor)

communicating_sensors(sensors, d, n)

# GUI code
import tkinter as tk
import matplotlib.pyplot as plt
from tkinter import *

window = Tk()
window.geometry("1600x800")

# Load the background image using PhotoImage
background_image = PhotoImage(file=f"C:\\Users\\nikitha\\Downloads\\wireless sensor network.png")

# Create a label with the background image
background_label = Label(window, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

label_1 = Label(window, text="WIRELESS SENSOR NETWORK")
font_tuple = ("comic sans ms", 50, "bold")
label_1.config(font=font_tuple)
label_1.pack()

def communicating_sensors(sensors, d, n):
    communicable_sensors = []
    for i in range(1, n):
        set_sensors = []
        for j in range(i + 1, n + 1):
            x1, y1 = sensors[i]
            x2, y2 = sensors[j]
            distance = ((y2 - y1) ** 2 + (x2 - x1) ** 2) ** 0.5
            if distance <= d:
                if i in set_sensors:
                    set_sensors.append(j)
                else:
                    set_sensors.append(i)
                    set_sensors.append(j)
        communicable_sensors.append(set_sensors)

    max_size = 0
    max_sensor = []
    for i in communicable_sensors:
        length = len(i)
        if length > max_size:
            max_size = length
            max_sensor = i
    return max_size, max_sensor

def plot_graph(sensors):
    x_values = [sensor[0] for sensor in sensors.values()]
    y_values = [sensor[1] for sensor in sensors.values()]
    plt.scatter(x_values, y_values, color='red', label='Sensors')
    plt.xlabel('X-coordinate')
    plt.ylabel('Y-coordinate')
    plt.title('Sensor Coordinates')
    plt.grid(True)
    plt.legend()
    plt.show()

def input_window():
    # Create the main GUI window
    root = Toplevel(window)
    root.title("Sensor Communication")
    root.geometry('1600x800')
    root.configure(bg='lightblue')

    label_n = tk.Label(root, text="Enter the number of sensors (n):", bg='lightblue')
    font_tuple = ("comic Sans MS", 20, "bold")
    label_n.configure(font=font_tuple)
    label_n.grid(row=0, column=0, padx=5, pady=5)
    entry_n = tk.Entry(root)
    entry_n.grid(row=0, column=1, padx=5, pady=5)

    label_d = tk.Label(root, text="Enter the communication distance (d):", bg='lightblue')
    label_d.configure(font=font_tuple)
    label_d.grid(row=1, column=0, padx=5, pady=5)
    entry_d = tk.Entry(root)
    entry_d.grid(row=1, column=1, padx=5, pady=5)

    label_sensors = tk.Label(root, text="Enter sensor coordinates (x y) separated by space:", bg='lightblue')
    label_sensors.configure(font=font_tuple)
    label_sensors.grid(row=2, column=0, padx=5, pady=5)
    entries_sensors = {}
    max_sensors = 5
    for i in range(max_sensors):
        label_sensor_i = tk.Label(root, text=f"Sensor {i + 1}:", bg='lightblue')
        label_sensor_i.configure(font=font_tuple)
        label_sensor_i.grid(row=i + 3, column=0, padx=5, pady=5)
        entry_sensor_i = tk.Entry(root)
        entry_sensor_i.grid(row=i + 3, column=1, padx=5, pady=5)
        entries_sensors[i + 1] = entry_sensor_i

    def result_window():
        result_window = Toplevel(root)
        result_window.geometry('1600x800')
        result_window.configure(bg="lightgreen")

        n = int(entry_n.get())
        d = int(entry_d.get())
        sensors = {}
        for i in range(1, n + 1):
            x, y = map(int, entries_sensors[i].get().split())
            sensors[i] = [x, y]

        max_size, max_sensor = communicating_sensors(sensors, d, n)
        result_label = Label(result_window, text=f"RESULT \n\n Max Size: {max_size}\nMax Sensor: {max_sensor}",
                             bg="lightgreen", font=("arial", 40, "bold"))
        result_label.pack()

        exit_button = tk.Button(result_window, text="EXIT", height=1, width=10, font=("arial", 10, "bold"),
                                command=window.destroy)
        exit_button.place(x=700, y=400)

    def graph_window():
        n = int(entry_n.get())
        d = int(entry_d.get())
        sensors = {}
        for i in range(1, n + 1):
            x, y = map(int, entries_sensors[i].get().split())
            sensors[i] = [x, y]
        plot_graph(sensors)

    graph_button = tk.Button(root, text="SHOW GRAPH", bg="lightpink", font=("arial", 10, "bold"),
                             command=graph_window)
    graph_button.place(x=500, y=500)

    result_button = tk.Button(root, text="SHOW RESULT", bg="lightpink", font=("arial", 10, "bold"),
                              command=result_window)
    result_button.place(x=900, y=500)

start_button = tk.Button(window, text="START", font=("arial", 20, "bold"), height=1, width=10, command=input_window)
start_button.place(x=700, y=600)

window.mainloop()
