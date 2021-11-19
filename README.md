# ptt-py 🌺
A ptt script for 3rd party applications that use OmniRig on non-CAT radios 📻

# prerequisite 🖐️
1. com0com (https://sourceforge.net/projects/com0com/)
2. OmniRig (http://dxatlas.com/omnirig/)
3. python (https://www.python.org/downloads/)

# Installation 🛠
1. create virtual environment (https://docs.python.org/3/library/venv.html) ☁️
2. activate the venv (Scripts\activate.bat) 🌬️
3. copy this project's files to the venv directory 📑
4. install the requirements (pip install -r requirements.txt) 🧰
5. copy Pttpy.ini to OmniRig's rigs directory (usually @ C:\Program Files (x86)\Afreet\OmniRig\Rigs) 📂

## com0com setup 🔗
![image](https://user-images.githubusercontent.com/24712835/142699060-38d166e6-a6da-4b88-a946-c503939074b9.png)

## OmniRig settings ⚙️
![image](https://user-images.githubusercontent.com/24712835/142699149-1be7c6e8-95b4-41cb-8b21-914affde394f.png)

# final touch 🧙‍♂️
make sure to set the correct COM ports.<br/> 
```python
if __name__ == "__main__":
    global ser
    ser = serial.Serial("COM8") #this is the actual port of the computer-radio interface
    ser.setRTS(False)

    loop = asyncio.get_event_loop()
    coro = serial_asyncio.create_serial_connection(loop, Output, "COM7", baudrate=38400) #this is the virtual port where 3rd party apps send the command
    loop.run_until_complete(coro)
    loop.run_forever()
    loop.close()
```
check in Device Manager if you are not sure.<br/>
![image](https://user-images.githubusercontent.com/24712835/142700304-cbc0b311-84b0-4297-a8ff-70b8d7e2a043.png)

# usage 🚀
launch pttpy.bat (this will activate the venv and run the script)

# what to expect 🤷‍♀️
whenever a ptt command is sent by a 3rd party program (Tx or Rx),<br/>
OmniRig sends the command defined in pttpy.ini to the virtual COM port we set.<br/>
the script receives the command and set RTS to the physical COM port of the computer-radio interface,>br/>
and it also logs to the cmd window.

# acknowledgments 🎁
- Irad 4Z1AC for developing VarAC (https://www.varac-hamradio.com/)
- Avishay 4X1ZQ for trying to play with VarAC on a non-CAT radio which created the need
- Gadi 4X6AG for discussing the technical issues and suggesting alternatives

73<br/>
Gil 4Z1KD
