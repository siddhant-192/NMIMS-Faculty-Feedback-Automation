from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

def search_and_get_query(sap_id,sap_pass,rate):
    
    driver = webdriver.Chrome()
    driver.get("https://www.google.com")
    search_box = driver.find_element(by=By.NAME,value="q")
    search_box.send_keys("svkm portal login")
    search_box.send_keys(Keys.RETURN)

    driver.implicitly_wait(5)

    search_results = driver.find_element(by=By.CSS_SELECTOR,value="h3.LC20lb.MBeuO.DKV0Md")
    
    if search_results:
        first_result = search_results
        first_result.click()

        driver.implicitly_wait(5)

        username_box = driver.find_element(by=By.CSS_SELECTOR, value="input#userName.focus.form-control")

        username_box.send_keys(sap_id)

        password_box = driver.find_element(by=By.CSS_SELECTOR, value="input#userPwd.form-control")

        password_box.send_keys(sap_pass)

        login_btn = driver.find_element(by=By.CSS_SELECTOR, value="input#userLogin.btn.btn-danger.w-100.loginBtn")

        login_btn.click()

        time.sleep(10)
        driver.get("https://portal.svkm.ac.in/MPSTME-NM-M/viewFeedbackDetails")

        feedback_form = driver.find_element(By.PARTIAL_LINK_TEXT, "Faculty Feedback")
        #feedback_form = driver.find_element(by=By.XPATH,value="//*[contains(text(), '{Faculty Feedback}')]")

        feedback_form.click()

        feedback_button = driver.find_element(by=By.CSS_SELECTOR, value="a.btn.btn-info")

        feedback_button.click()

        for j in range(12):
            def feedback_btn_click(elem_no,page_no):

                btn_css_val= "select#answer"+str(page_no)+str(elem_no)+".form-control.form-control-sm"

                feedback_q = driver.find_element(by=By.CSS_SELECTOR, value=btn_css_val)

                drop = Select(feedback_q)

                drop.select_by_value(rate)

                time.sleep(0.2) 

                if j==10:
                    feedback_q = driver.find_element(by=By.CSS_SELECTOR, value="select#answer100.form-control.form-control-sm")

                    drop = Select(feedback_q)

                    drop.select_by_value(rate)

                    feedback_q = driver.find_element(by=By.CSS_SELECTOR, value="select#answer101.form-control.form-control-sm")

                    drop = Select(feedback_q)

                    drop.select_by_value(rate)

                    feedback_q = driver.find_element(by=By.CSS_SELECTOR, value="select#answer102.form-control.form-control-sm")

                    drop = Select(feedback_q)

                    drop.select_by_value(rate)

                if j==11:
                    feedback_q = driver.find_element(by=By.CSS_SELECTOR, value="select#answer110.form-control.form-control-sm")

                    drop = Select(feedback_q)

                    drop.select_by_value(rate)

                    feedback_q = driver.find_element(by=By.CSS_SELECTOR, value="select#answer111.form-control.form-control-sm")

                    drop = Select(feedback_q)

                    drop.select_by_value(rate)

                    feedback_q = driver.find_element(by=By.CSS_SELECTOR, value="select#answer112.form-control.form-control-sm")

                    drop = Select(feedback_q)

                    drop.select_by_value(rate)

            for i in range(15):
                try:
                    feedback_btn_click(i,j)
                except Exception as e:
                    continue


            next_btn = driver.find_element(by=By.CSS_SELECTOR, value="button#btn"+str(j+1)+".btn.btn-success.btn-common.next-step.next-button")

            next_btn.click()

            time.sleep(3)

        time.sleep(10)

        finish_btn = driver.find_element(by=By.XPATH,value="//*[contains(text(), 'Finish')]")

        finish_btn.click()

        time.sleep(5)

        ok_button = driver.find_element(by=By.XPATH,value="//*[contains(text(), 'Ok')]")

        ok_button.click()

        time.sleep(10)

        print("Task Completed.")
        
        driver.quit()
    else:
        driver.quit()

usr = input("Enter SAP ID: ")
pas = input("Enter Password: ")
rt = input("Enter rating: ")

search_and_get_query(usr,pas,rt)