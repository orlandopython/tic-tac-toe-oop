# tic-tac-toe-oop
Object-Oriented TicTacToe Tutorial

- [YouTube](https://youtu.be/Kr5NqmxgjzM)
- [Meetup](https://www.meetup.com/OrlandoPython/events/nwxzbsyccdbfc/)

## Introduction

This is an very simple tutorial by <Fred.sells@sunrise.com> that focuses on the structure of code and pattern recognition more than the syntax of Python. This beginning tutorial on Python goes from a simple, inline coding example to the more structured Model-View-Controller (MVC) design pattern, where:

- Model is the data
- View is what you see, either as text out or as screen graphics
- Controller is the logic that gets the input and changes the model which the view then redisplays

However, clean code will not adhere to this design pattern absolutely, there is reason to blur the lines to support the concepts of:

- Data hiding – not showing data outside an object if it is not needed
- [Cohesion][1] – the basic concept of one function does one task
- Coupling – the idea that every "connection" between things is likely to increase the probability of failure and should be reduced and cleaning utilized

I have a personal bias against code commenting. I’ve found that as code evolves over the years and is maintained by different programmers and possibly even different companies, the comments tend to become less and less relevant and more and more misleading. I choose to focus on descriptive function and variable names and use comments only when it’s not obvious.

Furthermore, I like to be able to see an entire module/class/function on the monitor without scrolling. Thus "clutter" the code I’m trying to review. Of course, if I’m fixing someone else’s code it had better be commented or I’ll charge more 😊

To repeat, this is my personal bias based on the organizations where I’ve worked. I’m not necessarily right.

Finally, I spent most of my professional career with Python 2.7 and earlier (back to 0.92), so the coding styles that others can teach are more appropriate to the use of Python 3.8+

## Prerequisites

- Python 3.6+

There are no third-party requirements to install

## Running

Each file can be run directly like:

```bash
python3 code/ttt1_lists.py
```

[1]: https://sanaulla.info/2008/06/26/cohesion-and-coupling-two-oo-design-principles/