import nltk
from nltk.sentiment import util
from nltk.sentiment import vader
from nltk.sentiment import sentiment_analyzer

def main():
    vader_result = open("vaderResults.txt", "r")
    input_file = open("commentsForLabeling.txt")
    manual_result = open("manualResults.txt")
    manual_result_write = open("manualResultsDuplicate.txt", "w")
    sentistrength_result_primary = open("result_SentiStrength.txt")
    sentistrength_result = open("sentistrengthResults.txt", "r")
    liuhu_result = open("liuhuResults.txt", "r")

    # test1 = [1, 3, -1, 2, -5, 0]
    # test2 = [1.1, 2.9, -1.2, 3.0, -4.2, 0.0]


    ### change file pointer to "w" mode in each of the following cases

    # find_liuhu_results(liuhu_result, input_file)
    # find_sentistrength_results(sentistrength_result_primary, sentistrength_result)
    # find_vader_results(vader_result, input_file)


    """
    Results:
        sentistrength accuracy: 39.0%
        liu_hu_lexicon accuracy: 48.8%
        vader_polarity accuracy: 52.2%
    """

    # find_accuracy(manual_result, sentistrength_result)         #one test in each run since file pointer manual_result needs to be renewed
    # find_accuracy(manual_result, liuhu_result)
    find_accuracy(manual_result, vader_result)


def find_accuracy(manual_result, predicted_result):
    correct = [l==r for(l, r) in zip(manual_result, predicted_result)]
    if correct:
        print(correct)
        print(str(sum(correct)/len(correct)))
    else:
        print("0")

def find_vader_results(vader_result, input_file):
    i=0

    for line in input_file:
        dict = nltk.sentiment.util.demo_vader_instance(line)
        if dict is not None:
            i += 1
            # print(str(dict['compound']))
            if dict['compound'] > 0.0:
                vader_result.write("Positive" + '\n')
            elif dict['compound'] < 0.0:
                vader_result.write("Negative" + '\n')
            elif dict['compound'] == 0.0:
                vader_result.write("Neutral" + '\n')
    print("Number of comments: " + str(i))

def find_sentistrength_results(sentistrength_result_primary, sentistrength_result):
    i=0

    for line in sentistrength_result_primary:
        if line is not None:
            i += 1
            # print(line)
            # print(str(dict['compound']))
            if int(line) > 0:
                sentistrength_result.write("Positive" + '\n')
            elif int(line) < 0:
                sentistrength_result.write("Negative" + '\n')
            elif int(line) == 0:
                sentistrength_result.write("Neutral" + '\n')
    print("Number of comments: " + str(i))

def find_liuhu_results(liuhu_result, input_file):
    i=0

    for line in input_file:
        sentiment = nltk.sentiment.util.demo_liu_hu_lexicon(line)
        if sentiment is not None:
            i += 1
            print(str(i))
            # print(str(dict['compound']))
            # vader_result.write(str(dict['compound']) + '\n')
            liuhu_result.write(sentiment+"\n")


    print("Number of comments: " + str(i))

if __name__ == '__main__':
    main()