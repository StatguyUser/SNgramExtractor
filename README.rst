What is it?
===========

Companion library of machine learning book [Feature Engineering & Selection for Explainable Models A Second Course for Data Scientists](https://statguyuser.github.io/feature-engg-selection-for-explainable-models.github.io/index.html)

SNgramExtractor module helps extract Syntactic relations (SR tags) as elements of sn-grams. 

We follow the path marked by the arrows in the dependencies and obtain sngrams.[1]

The advantage of syntactic n-grams (SN-grams), i.e., n-grams that are constructed using paths in syntactic trees, is that they are less arbitrary than traditional n-grams. Thus, their number is less than the number of traditional n-grams. Besides, they can be interpreted as linguistic phenomenon, while traditional n-grams have no plausible linguistic interpretation they are merely statistical artifact. [1]

SN-gram has usability across many natural language processing application areas, such as classification tasks in machine learning[2], information extraction[3], query understanding[4], machine translation[5], question answering systems[6]

Input parameters
================

  - **text** input text as a single sentence.
  - **meta_tag** Resultant bigram and trigram should be concatenated with part of speech tag('pos') or dependency tag('dep') or original SN-gram('original')
  - **trigram_flag** if we need to include trigrams derived from SN-grams as well ('yes') or not ('no'). Default is 'yes'
  - **nlp_model** Specify the spacy language model you want to use. Default is spacy English language model en_core_web_sm. This is useful for being able to use languages other than english.

Output
================

Dictionary object with key value pairs for bigram and trigram derived from SN-gram.

  - **SNBigram** dictionary key for bigram derived from SN-gram
  - **SNTrigram** dictionary key for trigram derived from SN-gram

How to use is it?
=================

```python

from SNgramExtractor import SNgramExtractor

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

print('-----------------------------------')
nlp_french = spacy.load('fr_core_news_sm')
text='Je voudrais réserver un hôtel à Rennes.'
SNgram_obj=SNgramExtractor(text,meta_tag='original',trigram_flag='yes',nlp_model=nlp_french)
output=SNgram_obj.get_SNgram()    
print(text)
print('SNGram bigram:',output['SNBigram'])
print('SNGram trigram:',output['SNTrigram'])

```

Where to get it?
================

`pip install SNgramExtractor`

How to cite?
================

Md Azimul Haque (2022). Feature Engineering & Selection for Explainable Models A Second Course for Data Scientists

Dependencies
============

 - [spacy](https://spacy.io/)
 - [spacy model en_core_web_sm](https://github.com/explosion/spacy-models/releases/download/en_core_web_sm-2.2.0/en_core_web_sm-2.2.0.tar.gz)

References
============

1. [Syntactic Dependency-Based N-grams as Classification Features](http://www.icsd.aegean.gr/lecturers/stamatatos/papers/MICAI2012.pdf) by Grigori Sidorov , Francisco Velasquez, Efstathios Stamatatos, Alexander Gelbukh and Liliana Chanona-Hernández
2. [Syntactic N-grams as Machine Learning Features for Natural Language Processing](http://www.cic.ipn.mx/~sidorov/Synt_n_grams_ESWA_FINAL.pdf) by Grigori Sidorov , Francisco Velasquez, Efstathios Stamatatos, Alexander Gelbukh and Liliana Chanona-Hernández
3. [Dependency-Based Open Information Extraction](http://www.anthology.aclweb.org/W/W12/W12-0702.pdf) by Pablo Gamallo, Marcos Garcia and Santiago Fernandez-Lanza
4. [Query Understanding Enhanced By Hierarchical Parsing Structures](https://groups.csail.mit.edu/sls/publications/2013/Liu_ASRU_2013.pdf) by Jingjing Liu, Panupong Pasupat, Yining Wang, Scott Cyphers, and Jim Glass
5. [Dependency Structure Trees in Syntax Based Machine Translation](http://www.cs.cmu.edu/~vamshi/publications/DependencyMT_report.pdf) by Vamshi Ambati
6. [Question Answering Passage Retrieval Using Dependency Relations](https://www.comp.nus.edu.sg/~kanmy/papers/f66-cui.pdf) by Hang Cui, Renxu Sun, Keya Li, Min-Yen Kan and Tat-Seng Chua
