# Read text from a file, and count the occurence of words in that text
# Example:
# count_words("The cake is done. It is a big cake!") 
# --> {"cake":2, "big":1, "is":2, "the":1, "a":1, "it":1}
file = "./story.txt"
def read_file_content(filename):
    # [assignment] Add your code here 
    with open(filename,"r") as file:
        data = file.read()
    return data


print(read_file_content(file))

def count_words():
    text = read_file_content("./story.txt")
    # [assignment] Add your code here
    split_text = text.split()

    count = {}
    for i in split_text:
        if i in count:
            count[i] += 1
        else:
            count[i] =1
    return count

print(count_words())