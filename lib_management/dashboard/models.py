from django.db import models


# Create your models here.
class Book(models.Model):
    bookid = models.CharField(verbose_name="Book id", primary_key=True, max_length=6)
    title = models.TextField(verbose_name="Title", max_length=255)
    price = models.IntegerField(verbose_name="Price")
    desc = models.TextField(verbose_name="Description")
    publication = models.TextField(verbose_name="Publication")
    isbn = models.CharField(verbose_name="ISBN", max_length=20)
    picture = models.ImageField(verbose_name="Picture", upload_to='books', blank=True)

    def __str__(self):
        return self.bookid + " " + self.title


class Copy(models.Model):
    status_choices = [
        ('Available', 'Available'),
        ('Damaged', 'Damaged'),
        ('Not Available', 'Not Available')
    ]
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)
    copy_no = models.IntegerField(verbose_name="Copy no")
    status = models.TextField(verbose_name="status", choices=status_choices, default='Available')

    def __str__(self):
        return str(self.bookid.bookid) + "/" + str(self.copy_no)


class Issue(models.Model):
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)
    roll_no = models.CharField(verbose_name="roll_no", max_length=8)
    copy_no = models.IntegerField(verbose_name="Copy no")
    date_issued = models.DateField(verbose_name="Date Issued", auto_now_add=True)
    date_returned = models.DateField(verbose_name="Date Returned", blank=True)
    renewed = models.BooleanField(verbose_name="Renewed", default=False)
    date_renewed = models.DateField(verbose_name="Date Renewed", blank=True)


class Author(models.Model):
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)
    author = models.CharField(verbose_name="Author", max_length=50)

    def __str__(self):
        return str(self.bookid.bookid) + " " + self.author


class Damage(models.Model):
    bookid = models.ForeignKey(Book, on_delete=models.CASCADE)
    roll_no = models.CharField(verbose_name="roll_no", max_length=8)
    copy_no = models.IntegerField(verbose_name="Copy no")
    damaged_on = models.DateField(verbose_name="Damaged on", auto_now_add=True)
    damage_desc = models.TextField(verbose_name="Damage Description")




