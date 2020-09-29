


class loginPage():
    def __init__(self, driver):
        self.driver = driver

        self.userNameByID = "txtUsername"
        self.userPasswordByID = "txtPassword"
        self.clickonLoginByID = "btnLogin"

    def entersername(self, username):
        self.driver.find_element_by_id(self.userNameByID).send_keys(username)

    def enterusersassword(self, password):
        self.driver.find_element_by_id(self.userPasswordByID).send_keys(password)

    def clickonloginbtn(self):
        self.driver.find_element_by_id(self.clickonLoginByID).click()
