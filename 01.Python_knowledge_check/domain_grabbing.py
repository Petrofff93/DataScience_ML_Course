#  Create a function that grabs the email website domain from a string in the form


def get_domain(some_str):
    """
    We could for loop through the indexes and use splicing to return the needed data.
    """
    idx = 0

    for i in range(len(some_str)):
        if some_str[i] == '@':
            idx = i
            break

    return some_str[idx + 1:]


example_string = 'user@domain.com'
print(get_domain(example_string))
