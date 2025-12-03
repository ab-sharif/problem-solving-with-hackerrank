def mutate_string(string, position, character):
    my_list = list(string)
    my_list[position] = character
    final_list = ''.join(my_list)
    return final_list

    return

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)