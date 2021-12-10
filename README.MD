# AndroidSmishingSender
Send smishing (phishing SMS) messages with the Android phone from CSV file via ADB

## Installation

Enable USB debugging on your Android device:
1. Open the Settings app.
2. Select System.
3. Scroll to the bottom and select About phone.
4. Scroll to the bottom and tap Build number 7 times.
5. Return to the previous screen to find Developer options near the bottom.
6. Scroll down and enable USB debugging.

Install ADB (Debian-based Linux distribution) on your PC:
```
sudo apt install android-tools-adb
```

## CSV input file structure

CSV file structure: 
```
message_id,phone_number,message 
```

CSV file example:
```
1,+1000223332,Check this phishing page: https://google.com/?param=1232
2,+1000223322,Check this phishing page: https://google.com/?param=1233
3,+1000223342,Check this phishing page: https://google.com/?param=1234
```

Maximum message length - 160 characters (if no special characters are used).

## Usage

Connect your Android device with the USB cable to your PC, confirm trusting the connected PC on your Android device, prepare the CSV file and run the tool.

```
usage: AndroidSmishingSender.py [-h] [--input INPUT]

optional arguments:
  -h, --help            show this help message and exit
  --input INPUT, -i INPUT
                        Input CSV file, structure: message_id,phone_number,message
```

Example:
```
python AndroidSmishingSender.py -i file.csv
```

## Authors
Inceite - www.inceite.com