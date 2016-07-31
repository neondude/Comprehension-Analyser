# Comprehension Analyser V1.0
- Comprhension Analyser v1.0 is a basic comprehension passage test application.
- This version has one static test page with seperate timer for reading the passage and questions.
- Definitions of word can be viewed by clicking on the word(if highlighted)

# Prerequisites
## 1)Flask
    pip install flask
## 2)wordnet
>#### Steps to install wordnet module
    pip install -U nltk
    import nltk 
    nltk.download() 
>* select **CORPA** tab
>* select **wordnet** and download

## 3)Browser
#### - Chrome recommended
# Instructions
- Run **app.py** 
- Start your browser and open **http://localhost:5000/1**
- Click **Begin Test** to start the test
- Read the passage and click the **questions** tab to answer the questions related to the passage
- To view the definition of a word hover over the word and if definition is available the word will he highlighted. Click to view definition
- Click Submit once you've answered all your questions to view your **score** and **reading speed**

# Descriptions
# wordnet
>- WordNet® is a large lexical database of English. Nouns, verbs, adjectives and adverbs are grouped into sets of cognitive synonyms (synsets), each expressing a distinct concept. 
>- Learn more at [Wordnet Princeton](https://wordnet.princeton.edu/)

# ParaCompile.py
>### ParaCompile(string) 
>>* used to compile a html format passage with definitions contained in **bootstrap popover attribute**
>>* retruns the given passage in html format where each word whose definition, if available, is contained within 'a' tag with **bootstrap popover attribute** containing the definitions.

# wordDefine.py
>* program to return a list of definitions for the given word if available
>### example
>
        python wordDefine.py
        enter a word: hello
        an expression of greeting