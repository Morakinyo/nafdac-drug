import pandas
from fuzzywuzzy import fuzz

def simi(input_list):
    for i in range(len(input_list)):
        for j in range(len(input_list)):
            if i < j and fuzz.ratio(input_list[i], input_list[j]) >= 90:
                input_list[i] = input_list[j] # Keep the last encountered item
                # use following line to keep the first encountered item
                #input_list[j] = input_list[i]