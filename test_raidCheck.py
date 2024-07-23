import unittest
from raidCheck import parse_perccli

class TestRaidCheck(unittest.TestCase):
  def test_parse_perccli_normal(self):
    with open("sample.txt","r") as f :
      output = f.read()
    out = parse_perccli(output)

    for drive in out :
      for disk in out[drive] :
        self.assertEqual(out[drive][disk],'Onln',"Should parse as online")


if __name__ == '__main__':
    unittest.main()
