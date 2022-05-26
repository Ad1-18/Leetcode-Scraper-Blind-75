import unicodedata
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.support import expected_conditions as EC

#---------------------------------------------------------------
#--------------------------Globals------------------------------
s = Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

#---------------------------------------------------------------
#--------------------Problem Attributes-------------------------
codePath = "//div[@class='CodeMirror-code']/div/pre/*[text()]"
titlePath = "//div[@data-cy='question-title']"
contentPath = "//div[@data-cy='description-content']/div[1]/div[@class='content__u3I1 question-content__JfgR']/*[text()]"
diffPath = "//div[@data-key='description-content']/div/div/div[2]/div"

#---------------------------------------------------------------
# Given a Web Element, an attribute and optional arguments of
# strip and normalizaton, returns processed attribute from
# the Web Element.
def getAttr(WebEl, attr, strip="", normalize=False):
	res = WebEl.get_attribute(attr).strip(strip)
	if(normalize):
		return unicodedata.normalize('NFKD', res)
	return res

#---------------------------------------------------------------
# Given an array of web elmeents, an attribute and optional
# arguments, returns array of processed attributes
def getAttrArr(WebElArr, attr, strip="", normalize=False):
	tmp = []
	for i in WebElArr:
		tmp.append(getAttr(i, attr, strip, normalize))
	return tmp

#---------------------------------------------------------------
# Given a link to a Leetcode problem, returns-
# 1. Problem Number
# 2. Problem Name
# 3. Problem Difficulty
# 4. Sample Problem Code given
# 5. Problem Statement
def getProblem(t):
	try:
		driver.get(t)
	except WebDriverException:
		print("Window Closed")
		return(-1,-1,-1)
	retries = 10
	while(retries):
		try:
			element = WebDriverWait(driver, 20).until(
		            EC.invisibility_of_element_located((By.ID, "initial-loading")))
			break
		except:
			pass
		retries-=1
	try:
		diff = driver.find_element(By.XPATH, diffPath)
		diff = getAttr(diff, "diff")

		pName = driver.find_element(By.XPATH, titlePath)
		pName = getAttr(pName, "innerText", "").replace(".","").replace(" ", "_") + "_" + diff.title()

		content = driver.find_elements(By.XPATH, contentPath)
		content = getAttrArr(content, "innerText", normalize=True)
		content = "\n".join(content).replace("\n\n", "\n")

		code = driver.find_elements(By.XPATH, codePath)
		code = getAttrArr(code, "innerText", normalize= True)
		code = "\n".join(code)

		return(pName, content, code)
	except:
		print("Error in " + t)
		return (None,None,None)

#---------------------------------------------------------------