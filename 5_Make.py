
def steps_to_miles(steps):
    if steps < 0:
        raise ValueError("Exception: Negative step count entered.")
    return steps / 2000

if __name__ == '__main__':
    try:
        steps = int(input("Enter number of steps: "))
        miles = steps_to_miles(steps)
        print(f'{miles:.2f}')
    except ValueError as e:
        print(e)
