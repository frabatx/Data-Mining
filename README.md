# Data Mining Project
**Frequent itemset mining in tree-like sequences of complex objects**
**Data Mining University of Trento 2018/19 January/February Exam Period**

A great deal of applications are producing data records that are not independent to each other but sequences where the
appearance of a record depends on the appearance of another. Furthermore, each such record is not an opaque item but
consists of a number of components (or characteristics if you like). The goal of the current work is to develop an efficient
approach for computing the frequent and informative relationships among the characteristics of the records
Consider the case of a cloud system, where different machines are interconnected and together they serve different customers.
On each machine a number of different services are running. A service is basically a program that is called by someone
outside. When a service is called, it can be executed and then return the results, or it may need some extra services to call.
Consider, for instance, a request to buy a product in amazon with a specific credit card number, received by the http server.
The server has to call another service in another machine to check if the credit card is valid and when this responds then the
system calls the warehouse to place the order, and one finish return the request to the user. We would like to identify cases
like for instance the fact that when people buy TV they usually use a VISA credit card.
(Other applications one can think about:
- shopping in a super market considering the order of the items picked up from shelves
- servers in the cloud that call located in other machines,
- online shopping indicating orders in which items are bought,
- public administration with the processes, one can follow,
- sequence of responses in nested conversations in online forum discussions
- order in which pages are visited,
- etc.
So lets define the problem more formally: A record is a tuple of the form <a1:v1, a2:v2, ..., aN:vN>. The pair a:v is an attribute
name/value pair. For instance, it can be name:John, or time=10:22, or IP=123.182.123, etc. (An alternative would be not to
differentiate between attribute name and value and consider them both as one word or only one of them. This will make the
record to be instead of a tuple just a vector of terms.
A transaction is a set of records that form a tree (meaning that each record in the set has ONE only parent record. Here is an
example of a transaction:

>A
>+------- B
>          +------- C
>          +------- D
>+------- F
>          +------- G
>                    +------- H
>                              +------- I
>                    +------- J

Which means that A started, first called B, (B called C and then D), then the A called F which in turn called G. G called first H
(which called I) and then G called J.
To identify the transaction in which a record belongs we can assume that one of the attributes is called tid (meaning transaction
id). So, if two records have the same value in the attributes tid, it means that they belong to the same transactions. To
distinguish between records, we can also assume that each record has an attribute called rid (meaning record id) that is a
unique identifier for each record. Last but not least, the remaining attributes of the record can be whatever (they are application
dependent).
Problem statement: Given a set of transactions, identify patterns (sequences or tree form structures) of attributes (with or
without values) that are frequent. A frequent pattern is defined the same way the concept of frequent has been defined in the
frequent itemset problem.
Your goal is to develop a solution to the above problem (or a variation of it if you cannot find a solution to the exact problem).
Write a report in which you describe: (i) the problem, the way you have it understood it; (ii) a general description of what you
try to solve and why it is different from existing algorithms you know; (iii) the problem statement formally; (iv) the algorithmic
solution that you have developed; and (v) the set of the experiments you have performed.
For the last part, you need to perform a number of experiments that you study your algorithm, basically studying how well it
scales as the data gets larger or different. (More to be discussed in class during the presentation) Also, you better do a
comparison with what is called base line which means take one of the traditional algorithms, use it as a black box and somehow
run that algorithm on your data. Measure the different (success rate) of your algorithm compared to the base line using some
form or error measure (e.g. the RMSE that we talked in class).
IMPORTANT: Your report has to follow the specific format (Latex) that was provided to you alongside this document. You
cannot change font size or margins of this template.
Delivery: The deadline for delivering the project is Feb 15th. Note that this topic is for the Jan/Feb exam period. The other
periods will have a different topic that will be of the same level and announced at a similar time before the deadline.

For the delivery, you need to provide
1) Your report in pdf (named report.pdf)
2) Your document (in a directory called doc)
3) Your code (in a directory called code)
4) Your dataset (in a directory called dataset)
Place all the above in a google drive directory, and name it as DS_XXX_YYY where XXX and YYY are the student number
(matricola) of the members of the group. Share the folder with velgias@unitn.it
The project is intended for groups of two (2) ... Single person projects are also accepted.
Note: Discuss with the professor if you are also taking the Big Data course.
