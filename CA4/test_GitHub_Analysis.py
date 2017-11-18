
import unittest

from GitHub_Analysis import get_commits, read_file
            
class TestCommits(unittest.TestCase):

    def setUp(self):
        self.data = read_file('changes_python.log')

    #test code rading 5255 lines
    def test_number_of_lines(self):
        self.assertEqual(5255, len(self.data))

    def test_number_of_commits(self):
        commits = get_commits(self.data)
        self.assertEqual(422, len(commits))

    def test_first_commit(self):
        commits = get_commits(self.data)
        self.assertEqual('Thomas', commits[0].author)
        self.assertEqual('Jimmy', commits[420].author)
        self.assertEqual('r1551925', commits[0].revision)
        self.assertEqual(['SFR-108 : Create bilingual French/English translated Android application for SFR', '-----------', 'three dots. "..."'],
                commits[23].comment)
        self.assertEqual(['A /cloud/personal/client-international/android/branches/android-15.2-solutions/libs/ui/res/layout/permission_list_item.xml (from /cloud/personal/client-international/android/branches/android-15.2-solutions-att-m/libs/ui/res/layout/permission_list_item.xml:1548354)'],
                commits[40].changed_path)
        
if __name__ == '__main__':
    unittest.main()
