# Deep Learning Interpretability

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

## Save Model

The templates are saved in mongodb database for future explanation, the template download URL is the key to access in the future.

model: Keras model URL saved in file type [H5](https://www.h5py.org/)

### Example

**URL** : `/api/uploadmodel`

**Method** : `POST`

**Data example**
```json
{
    "model": "https://github.com/viniaraujoo/model_Example/raw/master/model_incep.h5"
}
```



## LIME:

**model:**  Template key (URL) saved to the database

**example:** URL of the image you want to use as an example of model explanation

**top_labels:** Explanation for K labels with higher probability.

**num_samples:** size of the neighborhood to learn the linear model

**hide_color:** 0 or 1

### Example

**URL** : `/api/explanationlime`

**Method** : `GET`

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

![Result](https://raw.githubusercontent.com/viniaraujoo/model_Example/master/Screenshot%20from%202019-04-23%2009-16-12.png)

## Success Response

**Code** : `200 OK`

## Error Response
**Code** : `400`

## SHAP:
**model:** Template key (URL) saved to the database

**example:** Image URL in numpy compressed ZIP file (Image that you want the explanation).

**train:** ZIP of the set of images numpy array train format of the explanation.

### Example

**URL** : `/api/shap`

**Method** : `GET`

**Data example**

```json
{
    "model": "https://github.com/viniaraujoo/model_Example/raw/master/model_incep.h5",
    "example": "",
    "train": ,

}
```

![Result](])

## Success Response

**Code** : `200 OK`

## Error Response
**Code** : `400`



License
----




![Foo](https://www.atmosphere-eubrazil.eu/sites/all/themes/theme1/logo.png)