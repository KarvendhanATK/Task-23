from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

# Initialize the WebDriver 
driver = webdriver.Chrome()
driver.maximize_window()

# Navigate to the URL
driver.get("https://jqueryui.com/droppable/")
time.sleep(2) 

# Switch to the iframe containing the drag and drop elements
iframe_index = 0  # it is at index 0
driver.switch_to.frame(iframe_index)

# Locate the draggable and droppable elements
draggable = driver.find_element(By.ID, "draggable")
droppable = driver.find_element(By.ID, "droppable")

# Perform the drag and drop action
actions = ActionChains(driver)
actions.drag_and_drop(draggable, droppable).perform()
time.sleep(2) 

print("Drag and Drop operation completed.")

# Close the browser
driver.quit()
