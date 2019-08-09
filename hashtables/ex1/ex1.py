#  Hint:  You may not need all of these.  Remove the unused functions.
from hashtables import (HashTable, hash_table_insert, hash_table_retrieve,)


def get_indices_of_item_weights(weights, length, limit):
    ht = HashTable(16)  # hash table with 16 boxes
    for item in range(length):  # loops through it
        weight = weights[item]  # weight of items
        item_index = item  # index of items
        l_w_difference = limit - weight  # limit / weight difference
        # is there a weight as a key in the hash_table?
        if hash_table_retrieve(ht, weight) is not None:
            print("Matching Keys Found")
            answer = (item_index, hash_table_retrieve(
                ht, l_w_difference))  # get the key and hash it
            return answer  # return the hashed key
        else:  # if there isnt a weight as a key
            # insert the weight as a key and the item index as a value
            hash_table_insert(ht, weight, item_index)
            print(f'{weight} - was inserted at the index: {item}')
            # if the limit / weight difference is already key in hash table
            if hash_table_retrieve(ht, l_w_difference):
                matching_keys = hash_table_retrieve(
                    ht, l_w_difference)  # stored above in new variable
                answer = (item_index, matching_keys)
                return answer
            else:  # if the l_w_difference isnt a already a key
                answer = None  # set it to none
                print("No Matching Keys Found")

    return None


def print_answer(answer):
    if answer is not None:
        print(str(answer[0] + " " + answer[1]))
    else:
        print("None")
