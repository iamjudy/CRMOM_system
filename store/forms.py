from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Supplier, Material, Product, Order, Dealer


class SupplierForm(forms.Form):
    class Meta:
        model = Supplier
        fields = ['s_ID', 's_name', 's_phone']
        widgets = {
          's_ID': forms.TextInput(attrs={'class': 'form-control', 'id': 's_ID'}),
          's_name': forms.TextInput(attrs={'class': 'form-control', 'id': 's_name'}),
          's_phone': forms.TextInput(attrs={'class': 'form-control', 'id': 's_phone'})
         }

class MaterialForm(forms.Form):
    class Meta:
        model = Material
        fields = ['m_ID', 'm_name', 'm_inventory', 'm_price']
        widgets = {
          'm_ID': forms.TextInput(attrs={'class': 'form-control', 'id': 'm_ID'}),
          'm_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'm_name'}),
          'm_inventory': forms.TextInput(attrs={'class': 'form-control', 'id': 'm_inventory'}),
          'm_price': forms.TextInput(attrs={'class': 'form-control', 'id': 'm_price'})
         }

class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['p_ID', 'p_name', 'p_price', 'p_inventory']
        widgets = {
            'p_ID': forms.TextInput(attrs={'class': 'form-control', 'id': 'p_ID'}),
            'p_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'p_name'}),
            'p_price': forms.TextInput(attrs={'class': 'form-control', 'id': 'p_price'}),
            'p_inventory': forms.TextInput(attrs={'class': 'form-control', 'id': 'p_inventory'})
            }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['o_ID', 'o_amount', 'o_price', 'o_date']

        widgets = {
            'o_ID': forms.TextInput(attrs={'class': 'form-control', 'id': 'o_ID'}),
            'o_amount': forms.TextInput(attrs={'class': 'form-control', 'id': 'o_amount'}),
            'o_price': forms.TextInput(attrs={'class': 'form-control', 'id': 'o_price'}),
            'o_date': forms.TextInput(attrs={'class': 'form-control', 'id': 'o_date'})
                }


class DealerForm(forms.ModelForm):
    class Meta:
        model = Dealer
        fields = ['d_ID', 'd_name', 'd_phone']

        widgets = {
            'd_ID': forms.TextInput(attrs={'class': 'form-control', 'id': 'd_ID'}),
            'd_name': forms.TextInput(attrs={'class': 'form-control', 'id': 'd_name'}),
            'd_phone': forms.TextInput(attrs={'class': 'form-control', 'id': 'd_phone'})
        }

class RawCategoryForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['p_ID']
        labels ={
            'p_ID': ('產品名稱')
        }
    康是美其他品牌購買量 = forms.DecimalField()
    寶雅其他品牌產品購買量 = forms.DecimalField()
    屈臣氏其他品牌產品購買量 = forms.DecimalField()

class RawOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class RawRateForm(forms.Form):
    d_choice = (
        ('康是美', '康是美'),
        ('寶雅', '寶雅'),
        ('屈臣氏', '屈臣氏'),
    )
    p_choice = (
        ('純色腮紅', '純色腮紅'),
        ('三色修容餅', '三色修容餅'),
        ('柔焦無瑕粉餅', '柔焦無瑕粉餅'),
        ('經典緞光唇膏', '經典緞光唇膏'),
        ('精萃水亮唇膏', '精萃水亮唇膏'),
    )
    經銷商名稱 = forms.ChoiceField(choices=d_choice)
    產品名稱 = forms.ChoiceField(choices=p_choice)
    前期顧客數量 = forms.DecimalField()
    本期留存顧客數量 = forms.DecimalField()

class RawCustomerForm(forms.Form):
    d_choice = (
        ('康是美', '康是美'),
        ('寶雅', '寶雅'),
        ('屈臣氏', '屈臣氏'),
    )
    p_choice = (
        ('純色腮紅', '純色腮紅'),
        ('三色修容餅', '三色修容餅'),
        ('柔焦無瑕粉餅', '柔焦無瑕粉餅'),
        ('經典緞光唇膏', '經典緞光唇膏'),
        ('精萃水亮唇膏', '精萃水亮唇膏'),
    )
    經銷商名稱 = forms.ChoiceField(choices=d_choice)
    產品名稱 = forms.ChoiceField(choices=p_choice)

class RawOrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'#['o_ID','d_name','p_name','o_amount','o_price','o_date']
        labels = {
            'o_ID': _('序號'),
            'o_amount': _('數量'),
            'o_price': _('價錢'),
            'o_profit': _('利潤'),
            'd_ID': _('經銷商名稱'),
            'p_ID': _('產品名稱'),
            'o_date': _('時間'),
        }
