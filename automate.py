import os
import time


# path for the adb.
#path = "D:\SDK\platform-tools"

# checking for connected devices
device = os.popen("adb devices").read()
print(device)

# connect to the selected device 172.0.0.1:62001
#print("Waiting for connection ...")
connect = os.popen("adb connect "+device).read()
#print(connect)

# gradle build apk
os.system("gradlew installDebug ")

#installing apk
#os.system("adb install F://TrainTicketing1//app//build//outputs//apk//debug//app-debug.apk")

#testing and collecting logcat
print("Monkey is testing the app...")
os.system("adb shell monkey -v --throttle 100 -p com.example.anupamanurag.trainticketing1 1000 > test11log.txt")
time.sleep((1000*100)/1000)

#kernel log
os.popen("adb shell dmesg >kernel3log.txt")

