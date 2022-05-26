# Leetcode-Scraper-Blind-75
Leetcode problem scrapper made in Selenium using python.

Repository contains two files-
1. _leetCodeScraper.py_: Given the link to a leetcode problem, it scrapes and returns problem number, name, difficulty, description and given sample code.
2. _blind75.py_: Scrapes the links of Leetcode Blind 75 problems, processes them through _leetCodeScraper.py_ and saves the problem with naming convention 
   _pNumber_pName_difficulty_, in the given outDir in the following format-

```
#include <bits/stdc++.h>  

using namespace std;  

/*  
{Problem Description}
*/  

{Sample Code}    

int main() {
    Solution sol;
    return 0;  
};
```
