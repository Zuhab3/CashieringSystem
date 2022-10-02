class cashieringsystem:

    def __init__(self, a=0, r=0,recieve=0,change=0,temp=0):

        print("\n~~~~~WELCOME TO Zuhab's Chickenry~~~~~\n")

        self.a = a
        self.r = r
        self.recieve = recieve
        self.change = change
        self.temp = temp

    def foods(self):
        print("~~~~~MENU~~~~~\n")
        print("1.Spicy Chicken Burger Meal -----> 5.00", "\n2.Spicy Chicken Wrap Meal -----> 4.50", "\n3.Chicken Shawarma Meal ----> 4.00", "\n4.Spicy Chicken Wings Meal ----> 3.50","\n5.Checkout", "\n6.Exit Till\n")
        while (1):
            try:
                c = int(input("Pick Option (1-6):\n"))

                if (c == 1):
                    d = int(input("Enter the quantity:\n"))
                    self.r = self.r + 5 * d
                elif (c == 2):
                    d = int(input("Enter the quantity:\n"))
                    self.r = self.r + 4.5 * d
                elif (c == 3):
                    d = int(input("Enter the quantity:\n"))
                    self.r = self.r + 4 * d
                elif (c == 4):
                    d = int(input("Enter the quantity:\n"))
                    self.r = self.r + 3.5 * d
                elif (c == 5):
                    print("Order Total: £", self.r)
                    if (self.r > 0):
                        recieve = int(input("Input Cash Recieved:\n £ "))
                        print("Change to return to customer: £", recieve - self.r)
                        print("Thank You Come Again!!!")
                        quit()
                elif (c == 6):
                    quit()
                else:
                    print("Invalid Option Entered\nEnter a number between 1-6")
                    break
            except ValueError:
                print("Invalid Data Type\nEnter a NUMBER between 1-6")





def main():
    a = cashieringsystem()

    while (1):

            a.foods()





main()

