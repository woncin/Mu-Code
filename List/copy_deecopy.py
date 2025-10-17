import copy

def update_spam(param):
    return param.append('a')

spam = [1, 2, 3]

new_spam = copy.copy(spam)

update_spam(new_spam)
