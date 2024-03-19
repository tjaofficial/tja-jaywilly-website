from django.db import models

# Create your models here.

class shows(models.Model):
    name = models.CharField(max_length=50)
    local = models.BooleanField(default=False)
    date = models.DateField(auto_now=False, auto_now_add=False)
    time_start = models.TimeField(auto_now=False, auto_now_add=False)
    time_end = models.TimeField(auto_now=False, auto_now_add=False)
    address = models.CharField(max_length=50)
    city = models.CharField(max_length=25)
    state = models.CharField(max_length=2)
    zipcode = models.CharField(max_length=15)
    description = models.CharField(max_length=2000)
    venue = models.CharField(max_length=25)
    ticket_link = models.CharField(max_length=250)
    def __str__(self):
        return str(self.name)
    
# class artistInfo(models.Model):
#     name = models.CharField(max_length=50)
#     def __str__(self):
#         return str(self.name)
    
class videoLinks(models.Model):
    artistName = models.CharField(max_length=50)
    # artistChoice = models.ForeignKey(artistInfo, on_delete=models.CASCADE, blank=True, null=True)
    name = models.CharField(max_length=50)
    embedLink = models.CharField(max_length=500)
    def __str__(self):
        return str(self.artistChoice) + ' - ' + str(self.name)
    
# class socialLinks(models.Model):
#     artistChoice = models.ForeignKey(artistInfo, on_delete=models.CASCADE, blank=True, null=True)
#     instagram = models.CharField(max_length=300)
#     youtube = models.CharField(max_length=300)
#     spotify = models.CharField(max_length=300)
#     spotifyURI = models.CharField(max_length=300)
#     apple = models.CharField(max_length=300)
#     twitterX = models.CharField(max_length=300)
#     facebook = models.CharField(max_length=300)
#     tiktok = models.CharField(max_length=300)
#     snapchat = models.CharField(max_length=300)
#     soundcloud = models.CharField(max_length=300)
#     def __str__(self):
#         return str(self.artistChoice)