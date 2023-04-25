import allure
class Test:
    @allure.title("Test login")
    def test_002(self,web_login):
        print("This is a test")
