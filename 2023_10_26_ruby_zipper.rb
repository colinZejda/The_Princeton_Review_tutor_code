Write in a declarative style (that is, using no assignment statements of any kind) a Ruby function zipper that accepts two arrays as arguments and returns an array that is an interleaving of the argument arrays. For instance, if zipper is passed the arrays [1,2] and [3,4,5], it should return the array [1,3,2,4,5]. As a second example, if it is passed [3,4,5,6] and [1,2] then it should return [3,1,4,2,5,6]. In general, it should return the array consisting of the first element of the first array, the first element of the second array, the second element of the first array, the second element of the second array, and so on, until one of the arrays is exhausted at which point the returned array ends with what remains of the other array (if anything).

NOTE: No points unless this program is written in a declarative style.

Hints: We wrote a Ruby function in declarative style in class as a collaborative learning exercise; this might be a good starting point. That function depended on recursion. We also wrote a rest method for the Ruby Array class that you might want to use in your code (my solution uses it). I've included it, but feel free to remove it if you don't want to use it.

You can find documentation of the Ruby Array class at https://ruby-doc.org/core-3.0.2/Array.html. You might find methods such as length() helpful.

class Array
  # Return an array consisting of all but the first 
  # element of this array.
  # For instance, [1,2,3].rest() returns [2,3].
  # Also, [1].rest() returns [] (the empty array).
  def rest()
    self[1..-1]
  end
end

def zipper(arr1, arr2)
  # YOUR CODE GOES BELOW THIS LINE 
  return arr2 if arr1.empty?          # base cases
  return arr1 if arr2.empty?
    
  [arr1.first, arr2.first] + zipper(arr1.rest, arr2.rest)  # recursive step
end

print(zipper([1,2], [3,4,5]), "\n")    # Should print [1,3,2,4,5]
print(zipper([3,4,5,6], [1,2]), "\n")  # Should print [3,1,4,2,5,6]

   
   Traceback (most recent call last):
    4: from main.rb:19:in `<main>'
    3: from main.rb:14:in `zipper'
    2: from main.rb:14:in `zipper'
    1: from main.rb:14:in `zipper'
main.rb:13:in `zipper': undefined method `empty?' for nil:NilClass (NoMethodError)
