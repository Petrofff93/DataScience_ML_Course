"""
**You are driving a little too fast, and a police officer stops you.
Write a function to return one of 3 possible results: “No ticket”, “Small ticket”, or “Big Ticket”.
If your speed is 60 or less, the result is “No Ticket”. If speed is between 61 and 80 inclusive,
the result is “Small Ticket”. If speed is 81 or more, the result is “Big Ticket”.
Unless it is your birthday (encoded as a boolean value in the parameters of the function) – on your birthday,
your speed can be 5 higher in all cases. **
"""


def caught_speeding(speed, is_birthday):
    speed_cases = {
        'No ticket': [60],
        'Small ticket': [61, 80],
        'Big ticket': [81]
    }

    if is_birthday:
        for key, value in speed_cases.items():
            speed_cases[key] = [x + 5 for x in value]

    for k, v in speed_cases.items():
        if k == 'No ticket':
            if speed <= v[0]:
                return k

        elif k == 'Small ticket':
            if v[0] <= speed <= v[1]:
                return k

        elif k == 'Big ticket':
            return k


print(caught_speeding(81, False))
print(caught_speeding(81, True))
print(caught_speeding(64, True))
print(caught_speeding(64, False))
