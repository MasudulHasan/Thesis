import sys

def main():
    output_file = open("comment.txt")
    result_file = open("commentsForLabeling.html", "w")

    i=1

    for line in output_file:
        if(len(line.split()) < 3):                  #At least 3 entities - text, pos, neg
            continue
        text, pos, neg = line.split("\t")
        update = "<p>" + str(i) + ". " + text + "</p>"
        i += 1

        result_file.write(update)


if __name__ == '__main__':
    main()