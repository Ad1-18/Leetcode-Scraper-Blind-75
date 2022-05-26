from os import path
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC
from leetCodeScraper import getProblem, getAttrArr, getAttr, driver

#---------------------------------------------------------------
#--------------------------Globals------------------------------
targetLink = "https://leetcode.com/discuss/general-discussion/460599/blind-75-leetcode-questions"
linkPath = "//div[@class='discuss-markdown-container']/ul/li/a"
outDir = "C:/prog/cpp/LeetCode/"

#---------------------------------------------------------------
# Given the link to the Blind 75 leetcode page,
# Returns an array of https links of LeetCode Blind 75 questions
def getLinks(t):
	try:
		driver.get(t)
	except WebDriverException:
		print("Window Closed")
		return([])
	retries = 10
	while(retries):
		try:
			element = WebDriverWait(driver, 20).until(
		            EC.visibility_of_element_located((By.CLASS_NAME, "discuss-markdown-container")))
			break
		except:
			pass
		retries-=1
	raw  = driver.find_elements(By.XPATH, linkPath)
	names = getAttrArr(raw, "innerText", "\t\r\n")
	raw = [raw[names.index(name)] for name in names if "Leetcode Premium" not in name]
	links = getAttrArr(raw,"href", " \t\r\n")
	return links

#---------------------------------------------------------------
# Given, problem name, description and sample code,
# creates a .cpp file with sample code and description embedded,
# in given directory.
def writeQues(name,content,code):
	name+=".cpp"
	writeStr = (f"#include<bits/stdc++.h>\n\n"
			f"using namespace std;\n"
			f"/*\n"
			f"{content}\n"
			f"*/\n"
			f"{code}\n\n"
			f"int main(){{ \n"
			f"\tSolution sol;\n"
			f"\treturn 0;\n"
			f"}};"
		)
	if(not(path.isfile(outDir+name)) ):
		f = open(outDir + name, "x", encoding = 'UTF-8' )
		f.write(writeStr)
		f.close()
	else:
		print(f"{name} already exists in {outDir}")

#---------------------------------------------------------------
# Helper Function
def main():
	links = getLinks(targetLink)
	for i in links:
		name,content,code = getProblem(i)
		if(name == -1):
			break
		if(name and content and code):
			writeQues(name,content,code)
	driver.quit()
#---------------------------------------------------------------
main()

