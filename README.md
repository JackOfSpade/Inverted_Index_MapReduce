# Inverted Index MapReduce

This is a simple MapReduce that creates an inverted index which maps categories to businesses. In other words, given a collection of businesses (as provided by
Yelp), an inverted index is a dictionary where each category is associated with a list of the business ids that belong to that category. 

![](https://i.imgur.com/RLzhgdr.png)

Why is this important?
This allows us to easily find, for example, all 

Your task is to design and implement MapReduce algorithms that given a collection of Yelp businesses:
• compute the inverted index of the categories to businesses (iimaper.py, iireducer.py)
and output the results in a file called inverted-index.txt
The collection of businesses is provided in a file yelp_business.csv that follows the same format
as the original data set provided by Kaggle. The contents of the file might vary when testing your code.
