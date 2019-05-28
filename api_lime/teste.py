import requests
#r = requests.post('http://localhost:5000/explanation/', data={'modelurl': 'https://drive.google.com/file/d/1dAkWIPLco68pdZ2G3iZoTvn_Ci3cvlas/view', 'exampleurl': 'https://drive.google.com/file/d/1YgZXJ591qMvbw2mwl-MX2bmu5XP8yOVP/view?usp=sharing'})


#model_img = 'https://github.com/viniaraujoo/model_Example/raw/master/model_incep.h5'

'''
Teste para requisição de modelos de imagens retinopatia
r = requests.post('http://localhost:5000/', data ={'model':'https://github.com/viniaraujoo/model_Example/raw/master/full_retina_model%20.h5','example': 'https://raw.githubusercontent.com/marcotcr/lime/master/doc/notebooks/data/cat_mouse.jpg'})
'''

r = requests.get('http://localhost:5000/explanationlime', data ={'model':'https://github.com/viniaraujoo/model_Example/raw/master/model_incep.h5','example': 'https://raw.githubusercontent.com/marcotcr/lime/master/doc/notebooks/data/cat_mouse.jpg','top_labels':4,'hide_color':0,'num_samples': 1000})

#v = requests.post('http://localhost:5000/', data ={'model':'https://github.com/viniaraujoo/model_Example/raw/master/model_incep.h5','example': 'https://raw.githubusercontent.com/marcotcr/lime/master/doc/notebooks/data/cat_mouse.jpg','top_labels':5})
#model_tabular = 'https://github.com/viniaraujoo/model_Example/raw/master/model.sav'

#r = requests.post('http://localhost:5000/tabular', data ={'model':'https://github.com/viniaraujoo/model_Example/raw/master/model.sav','example': 'https://raw.githubusercontent.com/viniaraujoo/model_Example/master/breast_cancer.csv'})
#v = requests.get('http://localhost:5000/tabular')
#r = requests.post('http://localhost:5000/uploads')
#v = requests.post('http://localhost:5000/uploadmodel', data = {'model': 'https://github.com/viniaraujoo/model_Example/raw/master/model_incep.h5'})
#r = requests.get('http://localhost:5000/load')
#v = requests.post('http://localhost:5000/uploadmodel', data = {'model': 'https://www.kaggle.com/viniciusaraujo/model-malaria/downloads/vgg_finetuned.h5/1'})
#r = requests.get('http://localhost:5000/shap', data ={'model': 'https://www.kaggle.com/viniciusaraujo/model-malaria/downloads/vgg_finetuned.h5/1', 'train': 'https://drive.google.com/a/ccc.ufcg.edu.br/uc?authuser=0&id=1rqN87_9sYkoC_5wuCWNaD9Vjl2r6Ee6g&export=download','example':'https://drive.google.com/a/ccc.ufcg.edu.br/uc?authuser=0&id=1BdIyjQmsuJZ_AOREhlEGyLU38ts2XOXu&export=download'})
##https://drive.google.com/a/ccc.ufcg.edu.br/uc?authuser=0&id=1BdIyjQmsuJZ_AOREhlEGyLU38ts2XOXu&export=download
#https://drive.google.com/a/ccc.ufcg.edu.br/uc?authuser=0&id=1FemIPhLz-FRRXOoSJ6Nf7P-ByZ3L7ZCO&export=download
#https://drive.google.com/a/ccc.ufcg.edu.br/uc?authuser=0&id=1rqN87_9sYkoC_5wuCWNaD9Vjl2r6Ee6g&export=download


### Teste LIME

#t = requests.post('http://localhost:5000/uploadmodel', data = {'model': 'https://github.com/viniaraujoo/model_Example/raw/master/model_incep.h5'})
print(r)
