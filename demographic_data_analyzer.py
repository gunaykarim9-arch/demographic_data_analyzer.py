import pandas as pd

def calculate_demographic_data(print_data: bool = True):
    # Read data
    df = pd.read_csv('adult.data.csv', skipinitialspace=True)

    # 1. How many of each race are represented?
    race_count = df['race'].value_counts()

    # 2. Average age of men
    average_age_men = round(df.loc[df['sex'] == 'Male', 'age'].mean(), 1)

    # 3. Percentage with Bachelor's degrees
    percentage_bachelors = round((df['education'] == 'Bachelors').mean() * 100, 1)

    # 4 & 5. Advanced education vs not, percentage earning >50K
    advanced = df['education'].isin(['Bachelors', 'Masters', 'Doctorate'])
    higher_education = df[advanced]
    lower_education = df[~advanced]

    higher_education_rich = round((higher_education['salary'] == '>50K').mean() * 100, 1)
    lower_education_rich = round((lower_education['salary'] == '>50K').mean() * 100, 1)

    # 6. Minimum work hours per week
    min_work_hours = int(df['hours-per-week'].min())

    # 7. Percentage of rich among those who work min hours
    min_workers = df[df['hours-per-week'] == min_work_hours]
    rich_percentage = round((min_workers['salary'] == '>50K').mean() * 100, 1)

    # 8. Country with highest percentage of >50K earners
    country_rich_pct = (
        df.groupby('native-country')['salary']
        .apply(lambda s: (s == '>50K').mean() * 100)
        .sort_values(ascending=False)
    )
    highest_earning_country = country_rich_pct.index[0]
    highest_earning_country_percentage = round(country_rich_pct.iloc[0], 1)

    # 9. Most popular occupation for those who earn >50K in India
    india_rich = df[(df['native-country'] == 'India') & (df['salary'] == '>50K')]
    top_IN_occupation = india_rich['occupation'].value_counts().idxmax()

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
        'highest_earning_country_percentage': highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation,
    }

if __name__ == '__main__':
    # Simple local run
    calculate_demographic_data(print_data=True)
