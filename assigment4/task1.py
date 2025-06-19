l=1 # for print line number
try:
    with open('sample.txt', 'r') as file:
        for line in file:
            print("Line",l,": ",line, end='')  # end='' to avoid extra newlines since line already contains one
            l=l+1
except FileNotFoundError:
    print("Error: The file 'sample.txt' does not exist.")
except IOError:
    print("Error: An I/O error occurred while trying to read the file.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")