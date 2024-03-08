# BEEZY: An innovative approach to redesigning Beehives for better monitoring of the colony
Beezy was an innovative solution to monitoring bee hive environmental factors and colony health. This was a smart redesign of the traditional beehive. The two primary functions were:<br>
1. **Tracking essential environmental metrics** that can be telling of the health of the hive. Temperature sensors, humidity sensors and CO2 sensors were placed on the roof of the hive and connected to an ESP32. The ESP32 read from these sensors in a timely fashion and transferred this data to a Raspberry Pi using UART communication protocol.
2. **Automation of the calculation of the varroa mite infestation rate** in a hive. I created a deep learning pipeline that took images from a camera mounted on the hive and estimated the manual process of determining varroa mite infestation rates with high accuracy.<br>

## Automated vrroa mite testing
Two YOLO models were trained: One was trained to detect bees in an image. Second was used to detect varroa mites from the detected bees. Here is how the pipeline worked:

1. PiCam takes pictures of the hive when testing is requested.
2. Pictures are run through the first model. Bee objects are detected, cropped out and saved.
3. The saved bee images are run through the second model which detects varroa mites present in these images.
4. The infestation rate is calculated using the number of bees and varroa mites detected.
_Fig: Algorithm for calculating varroa mite infestation rate_
_Fig: Output of first model_
_Fig: Output of second model_

I created a simple GUI that the user could use to monitor the metrics and run tests whenever they choose to.
_Fig: GUI_
