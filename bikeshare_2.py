import time
import pandas as pd
import numpy as np
# python bikeshare_2.py
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
    # get user input for city (chicago, new york city, washington).
    while True:
        city = input('Would you like to see data for chicago, new york city, or washington? ').lower()
        if city in CITY_DATA:
            break
        else:
            print('Please renter a valid city name.')
    # while city == 'Chicago' || city == 'New York' || city == 'Washigton':# get user input for month (all, january, february, ... , june)
    while True:
        month = input('Do you want details specific to a particular month? if yes, type month name within first six months esle type \'all\': ').lower()
        if month in ('january', 'february', 'march', 'april', 'may', 'june', 'all'):
            break
        else:
            print('Please renter a valid month name.')
    # get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input('Do you want details specific to a particular day? if yes type day name else type \'all\': ').lower()
        if day in ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all'):
            break
        else:
            print('Please renter a valid day name.')

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
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        m = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == m]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    com_month = df['month'].mode()[0]
    print("Most common month: ", com_month)

    # display the most common day of week
    com_day = df['day_of_week'].mode()[0]
    print("Most common day of week: ", com_day)

    # display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    com_hour = df['hour'].mode()[0]
    print("Most common hour: ", com_hour)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    start_station = df['Start Station'].mode()[0]
    print("Most common start station: ", start_station)

    # display most commonly used end station
    end_station = df['End Station'].mode()[0]
    print("Most common end station: ", start_station)

    # display most frequent combination of start station and end station trip
    combine_stations = (df['Start Station'] + ' AND ' + df['End Station']).mode()[0]
    print("Most frequent start and end station trip: ", combine_stations)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time
    total_time = df['Trip Duration'].sum()
    print("Total Travel Time = ", total_time)

    # display mean travel time
    mean_time = df['Trip Duration'].mean()
    print("Mean Travel Time = ", mean_time)
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    user_types = df['User Type'].value_counts()
    print("Counts of user types:\n", user_types)

    # Display counts of gender
    if city in ('chicago', 'new york city'):
        gender = df['Gender'].value_counts()
        print("Counts of gender:\n", gender)

    # Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df:
        earliest = df['Birth Year'].min()
        print("Earliest year of birth = ", earliest)
        recent = df['Birth Year'].max()
        print("Most recent year of birth = ", recent)
        com_year = df['Birth Year'].mode()[0]
        print("Most common year of birth =  ", com_year)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def display_data(df):
    i = 0
    # get users input by yes or no, if they want to see five row data or not.
    while True:
        choice = input('Would you like to see five more row data? yes or no. ').lower()
        if choice == 'yes':
            print(df[i:i+5])
            i = i + 5
        elif choice == 'no':
            break
        else:
            print('PLease renter yes or no.')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(df)
        # get users input by yes or no, if they want to restar.
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
