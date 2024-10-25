from django.db import models
import uuid



class OtherModel(models.Model):
    # name = models.CharField(max_length=100)
    name = "Rahin"


class MyModel(models.Model):
    name = models.CharField(max_length=20)
    roll = models.IntegerField(primary_key=True)
    father_name = models.TextField(default="Rahim")
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    char_field = models.CharField(max_length=255)
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    email_field = models.EmailField()
    file_field = models.FileField(upload_to='upload/')
    # file_path_field = models.FilePathField(path='upload/')  # Update this path
    float_field = models.FloatField()
    foreign_key = models.ForeignKey(OtherModel, on_delete=models.CASCADE)
    generic_ip_address_field = models.GenericIPAddressField()
    # image_field = models.ImageField(upload_to='upload/')
    integer_field = models.IntegerField()
    json_field = models.JSONField()
    # many_to_many_field = models.ManyToManyField(OtherModel)
    # one_to_one_field = models.OneToOneField(OtherModel, on_delete=models.CASCADE)
    positive_big_integer_field = models.PositiveBigIntegerField()
    positive_integer_field = models.PositiveIntegerField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    slug_field = models.SlugField()
    text_field = models.TextField()
    time_field = models.TimeField()
    uuid_field = models.UUIDField(default=uuid.uuid4, editable=False, unique=True)

    def __str__(self):
        return f"Roll : {self.roll}, Name: {self.name}"
