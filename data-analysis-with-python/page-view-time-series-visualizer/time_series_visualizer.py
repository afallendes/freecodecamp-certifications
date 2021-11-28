import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv('fcc-forum-pageviews.csv', index_col='date')
df.index = pd.to_datetime(df.index)

# Clean data
df = df[
    (df['value'] >= df['value'].quantile(0.025)) &
    (df['value'] <= df['value'].quantile(0.975))
]

# Helper
months = [
    'January',
    'February',
    'March',
    'April',
    'May',
    'June',
    'July',
    'August',
    'September',
    'October',
    'November',
    'December'
]

def draw_line_plot():
    # Draw line plot
    fig = plt.figure(figsize=(25,5))
    plt.plot(df, color='red')

    xtick_location = df.index.tolist()[::210]
    xtick_labels = [x.strftime('%Y-%m') for x in xtick_location]
    plt.xticks(ticks=xtick_location, labels=xtick_labels)

    plt.title('Daily freeCodeCamp Forum Page Views 5/2016-12/2019')
    plt.xlabel('Date')
    plt.ylabel('Page Views')


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar = df.groupby(by=[df.index.year, df.index.month]).mean()
    df_bar.index.rename(['year', 'month'], inplace=True)
    df_bar = df_bar.unstack(['month'], fill_value=0).value

    # Draw bar plot
    ax = df_bar.plot(kind="bar", figsize=(8,8))
    ax.set_xlabel('Years')
    ax.set_ylabel('Average Page Views')

    plt.legend(labels=months, loc='upper left')


    fig = ax.figure

    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    df_box['monthN'] = [d.month for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, axes = plt.subplots(1, 2)

    fig.set_size_inches([16,8])

    ax1 = sns.boxplot(x='year', y='value', data=df_box, ax=axes[0])
    ax1.set(xlabel ="Year", ylabel = "Page Views", title ='Year-wise Box Plot (Trend)')

    ax2 = sns.boxplot(x='month', y='value', data=df_box, ax=axes[1], order=[_[:3] for _ in months])
    ax2.set(xlabel ="Month", ylabel = "Page Views", title ='Month-wise Box Plot (Seasonality)')

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
