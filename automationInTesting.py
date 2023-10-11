from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.action_chains import ActionChains
import time

chrome_options = Options()
chrome_options.add_argument("--lang=pl-PL")

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://automationintesting.online/")
driver.implicitly_wait(1)

# User Story 1 Testing Scenario 1

driver.find_element(By.XPATH, "//button[text()='Book this room']").click()
driver.implicitly_wait(1)

driver.find_element(By.XPATH, "//button[contains(@class, 'btn-outline-primary') and contains(@class, 'float-right') and contains(@class, 'book-room')]").click()

alert = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger")
paragraphs = alert.find_elements(By.TAG_NAME, "p")

errors = []

for paragraph in paragraphs:
    errors.append(paragraph.text)

assert "nie może być puste" in errors, "Nie znaleziono błędu o pustym imieniu"
assert "nie może mieć wartości null" in errors, "Nie znaleziono błędu o pustym nazwisku"
assert "Firstname should not be blank" in errors, "Nie znaleziono błędu o pustym imieniu"
assert "Lastname should not be blank" in errors, "Nie znaleziono błędu o pustym nazwisku"
assert "wielkość musi należeć do zakresu od 11 do 21" in errors, "Nie wyświetlono błedu"
assert "wielkość musi należeć do zakresu od 3 do 18" in errors, "Nie wyświetlono błedu"
assert "wielkość musi należeć do zakresu od 3 do 30" in errors, "Nie wyświetlono błedu"

# User Story 1 Testing Scenario 2

driver.refresh()
driver.implicitly_wait(1)

driver.find_element(By.XPATH, "//button[text()='Book this room']").click()
driver.implicitly_wait(1)

driver.find_element(By.NAME, "firstname").send_keys("Adam")
driver.find_element(By.NAME, "lastname").send_keys("Nowak")
driver.find_element(By.NAME, "email").send_keys("adamnowak@gmail.com")
driver.find_element(By.NAME, "phone").send_keys("123456789")

driver.find_element(By.XPATH, "//button[contains(@class, 'btn-outline-primary') and contains(@class, 'float-right') and contains(@class, 'book-room')]").click()

alert = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger")
paragraphs = alert.find_elements(By.TAG_NAME, "p")

errors = []

for paragraph in paragraphs:
    errors.append(paragraph.text)

assert "nie może mieć wartości null" in errors, "Nie znaleziono błędu o pustym nazwisku"
assert "wielkość musi należeć do zakresu od 11 do 21" in errors, "Nie wyświetlono błedu"

# User Story 1 Testing Scenario 3

driver.refresh()
driver.implicitly_wait(1)

driver.find_element(By.XPATH, "//button[text()='Book this room']").click()
driver.implicitly_wait(1)

driver.find_element(By.NAME, "firstname").send_keys("Adam")
driver.find_element(By.NAME, "lastname").send_keys("Nowak")
driver.find_element(By.NAME, "email").send_keys("adamnowak@gmail.com")
driver.find_element(By.NAME, "phone").send_keys("1234567891111")

driver.find_element(By.XPATH, "//button[text()='Next']").click()

start_date = driver.find_element(By.XPATH, "//button[contains(text(),'20')]")

end_date = driver.find_element(By.XPATH, "//button[contains(text(),'22')]")

actions = ActionChains(driver)

actions.click_and_hold(start_date)
actions.move_by_offset(0, 20)
actions.move_to_element(end_date)

actions.release(end_date)

actions.perform()

driver.implicitly_wait(1)

driver.find_element(By.XPATH, "//button[contains(@class, 'btn-outline-primary') and contains(@class, 'float-right') and contains(@class, 'book-room')]").click()

driver.implicitly_wait(1)

# succcess message
success_alert = driver.find_element(By.XPATH, "//div[@class='col-sm-6 text-center']")

success_message_h3 = success_alert.find_element(By.TAG_NAME, "h3")
success_message_p = success_alert.find_element(By.TAG_NAME, "p")

assert success_message_h3.text == "Booking Successful!", "Nie wyświetlono komunikatu o powodzeniu rezerwacji"
assert success_message_p.text == "Congratulations! Your booking has been confirmed for:", "Nie wyświetlono komunikatu o powodzeniu rezerwacji"

# User Story 2 Testing Scenario 1

driver.refresh()
driver.implicitly_wait(1)

driver.find_element(By.ID, 'email').send_keys("obajtek@frajer.com")
driver.find_element(By.ID, 'phone').send_keys("123123123123")
driver.find_element(By.ID, 'subject').send_keys("witam")
driver.find_element(By.ID, 'description').send_keys("kto pokrył 2 miliardy strat orlenu?")   

driver.find_element(By.ID, "submitContact").click()

driver.implicitly_wait(1)

alert = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger")
paragraphs = alert.find_elements(By.TAG_NAME, "p")

assert "Name may not be blank" == paragraphs[0].text, "Nie wyświetlono błędu o pustym imieniu"

# User Story 2 Testing Scenario 2

driver.refresh()
driver.implicitly_wait(1)

