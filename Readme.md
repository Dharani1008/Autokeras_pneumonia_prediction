# Auto-Keras-Pneumonia prediction
## REST API SETUP
### Download Anaconda 5.3.0 or above
wget https://repo.anaconda.com/archive/Anaconda3-2020.02-Linux-x86_64.sh
### Install Anaconda
bash ~/Downloads/Anaconda3-2020.02-Linux-x86_64.sh

### Create conda environment
conda create -n ak python=3.6 anaconda

### Activate the environment
conda activate ak

### Clone the repo
git clone https://github.com/Dharani1008/Autokeras_pneumonia_prediction


To install Auto-Keras please use the `pip` installation as follows:

    pip install git+https://github.com/keras-team/keras-tuner.git@1.0.2rc2
    pip install autokeras
    pip install tensorflow-gpu==2.3.0  # GPU
    
**Note:** currently, Auto-Keras is only compatible with: **Python 3.6**.

## Example

Here is a short example of using the package.


    import autokeras as ak

    clf = ak.ImageClassifier()
    clf.fit(x_train, y_train)
    results = clf.predict(x_test)

## Datasets:
    The Autokeras Model is trained with Chest X-Ray images, Normal images and Pneumonia images and it is tested with  test images. Using Flask, restAPI is developed for web server usages.

### run the api server
python flask_sever.py

### Test the api server

cURL command example:
`curl -F "image=@0_L_CC.png" http://{ipaddress}:5012/api/v0`

 
