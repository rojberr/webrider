from selenium import webdriver

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

    # Set up the remote webdriver
    driver = webdriver.Remote(
        command_executor='http://localhost:4444/wd/hub',
        desired_capabilities={'browserName': 'chrome'}
    )

    driver.get('https://www.google.com')

    driver.implicitly_wait(99999999999999999999)

    driver.quit()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
