def format_name(full_name):
    # Split the full name by spaces
    name_parts = full_name.strip().split()

    # Check if the name has a middle name or not
    if len(name_parts) == 3:
        # If there's a middle name, format accordingly
        formatted_name = f"{name_parts[2]}, {name_parts[0][0]}.{name_parts[1][0]}."
    elif len(name_parts) == 2:
        # If there's no middle name, format accordingly
        formatted_name = f"{name_parts[1]}, {name_parts[0][0]}."
    else:
        # If the name format is not recognized, return an error message
        formatted_name = "Invalid name format."
    
    return formatted_name

# Test the function with the given examples
example_1 = "Pat Silly Doe"
example_2 = "Julia Clark"

formatted_example_1 = format_name(example_1)
formatted_example_2 = format_name(example_2)

formatted_example_1, formatted_example_2
