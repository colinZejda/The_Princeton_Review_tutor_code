# your current code
def synth_alg(coeff, root):
    result = []
    n = len(coeff)
    temp = coeff[0]
    result.append(temp)
    for i in range(1, n):
        temp = temp * root + coeff[i]# The synthetic division with jsut numbers
        result.append(temp)
    output = ""
    for i in range(0, n - 1):
        if result[i] != 0:
            if result[i] > 0 and i > 0:
                output += " + "# if pos add and nto the first term
            elif result[i] < 0:
                output += " - "# if neg subtract
            if abs(result[i]) != 1 or n - 1 - i == 0:# determine if coefficient not 1 or 0
                output += str(abs(result[i]))
            if n-i-3==0:
                output+="x"# extra line just for format so 5x^1 is 5x and -3 because 1 for ^0 and another fro remainder
            if n-i-3 > 0:
                output += "x"
                output += "^" + str(n - 2 - i)#power of
    remainder = temp
    if remainder != 0: # not 0 so not no reminder then add remainder/root
        if remainder > 0:
            output += " + "
        elif remainder < 0:
            output += " - "
        output += str(abs(remainder)) + " / (x - " + str(root) + ")"
    return output
# Test cases
test1 = [2, 11, 15]
root1 = -3
print(synth_alg(test1, root1))  # Output: "2x + 5"
test2 = [1, -3, 5, -17, 6]
root2 = 3
print(synth_alg(test2, root2))  # Output: "x^3 + 5x - 2"
test3 = [1, -5, 7, -34, -1]
root3 = 5
print(synth_alg(test3, root3))  # Output: "x^3 + 7x + 1 + 4 / (x - 5)"
test4 = [2, 6, 5, 0, -44]
root4 = -3
print(synth_alg(test4, root4))  # Output: "2x^3 + 5x - 15 + 1 / (x + 3)"


def evaluate(poly):
    numerator, denominator = poly.strip("()").split(") / (")
    numerator_terms = numerator.replace("-", "+-").split("+")

    coefficients = []
    for term in numerator_terms:
        if "x" in term:
            coefficient, power = term.split("x")
            if coefficient == '' or coefficient == '+':
                coefficient = '1'
            elif coefficient == '-':
                coefficient = '-1'
            if power.startswith("^"):
                power = power.lstrip("^")
            else:
                power = '1'  # For terms like 'x'
            coefficients.append((coefficient, power))
        else:
            # Handling constant terms without x
            coefficients.append((term, '0'))

    expression = " + ".join([f"{coef}x^{pow}" if pow != '0' else coef for coef, pow in coefficients])
    return expression

# Test case
poly = "(2x^2 + 11x + 15) / (x + 3)"
print(evaluate(poly))
#  "2x + 5"


def evaluate(poly):
    numerator, denominator = poly.strip("()").split(") / (")
    numerator_terms = numerator.replace("-", "+-").split("+")

    coefficients = []
    for term in numerator_terms:
        if "x" in term:
            coef, pwr = term.split("x")
            if coef == '' or coef == '+':
                coef = '1'
            elif coef == '-':
                coef = '-1'
            if pwr.startswith("^"):
                pwr = pwr.lstrip("^")
            else:
                pwr = '1'
            coef.append((coef, pwr))
        else:
            coef.append((term, '0'))

    # put it all back together
    expression = " + ".join([f"{c}x^{pow}" if pow != '0' else c for c, pow in coefficients])
    return expression