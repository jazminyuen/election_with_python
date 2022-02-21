# Election Audit

## Project Overview
A Colorado Board of Elections employee has asked for help to complete the election audit of a recent local congressional election. This involves analyzing the results of the election by candidate and by county.

## Resources
- Data source: election_results.csv
- Software: Python 3.9.7, Visual Studio Code, 1.64.2

## Election-Audit Results
The analysis of the election shows that:

- There were 369,711 votes cast in the election.
- The results of votes by county were:
   - Jefferson County produced 10.5% of the vote with 38,855 number of votes.
   - Denver County produced 82.8% of the vote with 306,055 number of votes.
   - Arapahoe County produced 6.7% of the vote with 24,801 number of votes.
- *Denver County had the largest number of votes.*
- The candidate results were:
  - Charles Casper Stockham received 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette received 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane received 3.1% of the vote and 11,606 number of votes.
- The **winner** of the election was:
  - **Diana DeGette** who received 72.8% of the votes and 272,892 number of votes.

## Election Audit Summary

Upon completion of this audit, I believe this script can be used for any election. I would like to describe to the election commission two examples for modifying the script to enable it to be used again.

1. The variables that represent the counties can be applied to any type of location that we receive for a particular ballot ID. This means that geographic information such as neighborhood, city, state, or region can be analyzed at this level. By duplicating the way that the 'county_options' variable is treated, we can easily modify the script to include more geographic information to see how voters from each location voted. This is helpful because it would cover any magnitude of election.
2. For this election audit, I was given very basic information: ballot ID, county, and candidate. For other elections, more data may be gathered which will allow for a wider analysis. If given more demographic information on each voter, this script can easily be modified by adding more variables. For example, I could add a variable to represent the age of the voter. I would be able to analyze the election results from multiple angles.
