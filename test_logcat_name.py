from unittest import TestCase

# import filename_parser
import logcat_name


class Test(TestCase):
    log_dir = "/disk2/thomas/sjPBP/DMS/GRACE-89/03/Log.2"

    def testcase_parse_dir(self):
        count = logcat_name.parse_dir(self.log_dir)
        print "count: %2d" % count
        # self.fail()
        pass

    def testcase_parse_file(self):
        no = logcat_name.parse_file("logcat.log.18")
        if no:
            print no
        pass
