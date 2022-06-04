from django.db import models
from django.contrib import auth

# Create your models here.




class Publisher(models.Model):
    name = models.CharField(max_length=50, help_text='Name of the publisher')
    website = models.URLField(help_text='Website of company')
    email = models.EmailField(help_text="Email address of the company")

    def __str__(self):
        return self.name
class Contributor(models.Model):
    first_name = models.CharField(max_length=50, help_text="First name of the contributor")
    last_name = models.CharField(max_length=50, help_text="Last name of the contributor")
    email = models.EmailField(help_text="Email Address of the contributor")

    def __str__(self):
        return self.first_name

class Book(models.Model):
    title = models.CharField(max_length=70, help_text="The title of the book")
    publication_date = models.DateField(verbose_name="Date the book was published")
    isbn = models.CharField(max_length=20, verbose_name="ISBN number of the book")
    """Many to one relation. Author have many books published. So books are many to one relaton with publisher
    So creating a foreignKey with Publisher
    """
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    """
    Many to Many relations
    A book has many contibutors and contirbutor has made contribution to many books. So adding
    many to many field
    """
    contributors = models.ManyToManyField(Contributor, through="BookContributor")

    def __str__(self):
        return self.title

class Review(models.Model):
    content = models.TextField(help_text="The Review Text")
    rating = models.IntegerField(help_text="The rating the reviewer has given")
    date_created = models.DateTimeField(auto_now_add=True, help_text="Date and time the review was created")
    date_edited = models.DateTimeField(null=True, help_text="The date and time the review was edited")
    creator = models.ForeignKey(auth.get_user_model(), on_delete=models.CASCADE)
    book = models.ForeignKey(Book, on_delete=models.CASCADE, help_text="The book this review has for")




class BookContributor(models.Model):
    class ContributorRole(models.TextChoices):
        AUTHOR = "AUTHOR", "Author"
        CO_AUTHOR = "CO_AUTHOR", "Co-Author"
        EDITOR = "EDITOR", "Editor"
    
    book = models.ForeignKey(Book, on_delete=models.CASCADE)

    contributor = models.ForeignKey(Contributor, on_delete=models.CASCADE)

    role = models.CharField(verbose_name="The role of this contributor had in the book", choices=ContributorRole.choices, max_length=20)