#Sending SMS from CSV via ADB
#CSV structure: message_id,phone_number,message
#Authors: Inceite - www.inceite.com

import csv
import os
import time
import re
import argparse

parser = argparse.ArgumentParser(description="Send smishing (phishing SMS) messages with the Android phone from CSV file via ADB. Authors: Inceite - www.inceite.com")
parser.add_argument("--input", "-i", help="Input CSV file, structure: message_id,phone_number,message")
args = parser.parse_args()

if not args.input:
    parser.print_help()
else:
    with open(args.input, newline='') as f:
        reader = csv.reader(f, delimiter=',')
        sms_list = list(reader)

    for sms in sms_list:
        message_id = sms[0]
        phone_number = sms[1]

        if(len(sms[2])>160):
            print('SMS id:'+message_id+' to:'+phone_number+' status: ERROR: Too long message (max 160 chars))')
            continue

        message = re.sub("(.)",r"\\\1",sms[2])

        cmd = 'adb shell service call isms 7 i32 0 s16 "com.android.mms.service" s16 "' +phone_number+'" s16 "null" s16 "'+message+'" s16 "null" s16 "null"'
        returned_value = os.system(cmd)
        print('SMS id:'+message_id+' to:'+phone_number+' status:' + str(returned_value))

        #max 30 SMS in 30 min
        time.sleep(61)
