import sys
import re

def main():
    input_file = open(sys.argv[1])
    output_file = open("input.txt", "w")

    for line in input_file:
        # l = ' '.join(line.split())

        """
        extract comments from <p> tags and bundle them together
        """

        # cleanr = re.compile('<.*?>')
        # l = re.sub(cleanr,'', l)

        # l.strip("<p>")
        # l += '\n'
        # print(str(len(l.split())))
        print("New: " + line)
        output_file.write(line)


if __name__ == '__main__':
    main()