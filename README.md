# ACM YorkU Programming Contest 2 :droplet:

The solutions for the questiosn are for the second round of the YorkU programming contest. The questions can be found [here](https://open.kattis.com/contests/dqdbnx)

## Thoughts :eyes:

I felt like it went better this time. I managed to solve the first question in about 20 minutes (*to be fair, the computer I was using was unresponsive for 10 minutes due to server issues, so I could have finished it faster*).

The second question was odd. I implemented it in Java, only for the solution to time out so I did the question in python. However I received run-time errors which made me realize that the default data types (int, long, float) will not be able to support the large numerical calculations.
`Max size of numericla data type is 2^64, while the input can have 10000 characters, which can potentially represent 2^10000`. 

## BIG PROBLEM

Time ran out at that point before I managed to convert it to a data type that can support it (BigDecimal for Java, Decimal for Python). However, I **still** have a run time error, so I'll try to figure that out... possibly.
