def get_search_list():
    '''Reads from the file and returns a list to search'''
    f = open('search_file.txt', 'r')
    search_list = f.readlines()
    return search_list

if __name__ == '__main__':
    pass
