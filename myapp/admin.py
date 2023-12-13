from django.contrib import admin
from .models import HostelUser, Admin, Review, Campus, Hostel, Booking, Room, Facility, Payment, HostelFacility

# Register your models here.
admin.site.register(HostelUser)
admin.site.register(Admin)
admin.site.register(Review)
admin.site.register(Campus)
admin.site.register(Hostel)
admin.site.register(Booking)
admin.site.register(Room)
admin.site.register(Facility)
admin.site.register(Payment)
admin.site.register(HostelFacility)