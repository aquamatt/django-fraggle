"System tests test functions, commands and template tags"

from fraggle.tests.common import Common

class System(Common):
    "System test suite"
    
    def test_template_tag_renders_content(self):
        self.assert_render_contains("test", 
            "{% load render_fragment %}{% render_fragment 'fragment1' %}")
        self.assert_render_contains("test", 
            "{% load render_fragment %}{% render_fragment 'fragment2' %}")
    
    def test_textile_transform_in_template_tag(self):
        self.assert_render("<div class='fraggle' id='fragment_1'>\t<p>test</p></div>", 
            "{% load render_fragment %}{% render_fragment 'fragment1' %}")
        self.assert_render("<div class='fraggle' id='fragment_2'>\t<h2>test</h2></div>", 
            "{% load render_fragment %}{% render_fragment 'fragment2' %}")

    def test_transform_with_form_elements(self):
        self.assert_render("<div class='fraggle' id='fragment_3'><form>test</form></div>",
            "{% load render_fragment %}{% render_fragment 'test_form' %}")
        
    def test_passing_invalid_fragment_identifier_renders_nothing(self):
        self.assert_render("", 
            "{% load render_fragment %}{% render_fragment 3 %}")
        self.assert_render("", 
            "{% load render_fragment %}{% render_fragment 'a' %}")
