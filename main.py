import time

from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # Set up the remote webdriver
    #driver = webdriver.Remote(
        #command_executor='http://0.0.0.0:4444/wd/hub',
        #options=chromeOptions
    #)
    chrome_options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(ChromeDriverManager().install())

    #version = driver.execute_script('return (window.chrome || {}).webdriver_version || "N/A"')
    #print("ChromeDriver version: ", version)

    driver.get('https://api.pekabex.pl')

    button = driver.find_element(By.XPATH, "/html/body/main/div/div[2]/div/form[1]/button")
    button.click()

    driver.implicitly_wait(5)
    inputElement = driver.find_element(By.ID, 'i0116')
    inputElement.send_keys('dupa jas')

    time.sleep(90)

    driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
