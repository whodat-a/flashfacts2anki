from selenium import webdriver



driver = webdriver.Firefox()

with open('jquery.min.js', 'r') as jquery_js: #read the jquery from a file
    jquery = jquery_js.read()
    driver.execute_script(jquery)  #active the jquery lib

driver.get("http://usmle-rx.com")

fields = {"edit-name": "jcolema4@tulane.edu",
          "edit-pass": "MLD^ozb9gGAW"}

for name, value in fields.items():
    elem = driver.find_element_by_id(name)
    elem.send_keys(value)

submit = driver.find_elements_by_id("edit-submit")[1]
submit.click()

flash_facts_link = driver.find_element_by_css_selector('td.cell-application > a').click()

create_deck_script = 'document.getElementById("#cmdCreateDeck").click(UsmleUI.Application.FlashFacts.CreateDeck.CreateNewDeck)'

driver.execute_script(create_deck_script)

# driver.find_element_by_xpath("contains(@id)")

# Main_headings = driver.find_elements_by_class_name("liSection")

# print len(main_headings)
