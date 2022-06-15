import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = input ('Would you like to see data for Chicago, New York, Washington?')

    while (city !='chicago') and (city !='new york city') and  (city !='washington') :
        print(' Please enter one of these cities : Chicago, New York, Washington ')
        city = input ('Would you like to see data for Chicago, New York, Washington?')


    # TO DO: get user input for month (all, january, february, ... , june)
    date_data = input (' Would you like to filter the data per month, day, both or none ?')

    month = 'none'
    day = 'none'
    if date_data == ('month' ):
        month = input (' Which month ? January, February,..., June or all')

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    elif date_data == ('day' ):
        day = input(' Which day ? Monday, Tuesday, ... Sunday or all ')

    elif date_data == ('both' ):
        month = input (' Which month ? January, February,..., June or all')
        day = input(' Which day ? Monday, Tuesday, ... Sunday or all')


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    df = pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    if (month != 'all') and (month != 'none'):
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if (day != 'all') and (month != 'none'):
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    popular_month = df['month'].mode()[0]

    print('Most Popular month:', popular_month)

    # TO DO: display the most common day of week

    popular_day_of_week = df['day_of_week'].mode()[0]

    print('Most Popular day of week:', popular_day_of_week)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('Most Popular Start Hour:', popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    most_commonly_start_station=df['Start Station'].mode()


    # TO DO: display most commonly used end station
    most_commonly_end_station=df['End Station'].mode()



    # TO DO: display most frequent combination of start station and end station trip
    df['combined'] = df['Start Station']+df['End Station']
    most_frequent_combination = df['combined'].mode()
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    #TO DO: display total travel time
    total_travel_time=df['Trip Duration'].sum()


    # TO DO: display mean travel time
    mean_travel_time=df['Trip Duration'].mean()

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts()


    # TO DO: Display counts of gender
    gender_types = df['Gender'].value_counts()


    # TO DO: Display earliest, most recent, and most common year of birth
    popular_year = df['Birth Year'].mode()
    print('Most common year:', popular_year)
    earliest_year = df['Birth Year'].min()
    print('earliest year:', earliest_year)
    most_recent_year = df['Birth Year'].max()
    print('Most recent year:', most_recent_year)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
