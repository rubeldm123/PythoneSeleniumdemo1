class homePage():
    def __init__(self, driver):
        self.driver = driver

        self.welcomelinkbyID = "welcome"
        self.logoutlinkbyLinkText = "Logout"

    def clickOnWelcomeLink(self):
        self.driver.find_element_by_id(self.welcomelinkbyID).click()

    def clickOnLogOutBtn(self):
        self.driver.find_element_by_link_text(self.logoutlinkbyLinkText).click()
