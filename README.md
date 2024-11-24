# Assignment 7

For the exercises of lecture 7 the library pandas is required. Run the following command at the beginning of the script: import pandas as pd

# Exercises outline
1) Create a new column within the data set 'data' called professor_initials to store the initials of each professor, both first and last name.
   First, the column professor is transformed into a string and split based on the gap between the first and last name. This is stored within the variable name. Then both the first and last name in the variable name are further split based on character. The first letter of the name and surname are extracted and added together and stored in the professor_initials column.
2) Implement a join to combine data and 'courses_data' data frames.
   An inner join is used to combine the 'courses_data' and 'data' data frames based on the column professor that both data frames have.
3) Combine the df and df_courses data frames.
   First, both 'data' and 'courses_data' are transformed into a pandas data frame and then merged based on the column professor.
4) Create a new column called professor_last_name to store the extracted last name of each professor using string operations.
   The column professor is transformed into a string, then split based on the space between the first and last names. Lastly the last name is extracted and stored in a new column called professor_last_name.
