""" Used Command : 
    ' pytest ' 
    for Run this file.
"""

import re 
from playwright.sync_api import Page, expect

def test_has_title(page: Page):
    # Open Browser
    page.goto("https://playwright.dev/")

    # Verify that the page title contains "Playwright"
    expect(page).to_have_title(re.compile("Playwright"))

def test_get_started_link(page: Page):
    # Open Browser
    page.goto("https://playwright.dev/")

    # Click element 
    page.get_by_role("link", name="Get started").click()

    # Verify that the page heading with the name "Installation" is visible
    expect(page.get_by_role("heading", name="Installation")).to_be_visible()

    # to_be_visible() is used to check if an element is visible on the page and not hidden.

