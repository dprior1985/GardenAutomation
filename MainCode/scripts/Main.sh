
sudo modprobe w1-gpio
sudo modprobe w1-therm

sleep 1
sh /home/pi/Desktop/GardenAutomation/MainCode/scripts/Senors.sh >> /home/pi/Desktop/Logs/Senors.log 2>&1
