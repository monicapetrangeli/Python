# Assignment 6

For the exercises of lecture 6 two datasets were used, Netflix and Titanic. You can find both in this Github branch.

To replicate this exercise the library pandas is required. Run the following command at the beginning of the script: import pandas as pd

# Exercises outline
Netflix
1) Identify if any missing values are present within the rating attribute of the data frame.
2) Calculate how many films in 2021 have the country attribute equal to your country. For this exercise, I used 'country'=='Italy'.
   First, the data frame was filtered based on country and release year. Then, the function len was used to count the number of observations derived from the filtering.
3) Calculate the number of films released in 2020 with no missing values in the other attributes.
   First, the observations with missing values were dropped to ensure only data with full information were present. Then the data frame was filtered based on release_year.
4) Identify which year has the highest number of movies released within it.
   A dictionary was created with the release year as the key and the values being the number of movies released within that year. The max function was then used to identify the release year with the largest number of movies.
5) Find the average number of movies released per year from 2010 onward.
   First, the data frame was filtered by release_year being equal to or bigger than 2010 and then grouped based on release_year and counted to find how many movies were released per year. Then a simple mean function was used to extrapolate the average number of movies released per year.

Titanic
1) Calculate the gender_based survival percentage
   The data frame is first grouped by gender and survival. Then to calculate both male and female survival percentage the total number of survived male/female was divided by the total number of male/female passengers present on the titanic.
2) Calculate the survival percentage grouped by gender and class
   A very similar approach to the previous question was applied here. The data frame was grouped by gender, survival and class (Pclass) and then the survival percentages by gender and class where calculated.
