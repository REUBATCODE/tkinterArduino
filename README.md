# tkinterArduino
A GUI to control an Arduino Uno.

To develop a graphical application in Python that controls an Arduino, you will need several libraries to help you interact with both the graphical interface and the Arduino hardware. Here are some recommendations:

### 1. **Tkinter**
Since you plan to use Tkinter for the graphical interface, it comes pre-installed with Python, so you should not need to install it explicitly. However, if for some reason you do not have it, you can install it with:

```bash
pip install tk
```

### 2. **pySerial**
To communicate with the Arduino through the serial port, `pySerial` is essential. This library allows you to read and write data on the serial port, which is crucial for sending commands to the Arduino and receiving data from it.

```bash
pip install pyserial
```

### 3. **Python-Arduino-Command-API**
Although not strictly necessary, `Python-Arduino-Command-API` is a library that facilitates communication between Python and Arduino, allowing you to send commands in a simpler and more readable way.

```bash
pip install arduino-python3
```

This package may not be directly available through `pip` or may require manual installation from its GitHub repository if the `pip` version is not the most updated or if the package is not actively maintained.

### 4. **Pillow (PIL Fork)**
If your graphical application needs to handle images (such as icons or photos), Pillow will be very useful. It is an image processing library that allows you to open, manipulate, and save many different file formats.

```bash
pip install Pillow
```

### 5. **NumPy**
Although not specific for the development of graphical applications or communication with Arduino, NumPy is a fundamental library for data handling in Python. If your project involves complex mathematical operations or handling large amounts of data, NumPy will be very useful.

```bash
pip install numpy
```