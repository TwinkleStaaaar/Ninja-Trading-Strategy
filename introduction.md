# Ninja-Trading-Strategy
Build a set of models to study and test stock trading strategy: momentum strategy

0. Why am I trying to run this project?

My major is Financial Engineering and I am a big fan of data analyst and module building. But unfortunately, I could not find a job to let me explore my idea and develop myself in the direction I want, what a pity. Even though, I still want to find a place to practice my coding skills and model building abilities. I wish one day, I can become a qualified quant.

1. Brief Introduction:

Momentum strategy should be the easiest strategy been used in the world. Its fundamental assumption is: stock price follows a constant trend. In other words, if the price has gone up for late ten days, it would be very likely to go up tomorrow.  This project will be built to spot and study this trend, train a model to use this strategy and back-testing the result.

2. Building Schedule:

(1). Plain coding model:
Input: one-dimensional data
Output: Profit for one-year investment
Coding method: plain script coding, line by line, like code in R
Mission: Explore the performance of strategy in perfect scenario (no cost, instant trading, etc.)

(2). Level-1 simulation model:
Input: all the data in the market
Output: Profit, Investment Stock, Holding period and other investment information
Coding Method: Plain script coding like Plain coding model
Mission: Calibrate key parameters like buy or sell conditions

(3). Level-2 simulation model:
Input: all the data in the market
Output: Profit, investment information
Coding Method: encapsulate model process in class and method
Mission: Build fundamental class for further detailed simulation

(4). Level-3 simulation model:
Input: really-time data
Output: Profit, Specified investment information
Coding Method: different classes for different scenario
Mission: Trying to address practical problems if put this model into commercial use.  