driver.find_element(By.ID, 'name').send_keys("Daniel")
driver.find_element(By.ID, 'phone').send_keys("123123123123")
driver.find_element(By.ID, 'subject').send_keys("witam")
driver.find_element(By.ID, 'description').send_keys("kto pokrył 2 miliardy strat orlenu?")   

driver.find_element(By.ID, "submitContact").click()

driver.implicitly_wait(1)

alert = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger")
paragraphs = alert.find_elements(By.TAG_NAME, "p")

assert "Email may not be blank" == paragraphs[0].text, "Nie wyświetlono błędu o pustym emailu"

# User Story 2 Testing Scenario 3

driver.refresh()
driver.implicitly_wait(1)

driver.find_element(By.ID, 'name').send_keys("Daniel")
driver.find_element(By.ID, 'email').send_keys("obajtek@frajer.com")
driver.find_element(By.ID, 'subject').send_keys("witam")
driver.find_element(By.ID, 'description').send_keys("kto pokrył 2 miliardy strat orlenu?")   

driver.find_element(By.ID, "submitContact").click()

driver.implicitly_wait(1)

alert = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger")
paragraphs = alert.find_elements(By.TAG_NAME, "p")

assert "Phone must be between 11 and 21 characters." == paragraphs[0].text, "Nie wyświetlono błędu o złym numerze telefonu"

# User Story 2 Testing Scenario 4

driver.refresh()
driver.implicitly_wait(1)

driver.find_element(By.ID, 'name').send_keys("Daniel")
driver.find_element(By.ID, 'email').send_keys("obajtek@frajer.com")
driver.find_element(By.ID, 'phone').send_keys("123123123123")
driver.find_element(By.ID, 'description').send_keys("kto pokrył 2 miliardy strat orlenu?")   

driver.find_element(By.ID, "submitContact").click()

driver.implicitly_wait(1)

alert = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger")
paragraphs = alert.find_elements(By.TAG_NAME, "p")

assert "Subject may not be blank" == paragraphs[0].text, "Nie wyświetlono błędu o braku tematu"

# User Story 2 Testing Scenario 5

driver.refresh()
driver.implicitly_wait(1)

driver.find_element(By.ID, 'name').send_keys("Daniel")
driver.find_element(By.ID, 'email').send_keys("obajtek@frajer.com")
driver.find_element(By.ID, 'phone').send_keys("123123123123")
driver.find_element(By.ID, 'subject').send_keys("witam")

driver.find_element(By.ID, "submitContact").click()

driver.implicitly_wait(1)

alert = driver.find_element(By.CSS_SELECTOR, "div.alert.alert-danger")
paragraphs = alert.find_elements(By.TAG_NAME, "p")

assert "Message must be between 20 and 2000 characters." == paragraphs[0].text, "Nie wyświetlono błędu o braku contentu wiadomości"

# User Story 2 Testing Scenario 6

driver.refresh()
driver.implicitly_wait(1)

imie = "Daniel"

driver.find_element(By.ID, 'name').send_keys(imie)
driver.find_element(By.ID, 'email').send_keys("obajtek@frajer.com")
driver.find_element(By.ID, 'phone').send_keys("123123123123")
driver.find_element(By.ID, 'subject').send_keys("witam")
driver.find_element(By.ID, 'description').send_keys("kto pokrył 2 miliardy strat orlenu?")   

driver.find_element(By.ID, "submitContact").click()

driver.implicitly_wait(1)

success_message = driver.find_element(By.XPATH, "//div[@style='height: 412px;']").find_element(By.TAG_NAME, "h2")

assert (f"Thanks for getting in touch {imie}!") == success_message.text, "Nie wyświetlono komunikatu o powodzeniu wysłania wiadomości"

# User Scenario 3 Testing Scenario 1

driver.get("https://automationintesting.online/#/admin")
driver.implicitly_wait(1)

password_input = driver.find_element(By.ID, "password")

password_input.send_keys("password")

driver.find_element(By.ID, "doLogin").click()

time.sleep(1)

style = password_input.get_attribute('style')

assert "border: 1px solid red;" in style, "Nie wyświetlono błędu o złym loginie"

# User Scenario 3 Testing Scenario 2

driver.refresh()
driver.implicitly_wait(1)

login_input = driver.find_element(By.ID, "username")

login_input.send_keys("username")

driver.find_element(By.ID, "password").send_keys("aaaa")

driver.find_element(By.ID, "doLogin").click()

time.sleep(1)

style = login_input.get_attribute('style')

assert "border: 1px solid red;" in style, "Nie wyświetlono błędu o złym haśle"

# User Scenario 3 Testing Scenario 3

driver.refresh()
driver.implicitly_wait(1)

driver.find_element(By.ID, "username").send_keys("admin")
driver.find_element(By.ID, "password").send_keys("password")

driver.find_element(By.ID, "doLogin").click()

time.sleep(1)

logout_link = driver.find_element(By.LINK_TEXT, "Logout")
front_page = driver.find_element(By.ID, "frontPageLink")

assert "Logout" == logout_link.text, "Nie zalogowano"
assert "Front Page" == front_page.text, "Nie zalogowano"

driver.quit()