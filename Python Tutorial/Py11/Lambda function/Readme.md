## What are the Lambda function in python ?

In Python, an anonymous function is a function that is defined without a name.

While normal functions are defined using the def keyword in Python, anonymous functions are defined using the lambda keyword.

Hence, anonymous functions are also called lambda functions.

--------------------------------------------------------------------------------------------------------------------------------------------

## How to use Laambda Function ?

Lambda functions can have any number of arguments but only one expression. The expression is evaluated and returned.
Lambda functions can be used wherever function objects are required

--------------------------------------------------------------------------------------------------------------------------------------------

## Why to use Lambda function ? 

We use lambda functions when we require a nameless function for a short period of time.

--------------------------------------------------------------------------------------------------------------------------------------------

## Built in functions of lambda function ->

- Map() ->
The map() function in Python takes in a function and a list.
The function is called with all the items in the list and a new list is returned which contains items returned by that function for each item.


- Filter() ->
The filter() function in Python takes in a function and a list as arguments.
The function is called with all the items in the list and a new list is returned which contains items for which the function evaluates to True.


### Similarities of `Filter()` & `Map()` --->

- filter() -> 
     - takes function and list as argument 
     - reeturn a new list based on the function evaluation

- map() -> 
     - takes function and list as argument 
     - reeturn a new list based on the function evaluation


```
#Syntax ---->
# newList=list(filter(lambda ---- ),listName)
# map() ->
#newList=list(map(lambda -----),listName)
```


## Differance between map() and filter() ->
```
In map: Function will be applied to all objects of iterable.
In filter: Function will be applied to only those objects of iterable who goes True on the condition specified in expression. 

```
