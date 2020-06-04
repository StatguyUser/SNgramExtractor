#!/usr/bin/env python
# coding: utf-8

# In[333]:


import spacy
nlp = spacy.load('en_core_web_sm')

class SNgramExtractor:
    '''
    text:input text
    meta_tag:Resultant bigram and trigram should be concatenated with part of speech tag('pos') or dependency tag('dep') or original SN-gram('original')
    trigram_flag:if we need to include trigrams derived from SN-grams as well ('yes') or not ('no'). Default is 'yes'
w
    '''
    def __init__(self,text,meta_tag,trigram_flag='yes',nlp_model=None):
        self.text=text
        self.meta_tag=meta_tag
        self.trigram_flag=trigram_flag
        if nlp_model:
            self.nlp_model=nlp_model
        else:
            self.nlp_model=nlp

    def get_trigram_element(self,trigram_element):
        return '_'.join([str(element) for element in trigram_element.split('_')[:-1]])

    def get_trigrams(self,left_right_words):
        trigrams=[]
        for i in range(len(left_right_words.values())):
            right=list(left_right_words.values())[i]
            right_value=list(left_right_words.keys())[i]
            if right in left_right_words.keys():
                #if present, find index and the actual word
                left_indx=list(left_right_words.keys()).index(right)
                #right,left key, left value
                left_key=list(left_right_words.keys())[left_indx]
                left_value=left_right_words[left_key]
                trigrams.append(str(self.get_trigram_element(right_value))+'_'+str(self.get_trigram_element(left_key))+'_'+str(self.get_trigram_element(left_value)))
        return ' '.join([str(trigram) for trigram in trigrams])
    
    def get_SNgram(self):
        bigrams=[]
        word_list=[]

        left_right_words={}
        unique_pos={}
        unique_dep={}

        nlp_obj=self.nlp_model(self.text)

        for spacy_element in nlp_obj:
            #no same head and body
            if str(spacy_element.head)+str(spacy_element.head.idx)!=str(spacy_element)+str(spacy_element.idx):
                ##check type of concatenation between head and body with meta attributes
                if self.meta_tag=='dep':
                    bigrams.append(str(spacy_element.head)+'_'+spacy_element.head.dep_+'_'+str(spacy_element)+'_'+spacy_element.dep_)
                    left_right_words[str(spacy_element.head)+'_'+str(spacy_element.head.dep_)+'_'+str(spacy_element.head.idx)]=str(spacy_element)+'_'+str(spacy_element.dep_)+'_'+str(spacy_element.idx)
                elif self.meta_tag=='pos':
                    bigrams.append(str(spacy_element.head)+'_'+spacy_element.head.pos_+'_'+str(spacy_element)+'_'+spacy_element.pos_)
                    left_right_words[str(spacy_element.head)+'_'+str(spacy_element.head.pos_)+'_'+str(spacy_element.head.idx)]=str(spacy_element)+'_'+str(spacy_element.pos_)+'_'+str(spacy_element.idx)
                elif self.meta_tag=='original' or self.meta_tag=='':
                    bigrams.append(str(spacy_element.head)+'_'+str(spacy_element))
                    left_right_words[str(spacy_element.head)+'_'+str(spacy_element.head.idx)]=str(spacy_element)+'_'+str(spacy_element.idx)

        flat_bigrams=' '.join([str(bigram) for bigram in bigrams])
        
        result_dict={}
        result_dict['SNBigram']=flat_bigrams

        if self.trigram_flag=='yes':
            result_dict['SNTrigram']=self.get_trigrams(left_right_words)
            return result_dict
        else:
            return result_dict
        
if __name__=="__main__":
    text='Economic news have little effect on financial markets.'    
    SNgram_obj=SNgramExtractor(text,meta_tag='original',trigram_flag='yes',nlp_model=None)
    output=SNgram_obj.get_SNgram()
    print(text)
    print('SNGram bigram:',output['SNBigram'])
    print('SNGram trigram:',output['SNTrigram'])
    
    print('-----------------------------------')
    text='every cloud has a silver lining'
    SNgram_obj=SNgramExtractor(text,meta_tag='original',trigram_flag='yes',nlp_model=None)
    output=SNgram_obj.get_SNgram()
    print(text)
    print('SNGram bigram:',output['SNBigram'])
    print('SNGram trigram:',output['SNTrigram'])
