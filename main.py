#PROBLEM:
# Write a program that prints the numbers from 1 to n. For multiples of three, print "Fizz" instead of the number, and for multiples of five, print "Buzz". For multiples of both three and five, print "FizzBuzz".


# Check for Fizz
def IsFizz(number: int) -> bool:
  return True if number % 3 == 0 else False


# Check for Buzz
def IsBuzz(number: int) -> bool:
  return True if number % 5 == 0 else False


# Main function
def main():
  # Ask user for the number should we start
  try:
    num = int(input("Please enter your starting number: "))
    if num > 0:
      for i in range(1, num + 1):
        if IsFizz(i) and IsBuzz(i):
          print("FizzBuzz")
        elif IsFizz(i):
          print("Fizz")
        elif IsBuzz(i):
          print("Buzz")
        else:
          print(i)
  except ValueError:
    print("Anything except numbers are prohibited")

# Application Start
if __name__ == "__main__":
  main()
