### Git Commands Documentation Project
import csv
import time
import pandas as pd

CITY_DATA = {
    'chicago': 'chicago.csv',
    'new york city': 'NYC.csv',
    'washington': 'washington.csv'
}

def get_filters():
    """
    Asks the user to specify a city, month, and day to analyze.

    Returns:
        city (str) - name of the city to analyze
        month (str) - name of the month to filter by, or "all" to apply no month filter
        day (str) - name of the day of the week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # Get user input for city
    while True:
        city = input("Enter the city (Chicago, New York City, Washington): ").lower()
        if city in CITY_DATA:
            break
        else:
            print("Invalid city. Please try again.")

    # Get user input for month
    while True:
        month = input("Enter the month (January, February, ... , June), or 'all' for all months: ").lower()
        if month in ['all', 'january', 'february', 'march', 'april', 'may', 'june']:
            break
        else:
            print("Invalid month. Please try again.")

    # Get user input for day of the week
    while True:
        day = input("Enter the day of the week (Monday, Tuesday, ... Sunday), or 'all' for all days: ").lower()
        if day in ['all', 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']:
            break
        else:
            print("Invalid day. Please try again.")

    print('-' * 40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        city (str) - name of the city to analyze
        month (str) - name of the month to filter by, or "all" to apply no month filter
        day (str) - name of the day of the week to filter by, or "all" to apply no day filter

    Returns:
        df (pd.DataFrame) - Pandas DataFrame containing city data filtered by month and day
    """
    filename = CITY_DATA[city]
    df = pd.read_csv(filename)

    if 'Start Time' not in df.columns:
        raise KeyError("Missing 'Start Time' column in the dataset.")

    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # Filter by month if applicable
    if month != 'all':
        month_num = ['january', 'february', 'march', 'april', 'may', 'june'].index(month) + 1
        df = df[df['Start Time'].dt.month == month_num]

    # Filter by day of the week if applicable
    if day != 'all':
        df = df[df['Start Time'].dt.day_name().str.lower() == day]

    return df


def time_stats(df):
    """
    Displays statistics on the most frequent times of travel.
    """
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = int(time.time())

    # Perform time-related calculations
    common_month = df['Start Time'].dt.month.mode()[0]
    common_day = df['Start Time'].dt.dayofweek.mode()[0]
    common_hour = df['Start Time'].dt.hour.mode()[0]

    print("Most Common Month:", common_month)
    print("Most Common Day of the Week:", common_day)
    print("Most Common Hour of the Day:", common_hour)

    print("\nThis took %.2f seconds." % int((time.time()) - start_time))
    print('-' * 40)


city, month, day = get_filters()

try:
    df = load_data(city, month, day)

    # Call the function to calculate and display user statistics
    #user_stats(df)

    # Call the function to calculate and display time statistics
    time_stats(df)

except Exception as e:
    print(f"An error occurred: {e}")

def get_popular_stations(df):
    """
    Calculates the most popular start and end stations.

    Args:
   python
        df (pd.DataFrame): Pandas DataFrame containing bikeshare data

    Returns:
        (str, str): Tuple containing the most popular start and end stations
    """
    start_station = df['Start Station'].mode().values[0]
    end_station = df['End Station'].mode().values[0]
    return start_station, end_station


#city, month, day = get_filters()

try:
    df = load_data(city, month, day)

    # Call the function and store the result
    start_station, end_station = get_popular_stations(df)

    # Print the results
    print('Most Popular Start Station:', start_station)
    print('Most Popular End Station:', end_station)
except Exception as e:
    print(f"An error occurred: {e}")
def trip_duration_stats(df):
    """
    Displays statistics on the total and average trip duration.
    """
    print('\nCalculating Trip Duration...\n')
    start_time = int(time.time())

    # Perform trip duration calculations
    total_duration = df['Trip Duration'].sum()
    average_duration = df['Trip Duration'].mean()

    print("Total Duration: {:.2f} seconds".format(total_duration))
    print("Average Duration: {:.2f} seconds".format(average_duration))
    print("\nThis took {:.2f} seconds.".format(int(time.time() - start_time)))
    print('-' * 40)


def main():
    #city, month, day = get_filters()

    try:
        df = load_data(city, month, day)

        if not df.empty:
            start_station, end_station = get_popular_stations(df)
            print('Most Popular Start Station:', start_station)
            print('Most Popular End Station:', end_station)

            trip_duration_stats(df)
        else:
            print("No data available for the specified filters.")

    except KeyError as e:
        print(f"An error occurred: {e}")

    except FileNotFoundError:
        print("Error: Data file not found.")


if __name__ == "__main__":
    main()

try:
    df = load_data(city, month, day)

    # Calculate user statistics
    user_types = df['User Type'].value_counts()

    if 'Gender' in df.columns:
        gender_counts = df['Gender'].value_counts()
    else:
        gender_counts = "Gender information not available."

    if 'Birth Year' in df.columns:
        # Calculate the earliest, most recent, and most common birth years
        earliest_birth_year = int(df['Birth Year'].min())
        most_recent_birth_year = int(df['Birth Year'].max())
        most_common_birth_year = int(df['Birth Year'].mode()[0])
    else:
        earliest_birth_year = "Birth Year information not available."
        most_recent_birth_year = "Birth Year information not available."
        most_common_birth_year = "Birth Year information not available."

    # Print user statistics
    print("User Type Statistics:")
    print(user_types)

    print("\nGender Statistics:")
    print(gender_counts)

    print("\nBirth Year Statistics:")
    print("Earliest Birth Year:", earliest_birth_year)
    print("Most Recent Birth Year:", most_recent_birth_year)
    print("Most Common Birth Year:", most_common_birth_year)

    print('-' * 40)
except Exception as e:
    print(f"An error occurred: {e}")
