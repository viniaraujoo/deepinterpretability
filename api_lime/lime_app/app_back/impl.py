import requests
import json
import lime
import matplotlib.pyplot as plt
import numpy as np
import os
import keras
import sklearn
from keras.preprocessing import image
from keras.applications import inception_v3 as inc_net
from lime import lime_image
from skimage.segmentation import mark_boundaries
from keras.models import load_model
from keras.metrics import top_k_categorical_accuracy
from IPython.display import Image


def expalantion_model(model, image,top_labels,hide_color,num_samples):
    explainer = lime_image.LimeImageExplainer(verbose=False)
    explanation = explainer.explain_instance(image= image[0], classifier_fn=model.predict, top_labels=top_labels, hide_color=hide_color, num_samples=num_samples)
    local = explanation.top_labels
    for n in range(top_labels):
        temp, mask = explanation.get_image_and_mask(local[n], positive_only=True, num_features=5, hide_rest=True)
        plt.imshow(mark_boundaries(temp / 2 + 0.5, mask))
        img = "./my_app/data/fig%d.jpg" % n
        plt.savefig(img)
    return "ok"





def transforming_img(exemple):
    with open(os.path.join('image.jpg'), 'wb') as handler:
        handler.write(exemple)
    images = transform_img_fn([os.path.join('image.jpg')])

    return images


def transform_img_fn(path_list):
    #Transform image so it can be processed by inception.
    out = []
    for img_path in path_list:
        img = image.load_img(img_path, target_size=(299, 299))
        x = image.img_to_array(img)
        x = np.expand_dims(x, axis=0)
        x = inc_net.preprocess_input(x)
        out.append(x)
    return np.vstack(out)


def top_2_accuracy(in_gt, in_pred):
    return top_k_categorical_accuracy(in_gt, in_pred, k=2)


def load_model_keras(url):
    model = requests.get(url).content
    with open(os.path.join('model.h5'), 'wb') as handler:
        handler.write(model)
    model = load_model('./model.h5',custom_objects={'top_2_accuracy': top_2_accuracy})
    return model

def explanation_image(url1, url2,top_labels,hide_color,num_samples):
    img_data = requests.get(url2).content
    img_data = transforming_img(img_data)
    model = load_model_keras(url1)
    expalantion_model(model,img_data,top_labels,hide_color,num_samples)
    return 'ok'





