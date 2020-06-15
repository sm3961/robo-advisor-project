# robo-advisor-project
My work for the Robo Advisor project. Completed by Soumom Manir.


A solution for the [Robo Advisor project] (https://github.com/sm3961/robo-advisor-project).

Issues requests to the [AlphaVantage Stock Market API](https://wwww.alphavantage.co/) in order to 
provide automated stock or cryptocurrency trading recommendations.

## Prerequisites

    + Anaconda 3.7
    + Python 3.7
    + Pip 

## Installation

Clone or download [this repository] (https://github.com/sm3961/robo-advisor-project) onto your computer. Then navigate there from the command line: 

```sh
cd robo-advisor-project
```
```
Create and activate a new Anaconda virtual environment:

conda create -n stocks-env python=3.7 # (first time only)
conda activate stocks-env
```

```
From within the virtual environment, install the required packages specified in the "requirements.txt" file you created:

pip install -r requirements.txt
```

## Setup

Before using or developing this application, take a moment to [obtain an Alphavantage API Key] (https://www.alphavantage.co/support/#api-key) (e.g. "abc123").

After obtaining an API key, create a new file in this repository called ".env", and update the contents of the ".env" file to specify your real API key. 

ALPHAVANTAGE_API_KEY="abc123"



## Usage

Run the project:

    python app/robo_advisor.py

