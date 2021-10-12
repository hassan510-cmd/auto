from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

def track():
    import subprocess
    import time
    import datetime
    last_date=subprocess.run("ls  -ltr --time-style=full-iso  | tail -1 | cut -d \" \" -f 7,8,9,10",shell=True,capture_output=True).stdout
    
    while True:
        time.sleep(1)
        current_date=subprocess.run("ls  -ltr --time-style=full-iso  | tail -1 | cut -d \" \" -f 7,8,9,10",shell=True,capture_output=True).stdout
        if current_date == last_date:
            print(f'no change at {datetime.datetime.now().strftime("%h %d %a %I:%M:%S")}'.center(50,"*"))
        else :
            file_name=subprocess.run("ls  -ltr --time-style=full-iso  | tail -1 | cut -d \" \" -f 10",shell=True,capture_output=True).stdout
            print(f'change detected in {file_name.decode("utf-8")}'.center(80,"-"))
            last_date=current_date
            
# datetime.datetime.now().strftime("%h %d %a %I:%M:%S") sdadsad



browser=webdriver.Chrome(ChromeDriverManager().install())
login="http://apps.iti.gov.eg/ManagementSystem/intlogin.aspx"
browser.get(login)
browser.find_element_by_id("txtUsername").send_keys("HAAL26512")
browser.find_element_by_id("txtpassword").send_keys("iti3")
browser.find_element_by_id("btnlogin").click()

# open courses list
browser.find_element_by_id("ContentPlaceHolder1_UcCourseEval1_ddlCourseName_chzn").click()
# save courses
courses=browser.find_element_by_class_name("chzn-results").find_elements_by_tag_name("li")
# access first course
courses[0].click()
# collect starts
stars=browser.find_elements_by_class_name("ratingStar")

for star in stars[::-1] :
    if  stars.index(star)%5==4:
        star.click()

finish=browser.find_element_by_id('ContentPlaceHolder1_UcCourseEval1_btnSave').click()