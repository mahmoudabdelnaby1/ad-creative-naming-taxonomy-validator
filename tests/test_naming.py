import unittest
import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent.parent / "src"))
from naming_validator import validate_naming

class TestNaming(unittest.TestCase):
    def test_validator(self):
        csv_p = Path(__file__).resolve().parent.parent / "examples" / "ad_names_sample.csv"
        rules_p = Path(__file__).resolve().parent.parent / "config" / "taxonomy_rules.json"
        out_p = Path(__file__).resolve().parent.parent / "reports" / "validation_errors.csv"
        errors = validate_naming(str(csv_p), str(rules_p), str(out_p))
        self.assertGreaterEqual(errors, 1)

if __name__ == "__main__":
    unittest.main()
