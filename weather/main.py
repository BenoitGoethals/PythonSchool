import pandas
import os
def main():
    cwd = os.getcwd()
    print("Hello World!")
    print(cwd)
    data = pandas.read_csv('weather_data.csv')
    print(data["day"])
if __name__ == '__main__':
    main()
