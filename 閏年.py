def isleap(year):
    return year%400 ==0 or(year%100!=0 and year%4==0)

def main():
    year=int(input())
    if isleap(year):
        print('it is leap year')
    else:
        print('it is common year')
if __name__ == '__main__':
    main()
