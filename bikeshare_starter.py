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
   
    while True:
        city = input('Would you like to see data for Chicago, New York City, or Washington? ').strip().lower()
        print("A beautiful city and a good choice👌")
        if city in ['chicago', 'new york city', 'washington']:
            break
        else:
            print('Incorrect entry! Please try again.')
    while True:
        Filter_Date = input('Would you like to filter the data by month, day,both or not at all(none)?').strip().lower()
        if Filter_Date in ['month', 'day', 'both', 'none']:
            break
        else:
            print('Incorrect entry! Please try again.')
    # TO DO: get user input for month (january, february, ... , june)
    month = 'all'
    if Filter_Date in ['month', 'both'] : 
        while True:
            month = input('Which month - January, February, March, April, May, or June? ').strip().lower()
            if month in ['january', 'february', 'march', 'april', 'may', 'june']:
                break
            else:
                print('Incorrect entry! Please try again.')
    # TO DO: get user input for day of week (monday, tuesday, ... sunday)
    day = 'all'
    if Filter_Date in ['day', 'both'] : 
        while True:
            day = input('Which day - Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, or Sunday? ').strip().lower()
            if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
                break
            else:
                print('Incorrect entry! Please try again.')
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
    
    if month != 'all' :
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
        df = df[df['month'] == month]
    if day != 'all' :
        df = df[df['day_of_week'] == day.title()]
    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = df['month'].mode()[0]
    popular_month = months[popular_month - 1]
    print('the most common start month: ',popular_month)    

    # TO DO: display the most common day of week
    popular_day = df['day_of_week'].mode()[0]
    print('the most common start day:\n ',popular_day)

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    print('the most common start hour:\n ',popular_hour)


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    PopularStartStation = df['Start Station'].mode()[0]
    print('the most commonly used start station:\n ',PopularStartStation)

    # TO DO: display most commonly used end station
    PopularEndStation = df['End Station'].mode()[0]
    print('the most commonly used End station:\n ',PopularEndStation)

    # TO DO: display most frequent combination of start station and end station trip
    TripStation = pd.Series(list(zip(df['Start Station'],df['End Station'])))
    PopularTripStation = TripStation.mode()[0]
    print('the most frequent combination of start station and end station trip: ',PopularTripStation)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print("The total travel time:\n ",df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print("The mean travel time: \n",df['Trip Duration'].mean())

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print("The counts of user types:\n ",df['User Type'].value_counts())

    # TO DO: Display counts of gender
    if 'Gender' in df.columns : 
        print("The counts of gender: \n",df['Gender'].value_counts())
    # TO DO: Display earliest, most recent, and most common year of birth
    if 'Birth Year' in df.columns :  
        print("The earliest of Birth Year:\n ",int(df['Birth Year'].min()))
        print("The most recent of Birth Year:\n ",int(df['Birth Year'].max()))
        print("The most common year of Birth Year:\n ",int(df['Birth Year'].mode()[0]))

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
        row_start = 0
        while True:
            show_data = input('\nWould you like to see 5 lines of raw data? Enter yes or no.\n').strip().lower()
            if show_data == 'yes':
                print(df.iloc[row_start:row_start + 5])
                row_start += 5
                if row_start >= len(df):
                    print("No more data to display.")
                    break
            elif show_data == 'no':
                break
            else:
                print("Please enter yes or no.")
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break
    print("I'll see you later🖐️🎉") 


if __name__ == "__main__":
    print("Hello, hello, hello, have a nice day🌄")
    main()

# I hope you liked this project and that it was beneficial to you.
