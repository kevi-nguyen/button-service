import time

import serial
import uvicorn
from fastapi import FastAPI, HTTPException

app = FastAPI()

port = '/dev/tty.usbserial-AQ027FTG'
baudrate = 9600
ser = serial.Serial(port, baudrate, timeout=1)

button_was_pressed = False
button_is_pressed = False

@app.get("/wait_for_button_press")
def wait_for_button_press():
    """
    Endpoint to wait for the button to be pressed and then return the status.
    """
    start_time = time.time()
    timeout = 180

    while True:
        try:
            if ser.in_waiting > 0:
                data = ser.read(ser.in_waiting)
                return {"status": "pressed"}
            # Check for timeout
            if time.time() - start_time > timeout:
                raise HTTPException(status_code=408, detail="Request timed out")

            time.sleep(0.1)

        except serial.SerialException as e:
            raise HTTPException(status_code=500, detail=f"Serial error: {e}")
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Error: {e}")


if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8082)
