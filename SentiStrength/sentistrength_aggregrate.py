import sys

def main():
    output_file = open("input+results.txt")
    result_file = open("result_SentiStrength.txt", "w")
    i=0
    for line in output_file:
        if(len(line.split()) < 3):                  #At least 3 entities - text, pos, neg
            continue
        text, pos, neg = line.split("\t")

        net = int(pos) + int(neg)
        result_file.write(str(net)+"\n")
        i+=1
    print(str(i))

if __name__ == '__main__':
    main()