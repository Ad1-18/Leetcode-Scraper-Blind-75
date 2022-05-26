# Leetcode-Scraper-Blind-75
Leetcode problem scrapper made in Selenium using python.


Repository contains two files-

1. leetCodeScraper.py: Given the link to a leetcode problem, it scrapes and returns problem number, name, difficulty, description and given sample code.
2. blind75.py: Scrapes the links of Leetcode Blind 75 problems, processes them through leetCodeScraper.py and saves the problem with naming convention 
   pNumber_pName_Difficulty, in the given outDir in the following format-

"#include <bits/stdc++.h>

using namespace std;
/*
{Problem Description}
*/

{Sample Code}

int main(){
  Solution sol;
  return 0;
};"
