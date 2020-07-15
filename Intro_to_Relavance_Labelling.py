
# coding: utf-8

# In[1]:


import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import spacy
from operator import itemgetter
import numpy as np
from matplotlib_venn import venn2, venn3

nlp = spacy.load('en_core_web_sm')


# In[21]:


def load_data(location):
    '''This function loads the data and finds the number of words labelled by the labeller'''
    
    f = open(location) 
    person = json.load(f)
    N = len(person[-1])
    
    return person, N


def get_data(person):
    '''This function gets words marked relevant and non-relevant by the labeller'''
    
    N = len(person[-1])
    
    relevant = set()
    for i in range(N):
        if person[-1][i][2] == '1':
            relevant.add(person[-1][i][0])
            
    nonrelevant = set()
    for i in range(N):
        if person[-1][i][2] == '0':
            nonrelevant.add(person[-1][i][0])
            
    return relevant, nonrelevant
            
            
    


# In[20]:


argota, Na = load_data('FashionData/fashion_cleaned-tagged_argota.json',) 
cata, Nc = load_data('FashionData/fashion_cleaned-tagged_cata.json',) 
manuel, Nm = load_data('FashionData/fashion_cleaned-tagged_manuel.json',) 
marta, Nmt = load_data('FashionData/fashion_cleaned-tagged_marta.json',) 
shivangi, Ns = load_data('FashionData/fashion_cleaned-tagged_shivangi.json',) 
uxue, Nu = load_data('FashionData/fashion_cleaned-tagged_uxue.json',) 

print('Argota: {} , Cata : {}, Manuel : {}, Marta : {}, Shivangi : {}, Uxue : {}'.format(Na, Nc, Nm, Nmt, Ns, Nu))
#Not using Argota Labellings


# In[22]:


relevant_argota , nonrelevant_argota = get_data(argota)
relevant_cata , nonrelevant_cata = get_data(cata)
relevant_manuel, nonrelevant_manuel = get_data(manuel)
relevant_marta , nonrelevant_marta = get_data(marta)
relevant_shivangi , nonrelevant_shivangi = get_data(shivangi)
relevant_uxue , nonrelevant_uxue = get_data(uxue)


# In[23]:


'''print('SHIVANGI - RELEVANT: ', len(relevant_shivangi)/len(shivangi[-1]), ' nonRELEVANT: ', len(nonrelevant_shivangi)/len(shivangi[-1]))
print('MARTA - RELEVANT: ', len(relevant_marta)/len(marta[-1]), ' nonRELEVANT: ', len(nonrelevant_marta)/len(marta[-1]))
print('CATA - RELEVANT: ', len(relevant_cata)/len(cata[-1]), ' nonRELEVANT: ', len(nonrelevant_cata)/len(cata[-1]))
print('UXUE - RELEVANT: ', len(relevant_uxue)/len(uxue[-1]), ' nonRELEVANT: ', len(nonrelevant_uxue)/len(uxue[-1]))
print('MANUEL - RELEVANT: ', len(relevant_manuel)/len(manuel[-1]), ' nonRELEVANT: ', len(nonrelevant_manuel)/len(manuel[-1]))'''


# In[10]:


'''This clearly shows we have two groups of people. 
Shivangi and Uxue didnt find a lot of words relevant. Marta, Cata and Manuel did.  '''


# # UNANIMOUS DECISION

# In[24]:


all_relevant = relevant_shivangi.intersection(relevant_marta).intersection(relevant_cata).intersection(relevant_uxue).intersection(relevant_manuel)
all_nonrelevant = nonrelevant_shivangi.intersection(nonrelevant_marta).intersection(nonrelevant_cata).intersection(nonrelevant_uxue).intersection(nonrelevant_manuel)
print('ALL RELEVANT: ', len(all_relevant))
print('ALL nonRELEVANT: ', len(all_nonrelevant))


# In[11]:


'''There are 130 words all the 5 people think are relevant, and 22 words everyone thinks are non-relevant.
Lets look at those words'''


# In[17]:


all_nonrelevant


# In[18]:


all_relevant

