# csce636_facial_expression_recognition
In this project, I am going to use a Convolutional Neural Network(CNN) to implement the facail expressions recognition from distinct images. First of all, we should install dependencies.
* tensorflow
* tflearn
* numpy
* argparse
* hyperopt
* pymongo
* network

If you want to train the model by yourself, please go ahead with my instruction, or if you want to just test the GUI the the model I have already trained, you can go directly downloading the files under the "best_model" folder firstly, and just put these files under the "best_model" folder, and then run the command "python test_gui.py".
### 1. Download dataset
I choose Fer2013 as the training dataset. Because of the size restriction of the uploading files, I decide to attach a link to download the related dataset. You can find it in the "dataset" folder.

### 2. Model training
```
python train.py --train=yes
```
In addition, if you want to train and evaluate
```
python train.py --train=yes --evaluate=yes
```
### 3.Optimizing training hyperparameters
```
python optimize_hyperparams.py --max_evals=20
```
After this, retrain the model:
```
python train.py --train=yes --evaluate=yes
```
### 4. Calculate the test accuracy
```
python train.py --evaluate=yes
```
### 5. Run the gui
```
python test_gui.py
```
You can test with the images under the "test_imgs" folder, or you can just use your own daily photos with different resolutions.
### 6. Demo
You can click the link to watch the demo: https://www.youtube.com/watch?v=Rcfiw0s2xa0
