from selenium import webdriver

# webdriver location
driver = webdriver.Chrome("C:\\Users\\clair\\Desktop\\python projects\\chromedriver.exe")

# initialize URL
url = "https://www.amherst.edu/go/student-health-survey"
driver.get(url)

# fill out the form
radiobuttons = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupElContainer")
radiobuttons[0].click()

nextButton = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel")
nextButton.click()

radiobuttons = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupElContainer")
radiobuttons[1].click()

nextButton = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel")
nextButton.click()

radiobuttons = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupElContainer")
radiobuttons[1].click()

nextButton = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel")
nextButton.click()

radiobuttons = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupElContainer")
radiobuttons[1].click()

nextButton = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel")
nextButton.click()

radiobuttons = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupElContainer")
radiobuttons[1].click()

nextButton = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel.quantumWizButtonPaperbuttonLabel.exportLabel")
nextButton.click()

radiobuttons = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupElContainer")
radiobuttons[2].click()

submitButton = driver.find_element_by_class_name("appsMaterialWizButtonPaperbuttonLabel quantumWizButtonPaperbuttonLabel exportLabel")
submitButton.click()
