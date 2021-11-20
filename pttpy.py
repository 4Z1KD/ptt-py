import time
import asyncio
import serial
import serial_asyncio
import sys
import configparser

def log(msg):
    t = time.localtime()
    current_time = time.strftime("%D %H:%M:%S", t)
    print(f"{current_time}  {msg}")

class Output(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport
        #log(f"{transport}")
        log("port open")
        log("waiting for ptt...")
    def data_received(self, data):
        #print("data received", repr(data))
        if data == b"on":
            ser.rts = True
            ser.dtr = True
            log("transmitting...")
        elif data == b"off":
            ser.rts = False
            ser.dtr = False
            log("receiving...")
        if b"\n" in data:
            log("closing...")
            self.transport.close()

    def connection_lost(self, exc):
        log("port closed")
        self.transport.loop.stop()

    def pause_writing(self):
        log("pause writing")
        log(self.transport.get_write_buffer_size())

    def resume_writing(self):
        log(self.transport.get_write_buffer_size())
        log("resume writing")

if __name__ == "__main__":
    #read config file
    config = configparser.ConfigParser()
    configFilePath = r'pttpy.cfg'
    config.read(configFilePath)
    virtual_port = config['interface']['virtual_port']
    physical_port = config['interface']['physical_port']

    global ser
    ser = serial.Serial(port=physical_port, baudrate=9600, timeout=None, xonxoff=False, rtscts=True, write_timeout=None, dsrdtr=True, inter_byte_timeout=None) #this is the actual port of the computer-radio interface
    ser.rts = False
    ser.dtr = False

    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    #loop = asyncio.get_event_loop()
    coro = serial_asyncio.create_serial_connection(loop, Output, virtual_port, baudrate=38400) #this is the virtual port where 3rd party apps send the command
    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()