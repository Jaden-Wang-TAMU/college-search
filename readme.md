# College CSV Search 

Now that you've implemented methods to search a CSV file, it's time for you to create a program to do something useful with the data. Your task is going to be to create a program that will allow users to search the `university-data.csv` file for information about colleges and universities that they are interested in. 

You are given example screens below, but feel free to tweak the display if you have a better idea. 

### Search

Your program must allow the user to search for a college or university by name. 

```
University Search

Enter the name of the university you're interested in:
```

If the search only has one result, show that result. If the search returns multiple results, you'll need to display each of the found schools and prompt the user to select one. Something like this.

```
Multiple results found for "Texas".
[1] Texas A&M University
[2] Texas Tech University
[3] University of Texas

Select [1-3]
```

Multiple results should be sorted alphabetically. 

Feel free to tweak the output a bit. You might also consider a message if there are too many returned and have the user modify their search. You don't want to list 10,000 results if someone searched for `e`. More than 20 results is probably a good place to kick the search back to the user to modify. 

### Data to Display

Your search results must display at least 10 pieces of data on the college or university displayed. 

It must include
* Address
* Website
* In state and out of state tuition

The other 7 are up to you. Select information that you would want to see when trying to decide on a school. And, of course, you can pick more than 7 more if you want. 10, the 3 above and 7 of your own, is the minimum. 

```
University of Texas
Address: 		123 Main Street
				Austin, TX 78701
Website: 		www.utexas.edu
Tuition (in):	$12,000
Tuition (out):  $18,000
... plus whatever other data you include ... 
```



### Notes

It's okay if the searches are slow. You're probably writing a linear search through a relatively large data file. That's not the fastest way to find data, and we'll talk about ways we can speed this process up later by using better data formats. 

Loading the entire file into memory when the program starts would speed up searches. It's not a great idea for really large data sets, but this one is small enough where it's probably okay. 

The data file is a few years old, so it's likely that some information is out of date. 