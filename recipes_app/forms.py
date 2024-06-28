from django import forms
from .models import Recipe, RecipeCategory, RecipeCategoryRelationship


class RecipeForm(forms.ModelForm):
    category = forms.ModelChoiceField(queryset=RecipeCategory.objects.all(), required=True)

    class Meta:
        model = Recipe
        fields = ['name', 'description', 'cooking_steps', 'preparation_time', 'image', 'category']
        # name = models.CharField(max_length=200)
        # description = models.TextField()
        # cooking_steps = models.TextField()
        # preparation_time = models.PositiveIntegerField()
        # image = models.ImageField(upload_to='images/')
        # author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='recipes')
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'cooking_steps': forms.Textarea(attrs={'class': 'form-control'}),
            'preparation_time': forms.NumberInput(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
        }
        labels = {
            'name': 'Название',
            'description': 'Описание',
            'cooking_steps': 'Шаги приготовления',
            'preparation_time': 'Время приготовления (в минутах)',
            'image': 'Изображение',
            'category': 'Категория',
        }