from django import forms
from django.forms import NumberInput,Textarea
from .models import Movie,Comment

# class DateInput(forms.DateInput):
#         input_type = 'date'

class MovieForm(forms.ModelForm):
    GENRE_CHOICES = [('코미디','코미디'),('공포','공포'),('로맨스','로맨스'),
    ('액션','액션'),('범죄','범죄'),('SF','SF'),('스랩스틱 코미디','스랩스틱 코미디')
    ,('전쟁','전쟁'),('스포츠','스포츠'),('뮤지컬','뮤지컬'),('멜로','멜로'),
    ('미스테리','미스테리'),('스릴러','스릴러'),('애니메이션','애니메이션'),]
    genre = forms.ChoiceField(choices=GENRE_CHOICES)

    audience = forms.IntegerField(min_value=0)
    
    score = forms.FloatField(
        max_value=5, min_value=0, 
        widget=NumberInput(
            attrs = {'step':'0.5'}
            ))

    release_date = forms.DateField()

    class Meta:
        model = Movie
        exclude = ('user',)
        # Widget = {'release_date' : DateInput()}


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        exclude = ('movie','user',)
        widgets = {
            'content': Textarea(attrs={'cols': 118, 'rows': 3}),
        }
