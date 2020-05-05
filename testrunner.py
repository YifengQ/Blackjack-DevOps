import unittest
import BlackJack_UnitTests
import BlackJack_IntegrationTest

def create_suite():
    loader = unittest.TestLoader()
    test_suite = unittest.TestSuite()
    test_suite.addTest(loader.loadTestsFromModule(BlackJack_UnitTests))
    test_suite.addTest(loader.loadTestsFromModule(BlackJack_IntegrationTest))
    return test_suite

if __name__ == 'main':
    suite = create_suite()
    runner = unittest.TextTestRunner()
    runner.run(suite)
