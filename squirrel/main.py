import pandas
import os
def main():
    data = pandas.read_csv('4.3 2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv')
    dt=data[data["Primary Fur Color"]== "Black"]
    print(len(dt))
    print(dt["Unique Squirrel ID"])

if __name__ == '__main__':
    main()
