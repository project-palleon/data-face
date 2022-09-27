# PALLEON data-face

> This is a repository that's part of the Palleon project, which in turn is a part of the SoC 2022.
>
> This project is still very much WIP, so everything is subject to radical change as I have to
> adjust everything to new requirements that come up on the way of developing.
>
> So I am sorry for everyone who has to look at this code. It will get better - I hope...

## How it works

1. load a classifier file for the [Cascade Classifier](https://docs.opencv.org/3.4/db/d28/tutorial_cascade_classifier.html)
2. receive frames from the core
3. use the cascade classifier to find face lookalikes
4. select the bounding box with the greatest area
5. cut the face out of the original face
6. send it back to the core
7. return to step 2

## Improvements

1. use a more sophisticated approach to find faces to
   1. be more accurate
   2. have less false positives
2. send only the coordinates instead of an image cut-ou
3. calculate some kind of "face-id" to enable face based authentication

## Installation

1. download a cascade file for the cascade classifier: https://github.com/opencv/opencv/tree/master/data/haarcascades
2. install python 3 (I am using version 3.10, I have not tested prior versions)
3. install requirements from requirements.txt
4. start the core
