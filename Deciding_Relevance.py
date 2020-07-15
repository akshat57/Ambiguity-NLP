
# coding: utf-8

# In[125]:


import json
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import spacy
from operator import itemgetter
import numpy as np
from matplotlib_venn import venn2, venn3
from Intro_to_Relavance_Labelling import load_data, get_data

nlp = spacy.load('en_core_web_sm')


# In[116]:


'''argota, Na = load_data('FashionData/fashion_cleaned-tagged_argota.json',) 
cata, Nc = load_data('FashionData/fashion_cleaned-tagged_cata.json',) 
manuel, Nm = load_data('FashionData/fashion_cleaned-tagged_manuel.json',) 
marta, Nmt = load_data('FashionData/fashion_cleaned-tagged_marta.json',) 
shivangi, Ns = load_data('FashionData/fashion_cleaned-tagged_shivangi.json',) 
uxue, Nu = load_data('FashionData/fashion_cleaned-tagged_uxue.json',) 

print('Argota: {} , Cata : {}, Manuel : {}, Marta : {}, Shivangi : {}, Uxue : {}'.format(Na, Nc, Nm, Nmt, Ns, Nu))
#Not using Argota Labellings

relevant_argota , nonrelevant_argota = get_data(argota)
relevant_cata , nonrelevant_cata = get_data(cata)
relevant_manuel, nonrelevant_manuel = get_data(manuel)
relevant_marta , nonrelevant_marta = get_data(marta)
relevant_shivangi , nonrelevant_shivangi = get_data(shivangi)
relevant_uxue , nonrelevant_uxue = get_data(uxue)

all_labels = [relevant_cata , nonrelevant_cata, relevant_manuel, nonrelevant_manuel, relevant_marta , nonrelevant_marta, relevant_shivangi , nonrelevant_shivangi, relevant_uxue , nonrelevant_uxue]'''


# In[74]:


def calculate_score(word, cata, manuel, marta, shivangi, uxue):
    score = 0
        
    if word in cata:
        score += 1
        
    if word in manuel:
        score += 1
        
    if word in marta:
        score += 1
        
    if word in shivangi:
        score += 1
        
    if word in uxue:
        score += 1
        
    return score
    


# In[126]:


def deciding_relevance(decision_threshold, all_labels, marta):

    relevant_cata , nonrelevant_cata, relevant_manuel, nonrelevant_manuel, relevant_marta , nonrelevant_marta, relevant_shivangi , nonrelevant_shivangi, relevant_uxue , nonrelevant_uxue = all_labels
    
    #Since Marta did the max number of words, we use those
    decision_relevant = []
    decision_nonrelevant = []

    for word, _, _, _ in marta[-1]:
        relevant_score = calculate_score(word, relevant_cata, relevant_manuel, relevant_marta, relevant_shivangi, relevant_uxue)
        nonrelevant_score = calculate_score(word, nonrelevant_cata, nonrelevant_manuel, nonrelevant_marta, nonrelevant_shivangi, nonrelevant_uxue)

        if relevant_score >= decision_threshold:
            decision_relevant.append(word)

        elif nonrelevant_score >= decision_threshold:
            decision_nonrelevant.append(word)

    print('Relevant : {}, NonRelevant : {}'.format(len(decision_relevant), len(decision_nonrelevant)))
    
    return decision_relevant, decision_nonrelevant


# In[124]:


#decision_relevant, decision_non_relevant = deciding_relevance(3, all_labels)

