def main(x, y):
    """Integer type variables 'x' and 'y' are given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func10

    Args:
        x (int): integer
        y (int): integer
        
    Returns:
        int: the value of the expression
    """

    a = 3 * pow(y,  0.5) + pow(x, 2/3)
    a = round (a, 1)
    return a

print(main(8, 4))