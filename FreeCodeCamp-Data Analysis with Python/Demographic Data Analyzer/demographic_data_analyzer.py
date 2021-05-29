import pandas as pd


def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    # race_count = df.groupby('race').race.count()
    race_count = df['race'].value_counts()

    # What is the average age of men?
    # average_age_men = df[df['sex'] == 'Male'].age.mean()
    average_age_men = df.groupby('sex').age.mean().get(key= 'Male')

    # What is the percentage of people who have a Bachelor's degree?
    percentage_bachelor = (df[df['education']=='Bachelors'].education.count() / df['education'].count())*100
    percentage_bachelors = round(percentage_bachelor , 1 )
    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]
    lower_education = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])]

    # percentage with salary >50K
    high_1 = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].salary == '>50K'
    high_2 = df[df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].salary
    higher_education_richs = high_1.values.sum() / high_2.count() * 100
    higher_education_rich = round(higher_education_richs, 1)
    low_1 = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].salary == '>50K'
    low_2 = df[~df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])].salary
    lower_education_richs = low_1.values.sum() / low_2.count() * 100
    lower_education_rich = round(lower_education_richs , 1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    num_min_workers = df[df['hours-per-week'] == 1]['hours-per-week'].count()
    rich_count = (df[df['hours-per-week'] == 1]['salary'] == '>50K').value_counts()
    rich_num = rich_count.values[1]
    rich_percentages = rich_num / num_min_workers * 100
    rich_percentage = round(rich_percentages , 1)

    # What country has the highest percentage of people that earn >50K?
    highest_earning_country = (df.loc[df['salary'] == '>50K', 'native-country'].value_counts()/df['native-country'].value_counts()).idxmax()
    highest_earning_country_percentages = (df.loc[df['salary'] == '>50K', 'native-country'].value_counts()/df['native-country'].value_counts()).max()*100
    highest_earning_country_percentage = round(highest_earning_country_percentages , 1)
    # Identify the most popular occupation for those who earn >50K in India.
    top_IN_occupation = df[df['native-country'] == 'India']['occupation'].value_counts().idxmax()

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
