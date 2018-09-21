# FastFood

[![Build Status](https://travis-ci.org/EvelyneNamwoyo/FastFood.svg?branch=api-develop)](https://travis-ci.org/EvelyneNamwoyo/FastFood) [![Coverage Status](https://coveralls.io/repos/github/EvelyneNamwoyo/FastFood/badge.svg?branch=api-develop)](https://coveralls.io/github/EvelyneNamwoyo/FastFood?branch=api-develop)

FastFoods is an API for a certain food delivery app

## Getting Started

The following instructions will get you a copy of the project up and running on your local machine for development and testing purposes. These are specific to windows machines.

### Prerequisites

The following are things you need to have on your machine
* Python 3.4 and above
* Postman
* Browser(preferably chrome)
* IDE(sublime/visual studio code)
* GIT

### Installing
This is a step by step process of how to get a development environment running.
1. Open your terminal and change to a directory where you want the project to live.
2. Clone the project using git clone **https://github.com/EvelyneNamwoyo/FastFood/tree/api-develop**
3. Create virtual environment.
4. Install all project dependencies using pip install -r requirements.txt
5. Test the output using postman with the following endpoints

| Verb | Endpoint               | Functionality |Public Access |
|------|------------------------|---------------|--------------|
|GET   |/FastFood/api/v1/orders | Get all orders|  True        |  
|GET   |/FastFood/api/v1/orders/<order_id>|Fetch an order|True |
|POST  |/FastFood/api/v1/orders| Create a new order|  True     |  
|PUT   |/FastFood/api/v1/orders/<order_id>|Update order status| FALSE |
|DELETE   |/FastFood/api/v1/orders | Delete an order|  FALSE      |  

## Running tests
To run the unnittests test, run this command in your console.
pytest

