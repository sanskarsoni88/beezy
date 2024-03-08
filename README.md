# BEEZY: An innovative approach to redesigning Beehives for better monitoring of the colony

Beezy was an innovative solution to monitoring bee hive environmental factors and colony health. This was a smart redesign of the traditional beehive. The two primary functions were:

1. **Tracking essential environmental metrics** that can be telling of the health of the hive. Temperature sensors, humidity sensors, and CO2 sensors were placed on the roof of the hive and connected to an ESP32. The ESP32 read from these sensors in a timely fashion and transferred this data to a Raspberry Pi using UART communication protocol.
2. **Automation of the calculation of the varroa mite infestation rate** in a hive. I created a deep learning pipeline that took images from a camera mounted on the hive and estimated the manual process of determining varroa mite infestation rates with high accuracy.

## Automated varroa mite testing

Two YOLO models were trained: One was trained to detect bees in an image. The second was used to detect varroa mites from the detected bees. Here is how the pipeline worked:


1. PiCam takes pictures of the hive when testing is requested.
2. Pictures are run through the first model. Bee objects are detected, cropped out, and saved.<br>
<div align="center">
  <img src="/bee_detection.png" alt="Output of first model"><br>
  <em>Fig: Output of first model</em><br><br>
</div>
3. The saved bee images are run through the second model which detects varroa mites present in these images.<br>
<div align="center">
  <img src="/Varroa_Mite_detection.jpg" alt="Output of second model"><br>
  <em>Fig: Output of second model</em><br><br>
</div>
4. The infestation rate is calculated using the number of bees and varroa mites detected.<br>
<div align="center">
  <img src="/algorithm.png" alt="Algorithm for calculating varroa mite infestation rate"><br>
  <em>Fig: Algorithm for calculating varroa mite infestation rate</em><br><br>
</div>




## GUI
I created a simple GUI that the user could use to monitor the metrics and run tests whenever they choose to.

<div align="center">
  <img src="/GUI.png" alt="GUI"><br>
  <em>Fig: GUI</em>
</div><br><br>
## Report
Here is a link to the [Final Report](https://drive.google.com/file/d/1C9szNUPga6EwcM8YAbFXn-X4DOJMqWRc/view?usp=sharing).
