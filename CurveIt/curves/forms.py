from django import forms
from curves.models import Course_Specific, User

# form to get a class and a grade from a user
class Course_SpecificForm(forms.ModelForm):
    curClasses = Course_Specific.objects.filter(semester="S2015")
    curClassesList = []
    for j in range (0, len(curClasses)):
        curClass = (curClasses[j].__unicode__(), curClasses[j].__unicode__())
        curClassesList.append(curClass)
    curClassesList.sort()
    pastSemClass = forms.ChoiceField(choices=curClassesList, help_text="Class")
    grade = forms.ChoiceField(choices=Course_Specific.CHOICES, help_text="Grade")
    # An inline class to provide additional information on the form.
    class Meta:
        # Provide an association between the ModelForm and a model
        model = Course_Specific
        fields = ('pastSemClass', 'grade')

class SearchForm(forms.Form):
    curClasses = Course_Specific.objects.filter(semester="S2015")
    curClassesList = []
    for j in range (0, len(curClasses)):
        curClass = (curClasses[j].__unicode__(), curClasses[j].__unicode__())
        curClassesList.append(curClass)
    curClassesList.sort()
    curProfs = []
    curDepts = []
    for class in Course_Specific.objects.all():
        if class.prof not in curProfs:
            curProfs.append(class.prof)
        if class.dept not in curDepts:
            curDepts.append(class.dept)
    curProfs.sort()
    curDepts.sort()
    allChoices = curClassesList + curProfs + curDepts
    search = forms.ChoiceField(choices = allChoices, help_text = "Class, Dept, or Professor")