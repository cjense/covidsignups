from selenium import webdriver

# webdriver location
driver = webdriver.Chrome("C:\\Users\\clair\\Desktop\\python projects\\chromedriver.exe")

# initialize URL
url = "https://www.amherst.edu/go/student-health-survey"
driver.get(url)

# find all radio buttons
radiobuttons = driver.find_elements_by_class_name("appsMaterialWizToggleRadiogroupElContainer")
print(radiobuttons)