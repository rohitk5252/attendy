from selenium import webdriver
from selenium.webdriver.common.keys import Keys
# using Chrome to access web
driver = webdriver.Chrome()

# open wbsite 
driver.get('https://guru.gndec.ac.in/login/index.php')

# select the id box
id_box = driver.find_element_by_name('username')

#send information
id_box.send_keys('1921199')

# find password box
pass_box = driver.find_element_by_name('password')

#send password
pass_box.send_keys('O40881C')

# find login button
login_button = driver.find_element_by_id('loginbtn')

# click login
login_button.click()


# DBMS
# visiting DBMS Attendence
# driver.get('https://guru.gndec.ac.in/mod/attendance/attendance.php?sessid=80911&sesskey=y1FNeHyzid')

# # dbms att present
# dbms = driver.find_element_id('id_status_43334')
# dbms.click()

# # finding  SAVE CHANGES BUTTON
# save_changes = driver.find_element_by_id('id_submitbutton')

# # clicking SAVE CHANGEs button
# save_changes.click()




# # CAM 
# # visiting CAM attendance
# driver.get('https://guru.gndec.ac.in/mod/attendance/attendance.php?sessid=78631&sesskey=y1FNeHyzid')

# # CAM att present
# cam = driver.find_element_by_id('id_status_43554')
# cam.click()

# # finding  SAVE CHANGES BUTTON
# save_changes = driver.find_element_by_id('id_submitbutton')
# # clicking SAVE CHANGEs button
# save_changes.click()



#  WT attendance
driver.get('https://guru.gndec.ac.in/mod/attendance/attendance.php?sessid=75607&sesskey=8P2jKm9JM6')

# WT att find present
wt = driver.find_element_by_id('id_status_43322')
wt.click()

# finding  SAVE CHANGES BUTTON
save_changes = driver.find_element_by_id('id_submitbutton')
# clicking SAVE CHANGEs button
save_changes.click()
