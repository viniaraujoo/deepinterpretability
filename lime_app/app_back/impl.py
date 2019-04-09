import requests
import json
import lime
from lime import lime_image
import lime.lime_tabular
from lime import lime_text
from lime.lime_text import LimeTextExplainer
from lime import submodular_pick
import numpy as np
import os
import keras
from keras.preprocessing import image
from keras.applications import inception_v3 as inc_net
import sklearn
from skimage.segmentation import mark_boundaries
from keras.models import load_model
from keras.metrics import top_k_categorical_accuracy

## Application code - LIME


def impl(model_predict,test,train=None,feature_names=None,class_names=None,idx_test=None,num_features=6,top_labels=5,hide_color=0,num_samples=1000):
      
      
    if(type(test) == bytes):
        img = transforming_img(test)
        explainer = lime_image.LimeImageExplainer(verbose=False)
        explanation = explainer.explain_instance(image= img[0], classifier_fn=model_predict, top_labels=top_labels, hide_color=hide_color, num_samples=num_samples)
        listtop = explanation.top_labels
        result = []
        for n in range(top_labels):
            top_local = listtop[n]
            temp, mask = explanation.get_image_and_mask(top_local, positive_only=True, num_features=5, hide_rest=True)
            img = mark_boundaries(temp / 2 + 0.5, mask)
            result.append(img)
        return result
        
    elif(type(test) == np.ndarray):
        explainer = lime.lime_tabular.LimeTabularExplainer(training_data=train, feature_names=feature_names, class_names=class_names, discretize_continuous=True)
        exp = explainer.explain_instance(data_row=test[idx_test], predict_fn=model_predict, num_features=num_features)
        return exp.show_in_notebook(show_table=True, show_all=False)                                                 
    else:
        explainer = LimeTextExplainer(class_names=class_names)
        exp = explainer.explain_instance(text_instance=test[idx_test], classifier_fn=model_predict, num_features=num_features)
        sp_obj = submodular_pick.SubmodularPick(explainer=explainer, data=test, predict_fn=model_predict, sample_size=2, num_features=6,num_exps_desired=2,top_labels=3)
        return [exp.as_pyplot_figure(label=0) for exp in sp_obj.sp_explanations];

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


def load_model(url):
    model = requests.get(url).content
    with open(os.path.join('model.h5'), 'wb') as handler:
        handler.write(model)
    model = load_model('/home/vinicius/WebService/WebService-LIME/model.h5',custom_objects={'top_2_accuracy': top_2_accuracy})
    return model


def explanation_image(url1, url2):
    img_data = requests.get(url2).content
    img_data = transforming_img(img_data)
    model = load_model(url1)

    return 'ok'
