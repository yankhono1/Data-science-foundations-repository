import spacy

# Takes the Hulk description and a list of movies as input. 
# It then calculates the similarity between the description and each movie using SpaCy's similarity metric.
 
def find_most_similar_movie(description_to_compare, movies):
    # Load the English model with word vectors
    nlp = spacy.load('en_core_web_md')

    model_description = nlp(description_to_compare)

    max_similarity = -1
    recommended_movie = ''

    # Loop through sentences in the movies to find out the similarity
    # Check if current similarity is higher than the maximum similarity found so far
    for sentence in movies:
        similarity = nlp(sentence).similarity(model_description)
        print(sentence + " - Similarity: " + str(similarity))
        if similarity > max_similarity:
            max_similarity = similarity
            recommended_movie = sentence

    # Print the recommended movie name, without the description [0] 
    return recommended_movie.split(':')[0]

description_to_compare = 'Will he save their word or destroy it? When the Hulk becomes too dangerous for the earth the illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator.'

movies = ['Movie A :When Hiccup discovers Toothless isn\'t the only Night Fury, he must seek The Hidden World, a secret Dragon Utopia before a hired tyrant named Grimmel finds it first.',
          'Movie B :After the death of Superman, several new people present themselves as possible successors.',
          'Movie C :A darkness swirls at the center of a world-renowned dance company, one that will engulf the artistic director, an ambitious young dancer, and a grieving psychotherapist. Some will succumb to the nightmare. Others will finally wake up.',
          'Movie D :A humorous take on Sir Arthur Conan Doyles classic mysteries featuring Sherlock Holmes and Doctor Watson.',
          'Movie E :A 16-year-old girl and her extended family are left reeling after her calculating grandmother unveils an array of secrets on her deathbed.',
          'Movie F :In the last moments of World War II, a young German soldier fighting for survival finds a Nazi captains uniform. Impersonating an officer, the man quickly takes on the monstrous identity of the perpetrators he is trying to escape from.',
          'Movie G :The world at an end, a dying mother sends her young son on a quest to find the place that grants wishes.',
          'Movie H :A musician helps a young singer and actress find fame, even as age and alcoholism send his own career into a downward spiral.',
          'Movie I :Corporate analyst and single mom, Jen, tackles Christmas with a business-like approach until her uncle arrives with a handsome stranger in tow.',
          'Movie J :Adapted from the bestselling novel by Madeleine St John, Ladies in Black is an alluring and tender-hearted comedy drama about the lives of a group of department store employees in 1959 Sydney.']

recommended_movie = find_most_similar_movie(description_to_compare, movies)
print("\nRecommended movie:", recommended_movie)
