from django.db import models

# Create your models here.


# ferr = [
#   ('1', '1'),
#   ('1.5', '1.5'),
#   ('2', '2')
# ]

# ferr = [

#     ('one', '1'),
#     ('one point five', '1.5'),
#     ('two', '2')

# ]

ferrules = [
    ('N/A', 'n/a'),
    ('one', 1),
    ('one comma five', float(1.5)),
    ('two', 2),
    ('four', 4),
    ('six', 6),
    ('eight', 8),
    ('twenty five', 25),
    ('thirty five', 35),
    ('fifty', 50),
    ('seventy', 70),
    ('ninety five',  95),
    ('one hundred and twenty', 120),
    ('one hundred and fifty', 150),
    ('one hundred ans eighty five', 185),
    ('three hundred', 300)
]


lugs = [
    ('N/A', 'n/a'),
    ('three', 3),
    ('five', 5),
    ('thirty five by sixteen', str('35 x 16')),
    ('thirty five by ten', str('35 x 10')),
    ('thirty five by twelve', str('35 x 12')),
    ('seventy by ten', str('70 x 10')),
    ('seventy by twelve', str('70 x 12')),
    ('seventy by sixteen', str('70 x 16')),
    ('ninety five by ten', str('95 x 10')),
    ('ninety five by twelve', str('95 x 12')),
    ('ninety five by sixteen', str('95 x 16')),
    ('one hundred and twenty by ten', str('120 x 10')),
    ('one hundred and twenty by twelve', str('120 x 12')),
    ('one hundred and twenty by sixteen', str('120 x 16')),
    ('one hundred and fifty by ten', str('150 x 10')),
    ('one hundred and fifty by twelve', str('150 x 12')),
    ('one hundred and fifty by sixteen', str('150 x 16')),
    ('one hundred and eighty five by ten', str('185 x 10')),
    ('one hundred and eighty five by twelve', str('185 x 12')),
    ('one hundred and eighty five by sixteen', str('185 x 16')),
    ('two hundred and forty by ten ', str('240 x 10')),
    ('two hundred and forty by twelve ', str('240 x 12')),
    ('two hundred and forty by sixteen ', str('240 x 16')),
    ('three hundred by ten', str('300 x 10')),
    ('three hundred by twelve', str('300 x 12')),
    ('three hundred by sixteen', str('300 x 16'))



]


sizes_words = [
    ('NOT_APPLICABLE', 'n/a'),
    ('SMALL', 'small'), ('MEDIUM', 'medium'),
    ('LARGE', 'large '), ('EXTRA_LARGE', 'extra-large')
]

category_choices = [

    ('FERRULES', 'ferrules'),
    ('INSULATION TAPE', 'insulation-tape'),
    ('LUGS', 'lugs')

]


# class SizesFerrules(models.Model):
#     name = models.CharField(max_length=50, blank=True, null=True)

#     def __str__(self):
#         return self.name


class Category(models.Model):
    name = models.CharField(max_length=50, blank=True, null=True)

    def __str__(self):
        return self.name


class Stock(models.Model):
    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, default='1', blank=True)
    item_name = models.CharField(
        max_length=100, blank=True, null=True)
    received_stock = models.IntegerField(default='0', blank=True, null=True)
    total_stock_quantity = models.IntegerField(
        default='0', blank=True, null=True)
    issued_quantity = models.IntegerField(default='0', blank=True, null=True)
    issued_by = models.CharField(max_length=100, blank=True, null=True)
    issued_to = models.CharField(max_length=100, blank=True, null=True)
    created_by = models.CharField(max_length=100, blank=True, null=True)
    reorder_level = models.IntegerField(default='0', blank=True, null=True)
    last_updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    issue_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    returned_date = models.DateTimeField(auto_now_add=False, auto_now=True)
    stock_received_date = models.DateTimeField(
        auto_now_add=False, auto_now=True)
    # export_to_CSV = models.BooleanField(default=False)
    sizes_ferrules = models.CharField(max_length=100, choices=ferrules)
    sizes_lugs = models.CharField(max_length=100, choices=lugs)
    sizes_others = models.CharField(max_length=100, choices=sizes_words)
    returned = models.BooleanField(default=False)
    condition_returned = models.TextField(blank=True)

    def __str__(self):
        return self.item_name + ' ' + str(self.total_stock_quantity)
