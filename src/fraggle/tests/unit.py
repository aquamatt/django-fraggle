"Unit tests are low level tests which test object methods and properties"

from fraggle.tests.common import Common
from fraggle.models import Fragment

class Unit(Common):
    "Unit test suite"

    def test_object_creation(self):
        self.assert_counts([3], [Fragment])

    def test_creation_of_fragments(self):
        Fragment.objects.all().delete()
        self.assert_counts([0], [Fragment])
        fragment1 = Fragment(
            title='fragment1',
            content='test'
        )
        fragment1.save()
        self.assert_equal(fragment1.title, 'fragment1')
        self.assert_equal(fragment1.content, 'test')
        
        self.assert_counts([1], [Fragment])
        
    def test_creation_of_fragments_without_content(self):
        Fragment.objects.all().delete()
        self.assert_counts([0], [Fragment])
        fragment2 = Fragment(
            title='fragment2',
        )
        fragment2.save()
        self.assert_counts([1], [Fragment])
        self.assert_equal(fragment2.title, 'fragment2')
        self.assert_equal(fragment2.content, '')
        
    def test_creation_of_fragments_without_title(self):
        Fragment.objects.all().delete()
        self.assert_counts([0], [Fragment])
        fragment1 = Fragment(
            content='test'
        )
        fragment1.save()
        self.assert_counts([1], [Fragment])
        self.assert_equal(fragment1.title, '')
        self.assert_equal(fragment1.content, 'test')

    def test_html_is_saved_from_content(self):
        self.assert_equal(self.fragment1.html,"\t<p>test</p>")
        self.assert_equal(self.fragment2.html,"\t<h2>test</h2>")
        
    def test_html_from_formatted_content(self):
        self.assert_equal(self.fragment1.transform_content(),"\t<p>test</p>")
        self.assert_equal(self.fragment2.transform_content(),"\t<h2>test</h2>")
