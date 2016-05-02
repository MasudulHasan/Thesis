import sys

def main():
    result = open("result_SentiStrength.txt", "r")
    print (str(len(result.readlines())))

if __name__ == '__main__':
    main()