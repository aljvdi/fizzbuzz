#PROBLEM:
# Write a program that prints the numbers from 1 to n. For multiples of three, print "Fizz" instead of the number, and for multiples of five, print "Buzz". For multiples of both three and five, print "FizzBuzz".

from colorama import Fore
from os import system


# Check for Fizz
def IsFizz(number: int) -> bool:
  return True if number % 3 == 0 else False


# Check for Buzz
def IsBuzz(number: int) -> bool:
  return True if number % 5 == 0 else False


# Clear screen
def clear():
  system("clear")


# Main function
def main():
  # Ask user for the number should we start
  try:
    num = int(input("Please enter your starting number: "))
    if num > 0:
      clear()
      for i in range(1, num + 1):
        if IsFizz(i) and IsBuzz(i):
          print(Fore.CYAN + "FizzBuzz" + Fore.RESET)
        elif IsFizz(i):
          print(Fore.GREEN + "Fizz" + Fore.RESET)
        elif IsBuzz(i):
          print(Fore.YELLOW + "Buzz" + Fore.RESET)
        else:
          print(i)
  except ValueError:
    clear()
    print(Fore.RED + "Anything except numbers are prohibited" + Fore.RESET)


# Application Start
if __name__ == "__main__":
  while True:
    try:
      main()
    except KeyboardInterrupt:
      clear()
      print(Fore.GREEN + "Goodbye!" + Fore.RESET)
      exit(1)
