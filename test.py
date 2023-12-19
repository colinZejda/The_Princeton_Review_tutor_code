from itertools import permutations

def is_value_consistent(var, value, assignment, csp_table):
    for hexa in csp_table:
        if len(set([assignment[i] for i in hexa if i in assignment])) != len([assignment[i] for i in hexa if i in assignment]):
            return False
    return True

def select_unassigned_variable(assignment, csp_table):
    for var in range(24):
        if var not in assignment:
            return var

def recursive_backtracking(assignment, csp_table):
    if len(assignment) == 24 and check_complete(assignment, csp_table):  # Check if assignment is complete
        return assignment

    var = select_unassigned_variable(assignment, csp_table)
    for value in '123456':
        if is_value_consistent(var, value, assignment, csp_table):
            assignment[var] = value
            result = recursive_backtracking(assignment, csp_table)
            if result:
                return result  # Return the successful assignment
            del assignment[var]  # Remove var from assignment (backtrack)

    return None  # Trigger backtracking

# Other functions remain unchanged

# In your main function, you would call it like this:
def main():
    csp_table = # your definition here
    initial_assignment = {}  # or you can parse the input to fill in some values
    solution = recursive_backtracking(initial_assignment, csp_table)
    if solution:
        print(display(solution))
    else:
        print("It's not solvable.")

if __name__ == '__main__':
    main()
