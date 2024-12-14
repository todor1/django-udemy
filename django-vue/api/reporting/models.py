from django.db import models

# Create your models here.

GENDER = (
    ("Masculine", "Masculine"),
    ("Feminine", "Feminine"),
    ("Prefer not to say", "Prefer not to say"),
)


class Category(models.Model):
    name = models.CharField(max_length=50)
    description = models.CharField(max_length=150)

    def __str__(self):
        return self.category_name


class Supplier(models.Model):
    company_name = models.CharField(max_length=50)
    contact_name = models.CharField(max_length=50)
    contact_title = models.CharField(max_length=50)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=100)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=100)
    phone = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    webpage = models.URLField(max_length=50)


class Customer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    gender = models.CharField(
        max_length=50, choices=GENDER, default="Prefer not to say"
    )
    title = models.CharField(max_length=10)
    address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    region = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    country = models.CharField(max_length=50)
    phone = models.CharField(max_length=20)
    email = models.EmailField()


class Product(models.Model):
    product_name = models.CharField(max_length=100)
    supplier = models.ForeignKey(Supplier, on_delete=models.DO_NOTHING, null=True)
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    unit_price = models.DecimalField(max_digits=10, decimal_places=2)
    units_in_stock = models.IntegerField()
    units_on_order = models.IntegerField()

    class Meta:
        ordering = ["category", "unit_price"]

    def __str__(self):
        return self.product_name


class Order(models.Model):
    order_date = models.DateTimeField()
    required_date = models.DateTimeField()
    shipped_city = models.CharField(max_length=100)
    shipped_name = models.CharField(max_length=100)
    shipped_address = models.CharField(max_length=200)
    shipped_postal_code = models.CharField(max_length=10)
    shipped_country = models.CharField(max_length=100)
    customer = models.ForeignKey(Customer, on_delete=models.DO_NOTHING)
    product = models.ForeignKey(Product, on_delete=models.DO_NOTHING)
