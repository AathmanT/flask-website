from unittest import TestCase


class TestIntegration(TestCase):
    def setUp(self):
        self.time_stamps = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']

        self.year = "2019"
        self.tweets_data_path = 'output.txt'

    def integration_test_month_for_correct(self):
        from FilterTweetDataByMonth import preprocess
        from blei_executable_and_tethne import make_csv
        from plotting import plot

        type = "Month"

        preprocess(self.tweets_data_path, self.year, self.time_stamps)
        make_csv(self.time_stamps, type)
        self.assertTrue(plot(self.time_stamps, type) == True)

    def integration_test_year_for_correct(self):
        from FilterTweetDataByYear import preprocess
        from blei_executable_and_tethne import make_csv
        from plotting import plot

        type = "Year"

        preprocess(self.tweets_data_path, self.time_stamps)
        make_csv(self.time_stamps, type)
        self.assertTrue(plot(self.time_stamps, type) == True)
