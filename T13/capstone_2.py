import spacy
nlp = spacy.load('en_core_web_sm')

gardenpathSentences = ["I convinced her children are noisy.", 
                       "Because he always jogs a mile seems a short distance to him.", 
                       "Mary gave the child a band aid.", 
                       "That Jill is never here hurts.", 
                       "The cotton clothing is made of grows in Mississippi."]

for sentence in gardenpathSentences:
    doc = nlp(sentence)

    # Tokenisation
    # The text attribute, returns the actual text of the token as it appears in the document.
    tokens = [token.text for token in doc]
    print("Tokens:", tokens)


    # Named Entity Recognition
    for ent in doc.ents:
        print("Entity:",ent.text, "I Start", ent.start_char, "I End:", ent.end_char, "I Label", ent.label_)
        print("Explanation:", spacy.explain(ent.label_))

print("---")

'''"Entity:": This is a string indicating that the following text represents the entity detected.
ent.text: This prints out the text of the named entity.
"I Start": This is a string indicating that the following number represents the starting index of the named entity in the document.
ent.start_char: This prints out the starting index of the named entity.
"I End:": This is a string indicating that the following number represents the ending index of the named entity in the document.
ent.end_char: This prints out the ending index of the named entity.
"I Label": This is a string indicating that the following text represents the label (type) of the named entity.
ent.label_: This prints out the label (type) of the named entity.'''
