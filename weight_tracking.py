import csv
import matplotlib.pyplot as plt
import datetime as dt
import matplotlib.dates as mdates
import pandas as pd

with open('weight_history.csv', encoding='utf-8-sig') as csvfile:
    reader = csv.DictReader(csvfile)

    weight_kg = []
    date = []
    for row in reader:
        weight_kg.append(float(row['Weight(kg)']))
        date.append(dt.datetime.strptime(row['Time of Measurement'], '%Y-%m-%d %H:%M:%S').date())

window_size = 7
weight_moving_average = pd.Series(weight_kg)
windows = weight_moving_average.rolling(window_size)
weight_moving_average = windows.mean().tolist()


plt.plot(date, weight_kg, '.')
plt.plot(date, weight_moving_average, '-')
plt.hlines(y=63.5, xmin=dt.date(2023, 3, 1), xmax=max(date), color='r', linestyle='-', alpha=0.2, linewidth=58)
plt.axvline(x=dt.date(2023, 3, 1), color='g', linestyle='--')

plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%d-%m'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=1))
plt.xticks(rotation=70)
plt.xlim(dt.date(2023, 2, 1))
plt.ylim(62.5, 65)
plt.xlabel('Date')
plt.ylabel('Weight (kg)')
plt.grid()
plt.show()


