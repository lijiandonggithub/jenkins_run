class TestLogin:

    def test_login_001(self):
        print("问题已修复Bug.001")
        assert 1

    def test_login_002(self):
        assert 1

    def test_login_003(self):
        assert 1


# cd jenkins_run
# allure generate report/ -o report/html --clean https://github.com/lijiandonggithub/jenkins_opject.git