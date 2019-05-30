import lime
import matplotlib.pyplot as plt
import numpy as np
import os
import shap
from lime import lime_image
from skimage.segmentation import mark_boundaries
from IPython.display import Image



def expalantion_model_lime_image(model, image,top_labels,hide_color,num_samples):
    explainer = lime_image.LimeImageExplainer(verbose=False)
    explanation = explainer.explain_instance(image= image[0], classifier_fn=model.predict, top_labels=top_labels, hide_color=hide_color, num_samples=num_samples)
    local = explanation.top_labels

    plt.figure(1 , figsize = (4,4))
    n = 0 
    for i in range(len(local)):
        n += 1 
        plt.subplot(4 , 4 , n)
        plt.subplots_adjust(hspace = 0.5 , wspace = 0.5)
        temp, mask = explanation.get_image_and_mask(local[i], positive_only=True, num_features=5, hide_rest=True)
        plt.imshow(mark_boundaries(temp / 2 + 0.5, mask))
    plt.savefig('./my_app/result.jpg')
    return "ok"


def expalantion_model_shap_image(model, train,example):
    explanation = shap.DeepExplainer(model, train)
    shap_values = explanation.shap_values(example)
    fig = shap.image_plot(shap_values, -example, show=False)
    plt.savefig('./my_app/result.jpg')
    return "ok"






