import os
import time

# path for the adb.
path = "D:\SDK\platform-tools"

# checking for connected devices
device = os.popen("adb devices").read()
print(device)

# connect to the selected device 172.0.0.1:62001
print("Waiting for connection ...")
connect = os.popen("adb connect "+device).read()
print(connect)

# gradle build apk
os.system("gradlew assembleDebug ")

#installing apk
os.system("adb install F://TrainTicketing1//app//build//outputs//apk//debug//app-debug.apk")

#testing and collecting logcat
#time.sleep(3)
os.system("adb shell monkey --ignore-crashes -p com.example.anupamanurag.trainticketing1 -v 2000 --hprof > test11log.txt")


