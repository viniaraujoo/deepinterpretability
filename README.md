# Dillinger

[![Build Status](https://travis-ci.org/joemccann/dillinger.svg?branch=master)](https://travis-ci.org/joemccann/dillinger)

Several models of Machine Learning and Deep Learning emerges more and more to solve complex problems and tied to that we have models more and more these models are difficult to be interpreted being considered thus black-box models. In this way, it is difficult to promote ethics, justice and transparency about the decisions that certain models make regarding the context of the problem. Thinking about this, we developed this API for the [Atmosphere](https://www.atmosphere-eubrazil.eu/) project that aims to promote explanations for Keras models.
This API uses the LIME technique to promote model explanations.

# Example

Used to collect a Token for a registered User.

**URL** : `/api/login/`

**Method** : `POST`   `GET`

**Data example**

```json
{
    "likmodel": "iloveauth@example.com",
    "examplemodel": "abcd1234"
    
}
```

## Success Response

**Code** : `200 OK`

## Error Response
**Code** : `400`







License
----

MIT


![Foo](https://www.atmosphere-eubrazil.eu/sites/all/themes/theme1/logo.png)



  
