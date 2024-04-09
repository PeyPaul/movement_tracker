# motion sensor
 This code utilizes the Mediapipe library along with OpenCV for real-time pose detection and angle calculation from a webcam feed. The program captures video frames from the webcam, detects human poses, and calculates angles between specific body joints. It then visualizes these angles on the video feed. Finally, the position of the body is analized to unlock the secret message

## user's instruction
- We first need to install the dependencies
Run the following bash command once you are in your python environnement :
pip install mediapipe opencv-python
- To change the code or the secret message, modify the corresponding values in the file settings.py
- Other useful values can be modify in the file settings.py but for more important change, such as the color, you have to change the file main.py
- To launch the project, run the file 'main.py'. To close the mediapipe feed press the 'q' key

## Credits
This code was made by Paul Peytevin, an engineer student at CentraleSupelec (part of University Paris-Saclay)