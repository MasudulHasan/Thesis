import sys

def main():
    output_file = open(sys.argv[1])
    result_file = open("result_SentiStrength.txt", "w")

    temp_sentiment_score = None
    text_status = None
    count = 0
    commentCount = 0

    for line in output_file:
        if(len(line.split()) < 3):                  #At least 3 entities - text, pos, neg
            continue
        text, pos, neg = line.split("\t")
        commentCount += 1
        # print(text)

        if line[0] == '"':
            temp_sentiment_score = None             #None = null
            final_sentiment_score = None
            text_status = "running"                 #text not completed yet

        # elif line[0] != '"' and text_status == None:
        #     print(text)

        if(temp_sentiment_score == None):           #New text
            temp_sentiment_score = int(pos) + int(neg)
            if(text[-1] == '"'):
                text_status = None
            if(text_status == None):
                final_sentiment_score = temp_sentiment_score
                temp_sentiment_score = None
        else:
            temp_sentiment_score += int(pos) + int(neg)
            if(text[-1] == '"'):                    #End of previous text
                final_sentiment_score = temp_sentiment_score
                temp_sentiment_score = None
                text_status = None                  #text completed


        if(final_sentiment_score != None):          #Sentiment score ready
            # print(str(final_sentiment_score))
            count += 1
            result_file.write(str(final_sentiment_score)+'\n')

    print(commentCount)

if __name__ == '__main__':
    main()