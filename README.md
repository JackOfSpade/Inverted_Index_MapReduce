# Yelp_Businesses_Map_Reduce

This is simple Map
In this assignment, you will be designing and implementing MapReduce algorithms for performing distributed analytics on textual data. The dataset is a subset of Yelp1's was originally put together for the Yelp Dataset Challenge and contains seven CSV files including information about businesses across 11 metropolitan areas in four countries and can be accessed here (registration to Kaggle is required):
Yelp dataset: https://www.kaggle.com/yelp-dataset/yelp-dataset/version/6
Yelp dataset (local copy): https://www.eecs.yorku.ca/course_archive/2020-21/S/4415/yelp-data.zip
The first set of the MapReduce algorithms compute n-grams of business tips; the second set computes popularity of a business; the third set computes an inverted index of the business categories. These are important statistics and tools commonly used in computational linguistic and information retrieval tasks.

In information retrieval, an inverted index is an index data structure that stores a mapping from words
to a collection of documents that they appear in. Your task is to build an inverted index that maps
categories (of businesses) to businesses. In other words, given a collection of businesses (as provided by
Yelp), an inverted index is a dictionary where each category is associated with a list of the business ids
that belong to that category. See the example below:

![](https://i.imgur.com/RLzhgdr.png)

Your task is to design and implement MapReduce algorithms that given a collection of Yelp businesses:
• compute the inverted index of the categories to businesses (iimaper.py, iireducer.py)
and output the results in a file called inverted-index.txt
The collection of businesses is provided in a file yelp_business.csv that follows the same format
as the original data set provided by Kaggle. The contents of the file might vary when testing your code.
