# Button-Service
This repository contains a RESTful service that provides a GET /wait_for_button endpoint. When called, the service waits for a physical button to be pressed and returns once the press is detected. If the button is not pressed within 3 minutes, the request will timeout.

## Installation

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/kevi-nguyen/button-service.git
   cd button-service
   ```

2. **Install Dependencies**:
   Activate your virtual environment and install the required dependencies from the `requirements.txt` file.
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the Service**:
   To start the button service, use the following command:
   ```bash
   python Button-API.py
   ```
   This will start the FastAPI service on `http://0.0.0.0:8082`.

## Required Adjustments

**Serial Port Adjustment**:
If you're using a button connected via a serial port, the `port` variable in the code needs to match the serial port available on your computer.
The current port is configured for a macOS system:
```python
port = '/dev/tty.usbserial-AQ027FTG'
```
On a Windows system, you will need to change this to the appropriate **COM port** (e.g., `COM3`), and on Linux, it might look like `/dev/ttyUSB0`. Adjust the code as follows:

- For **Windows**:
```python
port = 'COM3'  # Replace with the correct COM port number
```

- For **Linux**:
```python
port = '/dev/ttyUSB0'  # Replace with the correct USB serial port
```

Ensure that the correct serial driver is installed and that the device is properly connected.
