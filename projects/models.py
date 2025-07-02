from django.db import models
from ckeditor.fields import RichTextField
from django.template.defaultfilters import slugify

# Create your models here.
class PersonalProject(models.Model):
    class Meta:
        verbose_name_plural = 'Personal Projects'
        verbose_name = 'Personal Project'
        ordering = ["name"]

    date = models.DateTimeField(blank=True, null=True)
    name = models.CharField(max_length=200, blank=True, null=True)
    description = models.CharField(max_length=500, blank=True, null=True)
    body = RichTextField(blank=True, null=True)
    slug = models.SlugField(null=True, blank=True)
    image = models.ImageField(blank=True, null=True, upload_to="personal_projects/")

    def save(self, *args, **kwargs):
        if not self.id:
            self.slug = slugify(self.name)
        super(PersonalProject, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return f"/personal-project/{self.slug}"