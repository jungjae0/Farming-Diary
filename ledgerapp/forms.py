from django.forms import ModelForm, DateInput
from ledgerapp.models import Ledger
from django import forms


class LedgerForm(ModelForm):
    class Meta:
        model = Ledger
        fields = ["date","type","item","business","category","correspondent","amount","payment","description"]
        # datetime-local is a HTML5 input type
        widgets = {
            "date": DateInput(
                attrs={'type': 'datetime-local', 'class': 'form-control'},
                format='%Y-%m-%d'
            ),
            "type": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "수입·지출 선택"},
            ),
            "item": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "작물 선택"},
            ),
            "business": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "사업 유형 입력"},
            ),
            "category": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "종류입력"},
            ),
            "correspondent": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "거래처 입력"},
            ),
            "amount": forms.NumberInput(
                attrs={"class": "form-control", "placeholder": "금액 입력"},
            ),
            "payment": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "지불 유형 선택"},
            ),
            "description": forms.TextInput(
                attrs={"class": "form-control", "placeholder": "특이사항 입력"},
            ),
        }
        exclude = ["user"]

    def __init__(self, *args, **kwargs):
        super(LedgerForm, self).__init__(*args, **kwargs)
        # input_formats to parse HTML5 datetime-local input to datetime field
        self.fields["date"].input_formats = ("%Y-%m-%d",)
        # self.fields["end_time"].input_formats = ("%Y-%m-%dT%H:%M",)


# class AddMemberForm(forms.ModelForm):
#     class Meta:
#         model = EventMember
#         fields = ["user"]
