# Define a function called fibonacci_search that takes four arguments:
# - f: The objective function to be minimized
# - a: The lower bound of the search interval
# - b: The upper bound of the search interval
# - n: The number of iterations or steps to perform the search
# - ϵ: A optional parameter for the minimum acceptable step size (default is 0.01)
function fibonacci_search(f, a, b, n; ϵ=0.01)
    # Calculate the constant s used in the Fibonacci search formula
    s = (1-√5)/(1+√5)
    
    # Calculate the initial value of the parameter ρ using the Fibonacci formula
    φ = (1+√5)/2
    ρ = 1 / (φ*(1-s^(n+1))/(1-s^n))
    
    # Calculate the initial point d in the search interval
    d = ρ*b + (1-ρ)*a
    yd = f(d)  # Evaluate the objective function at point d
    
    # Iterate for n-1 steps
    for i in 1 : n-1
        if i == n-1
            # If it's the last iteration, calculate point c with a smaller step size ϵ
            c = ϵ*a + (1-ϵ)*d
        else
            # Calculate point c using the current ρ value
            c = ρ*a + (1-ρ)*b
        end
        yc = f(c)  # Evaluate the objective function at point c
        
        # Compare the objective function values at c and d to update the search interval
        if yc < yd
            b, d, yd = d, c, yc
        else
            a, b = b, c
        end
        
        # Update ρ for the next iteration using the Fibonacci formula
        ρ = 1 / (φ*(1-s^(n-i+1))/(1-s^(n-i)))
    end
    
    # Return the result as a tuple containing the updated search interval (a, b)
    return a < b ? (a, b) : (b, a)
end
