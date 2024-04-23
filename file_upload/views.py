from django.shortcuts import render, HttpResponse
from django.core.files.storage import default_storage
from .models import UploadedFile  # Import your model (replace with your actual model path)
import psycopg2  # Import psycopg2 for PostgreSQL connection

def upload_file(request):
  if request.method == 'POST':
    uploaded_file = request.FILES['file']

    # File validation (optional):
    # Check for supported file types, size limits, etc.
    # if uploaded_file.size > 1048576 (1 MB):  # Example size limit
    #     return HttpResponseBadRequest("File size exceeds limit (1 MB)")

    try:
      # Save uploaded file:
      filename = default_storage.save(uploaded_file.name, uploaded_file)

      # Connect to PostgreSQL database:
      conn = psycopg2.connect(
          database="uploadFile",
          user="postgres",
          password="9629",
          host="localhost",
          port="5432"  # Optional, default is 5432
      )

      # Prepare SQL statement and execute:
      cursor = conn.cursor()
      sql = "INSERT INTO files (filename, filepath) VALUES (%s, %s)"
      cursor.execute(sql, (filename, default_storage.url(filename)))  # Use url for filepath
      conn.commit()

      return HttpResponse("File uploaded and information stored in database.")

    except Exception as e:
      # Handle exceptions (e.g., file upload error, database connection error)
      return HttpResponseBadRequest(f"Error uploading file: {str(e)}")

    finally:
      # Close database connection if opened
      if conn:
        cursor.close()
        conn.close()

  else:
    return HttpResponseBadRequest("Invalid request method")
