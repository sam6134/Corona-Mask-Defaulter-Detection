# Corona-Mask-Defaulter-Detection
A simple web-app build on flask framework that detects people without face mask using cascade filters. The problem dealing with todays scenario is that many people do not follow the norms of social distancing and are not wearing face masks.\
In order to deal with this situation, I attempted to build a feasible a solution that could detect faces without masks and identify the defaulters using webcam stream.\
The model that I have used the haar cascades that is a machine learing object detection algorithm and can be used to find faces in a stream with great accuracy in real time. People not wearing masks can be easily identified using this filter which a series of classifier trained on 1000 of postive face images and negative face images using Ada-Boost.\
\
The models weights are directly used and can be found in the directory. To use the demo web-app please follow the below instructions.


## Instructions
Install dependencies as given in requirements.txt 
```
pip install requirements.txt
```
After cloning the directory in your system.\
Open cmd prompt or terminal, navigate to the directory
cd Face-Mask Detection
```
cd  Face-Mask\ Detection/
```
Run run.py
```
python3 run.py
```
Open [localhost:5000](http://127.0.0.1:5000/) in the browser
### Results
<p align="center">
 <img src="https://github.com/sam6134/Corona-Mask-Defaulter-Detection/blob/master/results/Screen%20Shot%202020-05-06%20at%202.56.43%20PM.png" width="264" alt="Screenshot"/>
  <img src="https://github.com/sam6134/Corona-Mask-Defaulter-Detection/blob/master/results/Screen%20Shot%202020-05-06%20at%202.57.06%20PM.png" width="264" alt="Screenshot"/>
 </p>
  
### License
<img src="https://img.shields.io/badge/license-MIT-blue.svg?style=flat" width="80" />
Note this Web app is distributed under the [MIT License](http://opensource.org/licenses/MIT).

Your feedback, ideas, suggestions are most welcome!
