
from playwright.sync_api import sync_playwright

with sync_playwright() as g:
    browser = g.firefox.launch()# headless=False, slow_mo=50
    web_page = browser.new_page()
    web_page.goto('https://ecampus.psgtech.ac.in/studzone2/')
    web_page.fill('input#txtusercheck', 'Rollno') # here #represents the CSS selector ID
    web_page.fill("input#txtpwdcheck", 'Password')
    web_page.click('input#abcd3')
    web_page.click('td#Title1_Menu1-menuItem002')
    web_page.click('td#Title1_Menu1-menuItem002-subMenu-menuItem002')
    web_page.wait_for_load_state("networkidle")
    web_page.screenshot(path='/home/gannadheesh/pic.png')

