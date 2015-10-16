__author__ = 'slaureano'


    def test_example(self):
        test_dict = {'te=': 1, 'b': 2, 'c': 3}
        try:
            if test_dict['test']:
                print "found"
        except:
            print "not found"


    def test_example1(self):
        test_dict = {'te=': 1, 'b': 2, 'c': 3}
        if test_dict['test']:
            print "found"
        else:
            print "not found"


    def test_example2(self):
        test_dict = {'te=': 1, 'b': 2, 'c': 3}
        try:
            fdfd
            if test_dict['test']:
                print "found"

        except (KeyError, NameError) as Errors:
            print "not found"
            print "exception:", Errors

        finally:
            pass

