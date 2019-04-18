import requests
#r = requests.post('http://localhost:5000/explanation/', data={'modelurl': 'https://drive.google.com/file/d/1dAkWIPLco68pdZ2G3iZoTvn_Ci3cvlas/view', 'exampleurl': 'https://drive.google.com/file/d/1YgZXJ591qMvbw2mwl-MX2bmu5XP8yOVP/view?usp=sharing'})


#model_img = 'https://github.com/viniaraujoo/model_Example/raw/master/model_incep.h5'

'''
Teste para requisição de modelos de imagens retinopatia
r = requests.post('http://localhost:5000/', data ={'model':'https://github.com/viniaraujoo/model_Example/raw/master/full_retina_model%20.h5','example': 'https://raw.githubusercontent.com/marcotcr/lime/master/doc/notebooks/data/cat_mouse.jpg'})
'''

r = requests.post('http://localhost:5000/', data ={'model':'https://github.com/viniaraujoo/model_Example/raw/master/model_incep.h5','example': 'https://raw.githubusercontent.com/marcotcr/lime/master/doc/notebooks/data/cat_mouse.jpg'})

#model_tabular = 'https://github.com/viniaraujoo/model_Example/raw/master/model.sav'

#r = requests.post('http://localhost:5000/tabular', data ={'model':'https://github.com/viniaraujoo/model_Example/raw/master/model.sav','example': 'https://raw.githubusercontent.com/viniaraujoo/model_Example/master/breast_cancer.csv'})
v = requests.get('http://localhost:5000/tabular')
print(r)
