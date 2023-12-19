def approx_pi(iterations):
  
    # initialzations
    pi = 3.0
    s = 1.0        # sign, flips every loop
      
    # loop over iterations
    for i in range(1, iterations+1):
        
        # perform computations per loop
        to_add = 4 / (2*i * (2*i + 1) * (2*i + 2))
        pi += s * to_add
        
        # update variables (flip sign)
        s *= -1
	
    # done with loop here, return pi
    return round(pi, 10)
  
  
  
# prof flowchar-- need a main function
def main():
	# call the function on dif iteration values
    values_to_test = [200, 500, 1000]
    for value in values_to_test:
      
        # inside loop, call approx_pi
        # then print result
        result = approx_pi(value)
        print(f"The value of \u03C0 is {result} when i = {value}")
    
    
# run main 
if __name__ == "__main__":
    main()
