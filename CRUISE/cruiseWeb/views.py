from django.shortcuts import render
from cruiseWeb import forms
from cruiseWeb.models import Tweet, ObtainedDataNER
from django.forms.formsets import formset_factory
from django.db.models import Avg, Min, Max
# Create your views here.
def index(request):
    return render(request, 'cruiseWeb/index.html')

def aboutUs(request):
    return render(request, 'cruiseWeb/aboutUs.html')

def projectDescr(request):
    return render(request, 'cruiseWeb/projdesc.html')

def cruiseDemo(request):

    return render(request, 'cruiseWeb/demo.html')

def technicalElement(request):
    return render(request, 'cruiseWeb/techManual.html')

def gtSurvey(request):
    allTweets =Tweet.objects.all()
    minDict = allTweets.aggregate(Min('completedCount'))
    minVal = minDict['completedCount__min']
    print("LOWEST UNFINISHED :"+ str(minVal))
    tweet_items = Tweet.objects.filter(completedCount=minVal)[:10]
    # print(tweet_items)
    # for ea in tweet_items:
    #     print(ea.id)
    qForms = formset_factory(forms.NewNerForm, extra=len(tweet_items))

    if request.method == 'POST':
        qForms = qForms(request.POST)
        if qForms.is_valid():

            for num, form in enumerate(qForms):
                # print(num)
                if form.is_valid():
                    obj = form.save(commit = False)
                    # print(tweet_items[num])
                    # print("ID: "+ str(tweet_items[num].tweetText))
                    # print("ID: "+ str(tweet_items[num].id))
                    obj.tweet = tweet_items[num]
                    obj.save()

                    temp = tweet_items[num]
                    temp.completedCount = temp.completedCount+1
                    # print(temp.completed)
                    temp.save()

                    # tweet_items = Tweet.objects.filter(completed=False)[:3]
                    # qForms = formset_factory(forms.NewNerForm, extra=3)
            return thankyou(request)
        # do nth

    return render(request, 'cruiseWeb/gtSurvey.html', {'formset':qForms(), 'tweetset':tweet_items})
    # tweet = Tweet.objects.filter(completed=False)[:1]
    # tweet = tweet[0]
    #
    # # form = forms.NewNerForm(tweet)
    # form = forms.NewNerForm()
    # dataGroup = {'text' : tweet.tweetText, 'form':form}
    #
    # if request.method =="POST":
    #     form = forms.NewNerForm(request.POST)
    #     if form.is_valid():
    #         obj = form.save(commit = False)
    #         obj.tweet = tweet
    #         obj.save()
    #         tweet.completed = True
    #         tweet.save()
    #         # form.save(commit = True)
    #         print("INPUT GET!")
    #         print("LOCATION: "+ form.cleaned_data['tLocation'])
    #         print("STATE: "+ form.cleaned_data['tState'])
    #
    #         tweet = Tweet.objects.filter(completed=False)[:1]
    #         tweet = tweet[0]
    #         form = forms.NewNerForm()
    #         dataGroup = {'text' : tweet.tweetText, 'form':form}
    #
    #     else:
    #         print("UH OH! Something is wrong!")
    #
    # return render(request, 'cruiseWeb/gtSurvey.html', context = dataGroup)

def thankyou(request):

    return render(request, 'cruiseWeb/thankyou.html')
