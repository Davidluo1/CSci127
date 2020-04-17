#CSci 127 Teaching Staff
#A program that uses functions to print out days.
#Modified by:  ADD YOUR NAME HERE

def dayString(dayNum):
     
     days = {1:January, 2:February, 3:March, 4:April, 5:May, 6:June, 7:July}
     
     return(days[dayNum])



def main():
     n = int(input('Enter the number of the day: '))
     dString = dayString(n)
     print('The day is', dString)


if __name__ == "__main__":
     main()
                   
