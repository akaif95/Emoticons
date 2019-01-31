'''
Description:

This program contains functions that will find values associated with
twitter emoticons, as well as finding the most common ones used on Twitter >
'''




def load_twitter_dicts_from_file(filename, emoticons_to_ids, ids_to_emoticons):
    emoticons_file = open(filename, "r")

    for line in emoticons_file:
        data = line.strip().split('"')

        if data[1] not in emoticons_to_ids:
            emoticons_to_ids[data[1]] = []
        emoticons_to_ids[data[1]].append(data[3])
        if data[3] not in ids_to_emoticons:
            ids_to_emoticons[data[3]] = []
        ids_to_emoticons[data[3]].append(data[1])

    emoticons_file.close()
        

    
def find_most_common(some_dictionary):
    data_length = 0
    max_key = ""
    for key in some_dictionary:
        if len(some_dictionary[key]) > data_length:
            data_length = len(some_dictionary[key])
            max_key = key

    print(max_key.ljust(21, " ") + "occurs" + str(data_length).rjust(9, " ") + " times")
    return max_key


#==========================================================
def main():
    emoticons_to_ids = {}
    ids_to_emoticons = {}

    load_twitter_dicts_from_file("twitter_emoticons.dat", emoticons_to_ids, ids_to_emoticons)

    print("Emoticons: " + str(len(emoticons_to_ids.keys())))
    print("UserIDs:   " + str(len(ids_to_emoticons.keys())))


    for i in range(0, 5):
        magic_key = find_most_common(emoticons_to_ids)
        emoticons_to_ids.pop(magic_key)



