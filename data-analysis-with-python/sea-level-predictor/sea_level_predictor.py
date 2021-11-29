import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')


    # Adjust datasets
    df_sea_level = df[['Year', 'CSIRO Adjusted Sea Level']]
    df_sea_level
    df_sea_level.columns = ['x', 'y']

    df_sea_level_prediction = pd.DataFrame(
        pd.concat([
            df_sea_level['x'],
            pd.Series(range(2014, 2050 + 1), name='x')
        ])
    )


    # Predictions
    def predict_y(x:pd.Series, res):
        return (res.intercept + res.slope*x).rename('y')


    res1 = linregress(df_sea_level)
    df_sea_level_prediction['y1'] = predict_y(df_sea_level_prediction['x'], res1)

    res2 = linregress(df_sea_level[df_sea_level['x'] >= 2000])
    df_sea_level_prediction['y2'] = predict_y(df_sea_level_prediction['x'], res2)


    # Plot
    fig = plt.figure(figsize=(10, 5))

    plt.scatter(df_sea_level['x'], df_sea_level['y'], color='b', alpha=0.2)

    plt.plot(
        df_sea_level_prediction['x'],
        df_sea_level_prediction['y1'],
        'r',
        label='Best Fit 1'
    )
    plt.plot(
        df_sea_level_prediction[df_sea_level_prediction['x'] >= 2000]['x'],
        df_sea_level_prediction[df_sea_level_prediction['x'] >= 2000]['y2'],
        'b',
        label='Best Fit 2'
    )

    plt.xlabel('Year')
    plt.ylabel("Sea Level (inches)")
    plt.title('Rise in Sea Level')

    plt.xlim(right=2060)
    plt.ylim(bottom=-1)
    plt.legend(loc='lower right')

    
    # Save plot and return data for testing (DO NOT MODIFY)
    plt.savefig('sea_level_plot.png')
    return plt.gca()