from django import forms
from base_app.models import Post, Comments

class PostForm(forms.ModelForm):

    class Meta():
        model = Post    #conectam tabela pe care vrem sa o folosim in forma aceasta
        fields = ('author','title','text') #acestea sunt campurile pe care vrem sa le modificam din baza de date
        # definim tipul de Widget (TextInput/TextArea) si atribuim proprietati Widget-urilor ca si la bootstrap
        # am atribuit campurilor title si author atribute de aspect din clase predefinite sau definite de noi in fisiere .css
        #toate aceste atribuiri se fac in cadrul "class Meta()"
        #clasele 'editable' si 'medium-editor-textarea' sunt clase predefinite
        #acesta este modul in care conectam anumite widget-uri la .css styling
        
        widgets = {
            'title':forms.TextInput(attrs={'class':'clasa_definita1'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea clasa_definita2'})  
        }
        
class CommentForm(forms.ModelForm):

    class Meta():
        model = Comments
        fields = ('author','text')
        widgets = {
            'author':forms.TextInput(attrs={'class':'clasa_definita1'}),
            'text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
        }

