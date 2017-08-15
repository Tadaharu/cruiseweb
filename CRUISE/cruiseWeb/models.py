from django.db import models

# Create your models here.
class Tweet(models.Model):
    tweetText = models.CharField(max_length = 264)
    createdDate = models.DateTimeField()
    completedCount = models.IntegerField(default=0)
    # completed = models.BooleanField(default = False)

    def __str__(self):
        dateString = "Created at:" + str(self.createdDate)
        tweetString = " Text: " + self.tweetText
        return  self.tweetText

class ObtainedDataNER(models.Model):
    tweet = models.ForeignKey(Tweet)
    tLocation = models.CharField(max_length= 300)
    tState = models.CharField(max_length = 200)

    def __str__(self):
        tLocationList = tLocation.split(',')
        tStateList = tState.split(',')
        totalList = tLocationList + tStateList
        return totalList

class ObtainedDataCA(models.Model):
    dataOrigin = models.ForeignKey(ObtainedDataNER)
    locationOne = models.CharField(max_length= 100)
    locationTwo = models.CharField(max_length= 100)
    state = models.CharField(max_length= 50)

    def __str__(self):
        trafficString = self.locationOne +','+self.locationTwo+" is "+self.state
        return trafficString
