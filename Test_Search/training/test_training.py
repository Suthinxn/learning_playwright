import re
import time
from playwright.sync_api import Page, expect

def test_search_information(page: Page):

    # Open Training-diis
    page.goto("http://localhost:8080/")
    page.screenshot(path="01-site-page.png")

    # Login page
    page.get_by_role("link", name="Login").click()
    page.screenshot(path="02-login-page.png")

    # Filled info for login 
    page.get_by_label("ชื่อผู้ใช้").fill("admin")
    # อาจจะมีวิธีที่ดีกว่านี้
    page.get_by_label("รหัสผ่าน").fill("1234")
    page.screenshot(path="03-filled-login-page.png")

    # Login success
    page.keyboard.press("Enter")
    page.wait_for_load_state("networkidle")
    page.screenshot(path="04-login-success.png")

    # sit page
    page.get_by_role("link", name="ยืนยัน").click()
    page.screenshot(path="05-site-page.png")

