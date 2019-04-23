# api-lime

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Several models of Machine Learning and Deep Learning emerges more and more to solve complex problems and tied to that we have models more and more these models are difficult to be interpreted being considered thus black-box models. In this way, it is difficult to promote ethics, justice and transparency about the decisions that certain models make regarding the context of the problem. Thinking about this, we developed this API for the [Atmosphere](https://www.atmosphere-eubrazil.eu/) project that aims to promote explanations for Keras models.
This API uses the LIME technique to promote model explanations.

# Example

**URL** : `/api/image`

**Method** : `POST`

**Data example**

```json
{
    "model": "https://github.com/viniaraujoo/model_Example/raw/master/model_incep.h5",
    "example": "https://raw.githubusercontent.com/marcotcr/lime/master/doc/notebooks/data/cat_mouse.jpg",
    "top_labels": 5,
    "num_samples": 1000,
    "hide_color": 0
    
}
```

**URL** : `/api/result`

**Method** : `GET`

![Result](https://raw.githubusercontent.com/viniaraujoo/model_Example/master/Screenshot%20from%202019-04-23%2009-16-12.png)

## Success Response

**Code** : `200 OK`

## Error Response
**Code** : `400`







License
----




![Foo](https://www.atmosphere-eubrazil.eu/sites/all/themes/theme1/logo.png)



  
