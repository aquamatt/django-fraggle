"Models for Fraggle fragment manager for Django"

from django.db import models
from django.contrib.markup.templatetags.markup import textile
from django.utils.safestring import mark_safe
 
class Fragment(models.Model):
    "Represents an html fragment"
    title = models.CharField(max_length=250, unique = True, db_index = True)
    content = models.TextField(help_text=u'You may use Textile for formatting.')
    html = models.TextField(blank=True, null=True)
    use_textile = models.BooleanField(default=True, help_text = "Interpret content as textile formatted")
    
    def transform_content(self):
        "Return the textile transformed content. Also found in html property."
        return textile(self.content)
        
    def save(self, *args, **kwargs):
        "On saving fragment, save textile formatted html into html property if use_textile is True"
        if self.use_textile:
            self.html = textile(self.content)
        else:
            self.html = self.content

        super(Fragment, self).save(*args, **kwargs)

    def _templatetag(self):
        return mark_safe("{%% load render_fragment %%}{%% render_fragment '%s' %%}" % self.title)

    _templatetag.short_description = "Template tag"

    def __unicode__(self):
        return self.title
