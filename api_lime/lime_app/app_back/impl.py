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
from IPython.display import Image


def expalantion_model_lime_image(model, image,top_labels,hide_color,num_samples):
    explainer = lime_image.LimeImageExplainer(verbose=False)
    explanation = explainer.explain_instance(image= image[0], classifier_fn=model.predict, top_labels=top_labels, hide_color=hide_color, num_samples=num_samples)
    local = explanation.top_labels
    for n in range(top_labels):
        temp, mask = explanation.get_image_and_mask(local[n], positive_only=True, num_features=5, hide_rest=True)
        plt.imshow(mark_boundaries(temp / 2 + 0.5, mask))
        img = "./my_app/data/fig%d.jpg" % n
        plt.savefig(img)
    return "ok"






