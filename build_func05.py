def main(n, x):
    """Integer type variables 'n' and 'x' are given. Return the value of the expression in README.md file.
    https://github.com/codeschool43/Build_in_function_homework#build_func05

    Args:
        n (int): integer
        x (int): integer
        
    Returns:
        int: the value of the expression
    """
    z = pow(x, n) + pow(n, x)

    return z

print(main(3, 6))