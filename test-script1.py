def question_1():
    """
    Return the unique values from the following list [1, 2, 2, 1, 3, 3, 2]
    """
    my_list = [1, 2, 2, 1, 3, 3, 2]
    my_set = set(my_list)
    return my_set


if __name__ == '__main__':
    for num in range(1, 2):
        func = eval(f'question_{num}')
        question = ' '.join(func.__doc__.split())
        print(f'Question {num}: {question}')
        print(f'    {func()}\n\n')
