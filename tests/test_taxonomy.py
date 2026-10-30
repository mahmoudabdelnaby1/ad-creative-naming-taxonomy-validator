"""
Unit tests for Ad Taxonomy Validator
"""
import unittest
from src.taxonomy_linter import validate_creative_name

class TestTaxonomyLinter(unittest.TestCase):
    def test_valid_ad_name(self):
        name = "TIKTOK_CONV_UAE_MOTION_OFFER_9X16_V02"
        res = validate_creative_name(name)
        self.assertTrue(res["valid"])
        self.assertEqual(res["parsed_metadata"]["geo"], "UAE")

    def test_invalid_tokens_count(self):
        name = "META_CONV_TEST"
        res = validate_creative_name(name)
        self.assertFalse(res["valid"])

if __name__ == "__main__":
    unittest.main()
