from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select

driver = webdriver.Chrome()
driver.get("https://www.saucedemo.com/")

# Login
driver.find_element(By.ID, "user-name").send_keys("standard_user")
driver.find_element(By.ID, "password").send_keys("secret_sauce")
driver.find_element(By.ID, "login-button").click()

title = driver.find_element(By.CLASS_NAME, "title").text

assert "Products" in title, "cannot login"

# Sorting
select = Select(driver.find_element(By.CLASS_NAME, "product_sort_container"))
select.select_by_value("az")

products = driver.find_elements(By.CLASS_NAME, "inventory_item_name")
sorted_products = sorted([p.text for p in products])

assert sorted_products == [p.text for p in products], "Products are not sorted"

# Purchasing process
driver.find_element(By.ID, "add-to-cart-sauce-labs-fleece-jacket").click()

driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()

driver.find_element(By.ID, "checkout").click()

driver.find_element(By.ID, "first-name").send_keys("Michal")
driver.find_element(By.ID, "last-name").send_keys("Kowalski")
driver.find_element(By.ID, "postal-code").send_keys("01-022")

driver.find_element(By.ID, "continue").click()
driver.find_element(By.ID, "finish").click()

finalTextHeader = driver.find_element(By.CLASS_NAME, "complete-header").text
finalText = driver.find_element(By.CLASS_NAME, "complete-text").text

assert "Thank you for your order!" in finalTextHeader, "Error in final header text"
assert "Your order has been dispatched, and will arrive just as fast as the pony can get there!" in finalText, "Error in final text"


# driver.quit()
