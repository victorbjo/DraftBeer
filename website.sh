#!/bin/bash
cd website
sudo python3 coolerControl.py & 
sudo python3 saveTempData.py &
sudo python3 tempLogger.py &
sudo python3 homepage.py &
