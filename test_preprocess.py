from unittest import TestCase


class TestPreprocess(TestCase):


    def test_preprocess_for_correct(self):
        from FilterTweetData import preprocess
        time_stamps = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        tweets_data_path = 'output.txt'
        self.assertTrue(preprocess(tweets_data_path,time_stamps)==True)

    def test_preprocess_file_empty(self):
        from FilterTweetData import preprocess
        time_stamps = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        tweets_data_path = 'empty.txt'
        self.assertTrue(preprocess(tweets_data_path,time_stamps)==False)

    def test_preprocess_file_only_one_invalid(self):
        from FilterTweetData import preprocess
        time_stamps = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        tweets_data_path = 'invalid.txt'
        self.assertTrue(preprocess(tweets_data_path,time_stamps)==False)
    def test_preprocess_file_one_invalid_others_correct(self):
        from FilterTweetData import preprocess
        time_stamps = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        tweets_data_path = 'invalid_others_correct.txt'
        self.assertTrue(preprocess(tweets_data_path,time_stamps)==True)