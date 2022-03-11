from turtle import title
from django import forms 
from .models import Article

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article 
        fields = ['title', 'content']
    
    def clean(self):
        cleaned_data = self.cleaned_data
        title = cleaned_data.get('title')

        if Article.objects.filter(title__icontains = title):
            self.add_error('title', f"Title {title} is already taken!")

        return cleaned_data


class ArticleFormOld(forms.Form):
    title = forms.CharField()
    content = forms.CharField()

    # def clean_title(self):
    #     cleaned_data = self.cleaned_data
    #     print("cleaned data: ", cleaned_data)
    #     title = cleaned_data.get('title')
    #     if title.lower().strip() == "the office trailer":
    #         raise forms.ValidationError("This title is taken.")
    #     print("title: ", title)
    #     return title 

    # def clean(self):
    #     cleaned_data = self.cleaned_data
    #     print("cleaned data", cleaned_data)
    #     title = cleaned_data.get('title')
    #     content = cleaned_data.get("content")
    #     if title.lower().strip() == "the office trailer":
    #         self.add_error('title', "This title is taken")
    #         # raise forms.ValidationError("This title is taken.")
    #     if "office" in content or "office" in title.lower():
    #         self.add_error('content', "Office cannot be in content")
    #         raise forms.ValidationError("Office is not allowed")
    #     return cleaned_data

    def clean(self):
        cleaned_data = self.cleaned_data
        titles = Article.objects.all().values('title')
        # print(titles)
        import operator
        get_value = operator.itemgetter('title')
        lst = list(map(get_value, titles))
        # print(lst)
        title = cleaned_data.get('title')
        content = cleaned_data.get('content')
        if title.strip() in lst:
            self.add_error('title', 'title is already taken')
        if 'cobra' in content:
            self.add_error('content', 'You cannot use the word cobra in content')
            raise forms.ValidationError('Cobra prohibited')
        return cleaned_data