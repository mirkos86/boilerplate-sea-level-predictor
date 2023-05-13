import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress


def draw_plot():
  # Read data from file
  df = pd.read_csv('epa-sea-level.csv')

  # Create scatter plot
  fig, axes = plt.subplots(figsize=(15, 5))
  axes.scatter(df['Year'], df['CSIRO Adjusted Sea Level'], color='blue')

  # Create first line of best fit
  # Linear regression from 1880
  linregression = linregress(df['Year'], df['CSIRO Adjusted Sea Level'])
  fit_line_x = pd.Series([1880 + i for i in range(0, 171)])
  fit_line_y = fit_line_x * linregression.slope + linregression.intercept
  axes.plot(fit_line_x, fit_line_y)

  # Create second line of best fit, focusing on a restricted database, starting from year 2020
  df_2000 = df[df['Year'] >= 2000]
  linregression2020 = linregress(df_2000['Year'],
                                 df_2000['CSIRO Adjusted Sea Level'])
  fit_line_2020_x = pd.Series([2000 + i for i in range(0, 51)])
  fit_line_2020_y = fit_line_2020_x * \
      linregression2020.slope + linregression2020.intercept
  axes.plot(fit_line_2020_x, fit_line_2020_y)

  # Add labels and title
  axes.set_xlabel('Year')
  axes.set_ylabel('Sea Level (inches)')
  axes.set_title('Rise in Sea Level')

  # Save plot and return data for testing (DO NOT MODIFY)
  plt.savefig('sea_level_plot.png')
  return plt.gca()
