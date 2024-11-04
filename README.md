# Python

1) os.listdir was used to list all files within the annotations folder and save this list in a variable called files. From there the function len allowed us to retrieve the number of files in the annotations folder.

2) the name of each file was split and each part was assigned to a momentary variable. From there an if function tested that each part of the file's name followed the name convention of date, time, satellite number, version and unique region. All those tests were concatenated with an and such that there must have been a perfect match between the file's name and convention to count it in the variable files_following_convention.

3) two dictionaries were created to store the month/year as the key and the number of occurrences of that key as values. This allowed an easier analysis of the months and years the annotations corresponded to. Then a simple max function allowed us to extrapolate the month that occurred the most among the files.
   
4) first a new_annotations folder was created within the session_4 already existing one. And then for each month within the previously created months dictionary a folder was created within new_annotations.

5) I noticed the files when printed were already sorted, I just needed to reverse the order to have the most recent annotation first.

6) I followed the same thinking as task 3, creating an empty dictionary where the satellite number was key and the number of instances it appeared within the annotations folder as the value. To identify the most recently used satellite I extracted its number from the last instance in the files list.

7) lastly, I created an empty list called region. Then using a for loop like the ones previously used I split each file's name and extracted the unique region part. Since unique_region is a list I concatenate the items within using '_' between each instance. I then appended this new string within the region list. To then extract the unique regions I simply modified the list into a set, since sets do not allow for duplicated and then extracted the length of it to know the number of unique regions present.
