import sys
import nltk
from nltk.sentiment import util
from nltk.sentiment import vader
from nltk.sentiment import sentiment_analyzer

scores = []
polarities = []
subjectivity = []

def main():
    input_file = open("comment.txt")
    result_file = open("commentsForLabeling.txt", "w")
    test_file = open("commentsForLabeling.txt", "r")
    features_file = open("features.txt", "w")


    for line in input_file:
        if(len(line.split()) < 3):                  #At least 3 entities - text, pos, neg
            continue
        text, pos, neg = line.split("\t")

        result_file.write(text)
        result_file.write(' \n')

    i = 0

    for line in test_file:
        if(line == ''):
            continue

        sentences = line.split('.')
        polarity_score = 0
        i += 1

        for j in sentences:

            try:
                k, l = j.split(' but ')
                print(str(i) + ". " + str(k))
                kpolarity = case_of_but(k)
                print(str(i) + ". " + str(l))
                lpolarity = case_of_but(l)

                if kpolarity>0 and lpolarity<0:     #postive but negative
                    print('Negative overall')
                elif kpolarity<0 and lpolarity>0:   #negative but positive
                    print('Positive overall')

                polarity_score += lpolarity          #The sentiment after but is considered in every case


                continue
            except:
                pass

            print(str(i) + ". " + j + "\n")

            if addScore(j) is not None:
                print("demo_vader_instance: " + addScore(j))

            if nltk.sentiment.util.demo_sent_subjectivity(j) is not None:
                print("demo sent subjectivity: " + str(nltk.sentiment.util.demo_sent_subjectivity(j)))

            negation = nltk.sentiment.vader.negated(j)
            if negation is not None:
                print("vader negated: " + str(negation))

            polarity = nltk.sentiment.util.demo_liu_hu_lexicon(j)
            if polarity is not None and polarity == 'Positive':
                if negation is True:
                    print("demo liu hu lexicon: " + 'Negative')
                    polarity_score -= 1
                else:
                    print("demo liu hu lexicon: " + 'Positive')
                    polarity_score += 1

            elif polarity is not None and polarity == 'Negative':
                if negation is False:
                    print("demo liu hu lexicon: " + 'Negative')
                    polarity_score -= 1
                else:
                    print("demo liu hu lexicon: " + 'Positive')
                    polarity_score += 1

            elif polarity is not None:
                print(polarity)

        scores.append(polarity_score)

        features_file.write(str(i) +". " + str(polarity_score))
        # print(sia.)


        # addScore(line)
        # addPolarity(line)
        # determineSubjectivity(line)
        # result_file.write(str(scores[i]))
        # i = i+1




def addScore(line):
    scores.append(nltk.sentiment.util.demo_vader_instance(line))

def case_of_but(j):
    polarity_score = 0
    if addScore(j) is not None:
        print("demo_vader_instance: " + addScore(j))
    # if sia.polarity_scores(line) is not None:
    #     print("sia polarity scores: " + str(sia.polarity_scores(line)))

    if nltk.sentiment.util.demo_sent_subjectivity(j) is not None:
        print("demo sent subjectivity: " + str(nltk.sentiment.util.demo_sent_subjectivity(j)))

    negation = nltk.sentiment.vader.negated(j)
    if negation is not None:
        print("vader negated: " + str(negation))

    polarity = nltk.sentiment.util.demo_liu_hu_lexicon(j)
    if polarity is not None and polarity == 'Positive':
        if negation is True:
            print("demo liu hu lexicon: " + 'Negative')
            polarity_score -= 1
        else:
            print("demo liu hu lexicon: " + 'Positive')
            polarity_score += 1

    elif polarity is not None and polarity == 'Negative':
        if negation is False:
            print("demo liu hu lexicon: " + 'Negative')
            polarity_score -= 1
        else:
            print("demo liu hu lexicon: " + 'Positive')
            polarity_score += 1

    elif polarity is not None:
        print(polarity)

    return polarity_score

if __name__ == '__main__':
    main()