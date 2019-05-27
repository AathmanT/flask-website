from unittest import TestCase


class TestIntegration(TestCase):
    def setUp(self):
        self.time_stamps_month = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        self.time_stamps_year = ["2010","2011","2012","2013","2014","2015","2019"]
        self.year = "2019"
        self.tweets_data_path = 'output.txt'

    def test_integration_month_for_correct(self):
        from FilterTweetDataByMonth import preprocess
        from blei_executable_and_tethne import make_csv
        from plotting import plot

        type = "Month"

        preprocess(self.tweets_data_path, self.year, self.time_stamps_month)
        self.assertTrue(make_csv(self.time_stamps_month, type)==True)
        self.assertTrue(plot(self.time_stamps_month, type) == True)

    def test_integration_test_year_for_correct(self):
        from FilterTweetDataByYear import preprocess
        from blei_executable_and_tethne import make_csv
        from plotting import plot

        type = "Year"

        preprocess(self.tweets_data_path, self.time_stamps_year)
        self.assertTrue(make_csv(self.time_stamps_year, type)==True)
        self.assertTrue(plot(self.time_stamps_year, type) == True)

    def test_integration_test_month_for_wrong(self):
        from FilterTweetDataByMonth import preprocess
        from blei_executable_and_tethne import make_csv
        from plotting import plot

        type = "Month"

        if preprocess("empty.txt", self.year, self.time_stamps_month):
            self.assertTrue(make_csv(self.time_stamps_month, type)==True)
            self.assertTrue(plot(self.time_stamps_month, type) == True)



    def test_integration_test_year_for_wrong(self):
        from FilterTweetDataByYear import preprocess
        from blei_executable_and_tethne import make_csv
        from plotting import plot

        type = "Year"

        if preprocess("empty.txt", self.time_stamps_year):
            self.assertTrue(make_csv(self.time_stamps_year, type)==True)
            self.assertTrue(plot(self.time_stamps_year, type) == True)
