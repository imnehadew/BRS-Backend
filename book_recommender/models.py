from django.db import models

class Book(models.Model):
    ISBN = models.CharField(max_length=25, primary_key=True, db_column="ISBN")
    Book_Title = models.CharField(max_length=255, db_column="Book_Title")
    Book_Author = models.CharField(max_length=80, null=True, blank=True, db_column="Book_Author")
    Category = models.CharField(max_length=255, null=True, blank=True, db_column="Category")
    Year_Of_Publication = models.BigIntegerField(null=True, blank=True, db_column="Year_Of_Publication")
    Publisher = models.CharField(max_length=255, null=True, blank=True, db_column="Publisher")
    Image_URL_S = models.CharField(max_length=255, null=True, blank=True, db_column="Image_URL_S")
    Image_URL_M = models.CharField(max_length=255, null=True, blank=True, db_column="Image_URL_M")
    Image_URL_L = models.CharField(max_length=255, null=True, blank=True, db_column="Image_URL_L")

    class Meta:
        managed = False
        db_table = 'books'
