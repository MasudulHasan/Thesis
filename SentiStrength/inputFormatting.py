import sys

def main():
    input_file = open(sys.argv[1])
    output_file = open("input.txt", "w")

    for line in input_file:
        l = ' '.join(line.split())
        l += '\n'
        # print(str(len(l.split())))
        output_file.write(l)


if __name__ == '__main__':
    main()