import datetime
import sys

if __name__ == '__main__':
    startDate = sys.argv[1]
    endDate = sys.argv[2]
    dates = []
    dt = datetime.datetime.strptime(startDate, "%Y%m%d")
    date = startDate[:]
    while date <= endDate:
        dates.append(date)
        dt = dt + datetime.timedelta(1)
        date = dt.strftime("%Y%m%d")
    for date in dates:
        print(date)
