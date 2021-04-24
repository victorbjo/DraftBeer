File explanation:
data10Sec.npz, log of temperature measured every 10 second in the last hour
homepage.py main website
readData.py can read log files
target.py can read and write target temp to targetTemp.txt
targetTemp.txt target temp is stored here for logic and sync purposes
tempLogger.py logs temp and timestamp every 10 seconds in one file, and every 3 min in another
tempRead.py can read temp from thermometers
ANN.py to train neural network
think.py to run a neural network




README.txt is a description of the project, the files and how to start the webapp

To run the website:
navigate into the folder
sudo python3 homepage.py &

In another terminal, to log temps
python3 tempLogger.py&
