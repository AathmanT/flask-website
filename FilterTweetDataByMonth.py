import json
import re
import nltk
from nltk.stem.wordnet import WordNetLemmatizer
from nltk.corpus import stopwords
import os
from gensim import corpora, models, similarities

import cProfile, pstats, io

def profile(fnc):
    """A decorator that uses cProfile to profile a function"""

    def inner(*args, **kwargs):
        pr = cProfile.Profile()
        pr.enable()
        retval = fnc(*args, **kwargs)
        pr.disable()
        s = io.StringIO()
        sortby = 'cumulative'
        #ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
        ps = pstats.Stats(pr).sort_stats(sortby)
        ps.print_stats()
        #print(s.getvalue())
        return retval

    return inner

@profile
def preprocess(tweets_data_path,selected_year,time_stamps):
    # Reading Tweets
    print('Reading Tweets\n')
    #tweets_data_path = 'output.txt'

    n=0
    #selected_year="2019"
   # time_stamps = ['Jan','Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct', 'Nov', 'Dec']
    #time_stamps = [ 'May']

    conference = 'tourism'

    dat_outfile = open(os.path.join('data', conference, 'metadata.dat'), 'w')
    dat_outfile.write('id\tdate\tcontent\n')  # write header

    tweets = list()

    total_tweets_list = [0 for year in time_stamps]

    time_stamps_count = 0

    content_list=""

    tweets_file = open(tweets_data_path, "r")
    for line in tweets_file:
        print(line)
        try:

            tweet = json.loads(line)
            twitter_id = tweet["id"]
            created_at_list=tweet["created_at"].split(" ")
            created_at=created_at_list[1]
            year=created_at_list[-1]
            text=tweet["text"]

            try:
                index=time_stamps.index(created_at)

                if(index>=0 and selected_year==year):
                    # Remove @xxxx and #xxxxx
                    content = [word.lower() for word in text.split() if
                               word.find('@') == -1 and word.find('#') == -1 and word.find('http') == -1]

                    # join words list to one string
                    content = ' '.join(content)

                    # remove symbols
                    content = re.sub(r'[^\w]', ' ', content)

                    # remove stop words
                    content = [word for word in content.split() if
                               word not in stopwords.words('english') and len(word) > 3 and not any(
                                   c.isdigit() for c in word)]

                    # join words list to one string
                    content = ' '.join(content)

                    # Stemming and lemmatization
                    lmtzr = WordNetLemmatizer()

                    content = lmtzr.lemmatize(content)

                    # Filter only nouns and adjectives
                    tokenized = nltk.word_tokenize(content)
                    classified = nltk.pos_tag(tokenized)

                    content = [word for (word, clas) in classified if
                               clas == 'NN' or clas == 'NNS' or clas == 'NNP' or clas == 'NNPS' or clas == 'JJ' or clas == 'JJR' or clas == 'JJS']
                    # join words list to one string
                    content = ' '.join(content)

                    if len(content) > 0:
                        n+=1
                        tweets.append([twitter_id, content, created_at])

                        total_tweets_list[index] += 1


                        dat_outfile.write(str(twitter_id) + '\t' + str(created_at) + '\t' + content)
                        dat_outfile.write('\n')
            except ValueError:
                continue
        except Exception as e:
            print(e)
            continue

    dat_outfile.close()  # Close the tweets file

    if(n!=0):
        # Write seq file
        seq_outfile = open(os.path.join('data', conference, 'foo-seq.dat'), 'w')
        seq_outfile.write(str(len(total_tweets_list)) + '\n')  # number of TimeStamps

        for count in total_tweets_list:
            seq_outfile.write(str(count) + '\n')  # write the total tweets per year (timestamp)

        seq_outfile.close()

        print('Done collecting tweets and writing seq')

        # Transform each tweet content to a vector.

        stoplist = set('for a of the and to in'.split())

        # Construct the dictionary

        dictionary = corpora.Dictionary(line[1].lower().split() for line in tweets)

        # remove stop words and words that appear only once
        stop_ids = [dictionary.token2id[stopword] for stopword in stoplist
                    if stopword in dictionary.token2id]
        once_ids = [tokenid for tokenid, docfreq in dictionary.dfs.iteritems() if docfreq == 1]
        dictionary.filter_tokens(stop_ids + once_ids)  # remove stop words and words that appear only once
        dictionary.compactify()  # remove gaps in id sequence after words that were removed

        dictionary.save(os.path.join('data', conference, 'dictionary.dict'))  # store the dictionary, for future reference

        # Save vocabulary
        vocFile = open(os.path.join('data', conference, 'vocabulary.dat'), 'w')
        for word in dictionary.values():
            vocFile.write(word + '\n')

        vocFile.close()

        print('Dictionary and vocabulary saved')


        # Prevent storing the words of each document in the RAM
        class MyCorpus(object):
            def __iter__(self):
                for line in tweets:
                    # assume there's one document per line, tokens separated by whitespace
                    yield dictionary.doc2bow(line[1].lower().split())


        corpus_memory_friendly = MyCorpus()

        multFile = open(os.path.join('data', conference, 'foo-mult.dat'), 'w')

        for vector in corpus_memory_friendly:  # load one vector into memory at a time
            multFile.write(str(len(vector)) + ' ')
            for (wordID, weigth) in vector:
                multFile.write(str(wordID) + ':' + str(weigth) + ' ')

            multFile.write('\n')

        multFile.close()

        print('Mult file saved')
        return True
    else:
        return False




preprocess("output.txt","2019", time_stamps = ['Jan','Feb', 'Mar','Apr','May','Jun','Jul','Aug','Sep','Oct', 'Nov', 'Dec'])

















































if __name__ == '__main__':
    main()
