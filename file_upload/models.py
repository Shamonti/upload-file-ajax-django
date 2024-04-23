from django.db import models

class UploadedFile(models.Model):
  filename = models.CharField(max_length=255)
  filepath = models.CharField(max_length=500)  # Adjust length as needed
  # Add other fields as needed (e.g., upload_date, content_type)

  def __str__(self):
    return self.filename
