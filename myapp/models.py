from django.db import models


class HostelUser(models.Model):
        UserID = models.AutoField(primary_key=True)
        Username = models.CharField(max_length=100)
        Email = models.EmailField(unique=True)
        Password = models.CharField(max_length=100)
        Usertype = models.CharField(max_length=100)
        last_login = models.DateTimeField(auto_now=True, null=True, blank=True)

        def __str__(self):
            return self.Username

class Admin(models.Model):
        AdminId = models.AutoField(primary_key=True)
        Username = models.CharField(max_length=100)
        Email = models.EmailField(unique=True)
        Password = models.CharField(max_length=100)

        def __str__(self):
            return self.Username


class Review(models.Model):
      ReviewID = models.AutoField(primary_key=True)
      UserID = models.ForeignKey(HostelUser, on_delete=models.CASCADE)
      HostelID = models.IntegerField()  # Assuming HostelID is an integer
      Rating = models.DecimalField(max_digits=3, decimal_places=2)
      Comment = models.TextField()

      def __str__(self):
          return f"Review #{self.ReviewID}"

class Campus(models.Model):
        CampusID = models.AutoField(primary_key=True)
        CampusName = models.CharField(max_length=100)
        Location = models.CharField(max_length=100)

        def __str__(self):
            return self.CampusName

class Facility(models.Model):
        FacilityID = models.AutoField(primary_key=True)
        FacilityName = models.CharField(max_length=100)
        Description = models.TextField()

        def __str__(self):
            return self.FacilityName

class Hostel(models.Model):
        HostelID = models.AutoField(primary_key=True)
        HostelName = models.CharField(max_length=30)
        Description = models.CharField(max_length=1000 , null=True)
        Location = models.CharField(max_length=1000)
        ContactNumber = models.CharField(max_length=11)
        Website = models.URLField()
        HostelImage = models.ImageField(upload_to='hostel_images/', null=True, blank=True)
        facilities = models.ManyToManyField(Facility, through='HostelFacility', related_name='hostels')


        def __str__(self):
            return self.HostelName


class Room(models.Model):
        RoomID = models.AutoField(primary_key=True)
        HostelID = models.ForeignKey(Hostel, on_delete=models.CASCADE , default=1)
        RoomType = models.CharField(max_length=50)
        RoomNumber = models.CharField(max_length=10)
        Availability = models.BooleanField(default=True)
        RoomImage = models.ImageField(upload_to='room_images/', null=True, blank=True)
        Price = models.DecimalField(max_digits=10, decimal_places=2)

        def __str__(self):
            return f"Room #{self.RoomID}"
class Booking(models.Model):
        BookingID = models.AutoField(primary_key=True)
        HostelUserID = models.ForeignKey(HostelUser, on_delete=models.CASCADE)
        RoomID = models.ForeignKey(Room, on_delete=models.CASCADE)
        BookingDate = models.DateField()
        TotalPrice = models.DecimalField(max_digits=10, decimal_places=2)

        def __str__(self):
            return f"Booking #{self.BookingID}"


class Payment(models.Model):
        PaymentID = models.AutoField(primary_key=True)
        PaymentMethod = models.CharField(max_length=50)
        PaymentAmount = models.DecimalField(max_digits=10, decimal_places=2)

        def __str__(self):
            return f"Payment #{self.PaymentID}"


class HostelFacility(models.Model):
        HostelFacilityID = models.AutoField(primary_key=True)
        HostelID = models.ForeignKey(Hostel, on_delete=models.CASCADE)
        FacilityID = models.ForeignKey(Facility, on_delete=models.CASCADE)

        def __str__(self):
            return f"Hostel Facility #{self.HostelFacilityID}"
