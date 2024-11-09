
from django import forms
from .models import Phim, NguoiDung, TheLoai, DinhDangPhim, XuatChieu, RapChieu, Ve, GheNgoi, Combo, BinhLuan, Contact
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PhimForm(forms.ModelForm):
    class Meta:
        model = Phim
        fields = ['ten_phim', 'the_loai', 'dao_dien', 'dien_vien', 'thoi_luong', 'tom_tat', 'thumbnail', 'do_tuoi']

class NguoiDungForm(forms.ModelForm):
    class Meta:
        model = NguoiDung
        fields = ['username', 'email', 'sdt', 'password', 'gioi_tinh', 'ngay_sinh']
        widgets = {
            'password': forms.PasswordInput(),  # Hiển thị trường mật khẩu
            'ngay_sinh': forms.DateInput(attrs={'type': 'date', 'placeholder': 'dd/mm/yyyy'})  # Định dạng ngày sinh
        }

class UserForm(UserCreationForm):
    password = forms.CharField(widget=forms.PasswordInput)
    class Meta:
        model = User
        fields = ['username', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }
        
class TheLoaiForm(forms.ModelForm):
    class Meta:
        model = TheLoai
        fields = ['ten_the_loai']
        
class DinhDangPhimForm(forms.ModelForm):
    class Meta:
        model = DinhDangPhim
        fields = ['ten_dinh_dang']
        
        
class RapChieuForm(forms.ModelForm):
    class Meta:
        model = RapChieu
        fields = ['ten_rap', 'dia_chi', 'so_dien_thoai', 'email']
        
        
        
class XuatChieuForm(forms.ModelForm):
    class Meta:
        model = XuatChieu
        fields = ['phim', 'thoi_gian_chieu', 'rap_chieu', 'dinh_dang_phim']
        widgets = {
            'thoi_gian_chieu': forms.DateTimeInput(attrs={'type': 'datetime-local'}),  # Định dạng cho thời gian chiếu
        }



from django import forms
from .models import Ve

class VeForm(forms.ModelForm):
    class Meta:
        model = Ve
        fields = ['phim', 'thoi_gian_chieu', 'rap', 'ghe_ngoi', 'ma_qr_ve', 'user_mua_ve', 'combo','link_face']
        widgets = {
            'phim': forms.Select(),
            'thoi_gian_chieu': forms.Select(),
            'rap': forms.Select(),
            'ghe_ngoi': forms.Select(),
            'combo' : forms.Select(),
            'ma_qr_ve': forms.TextInput(),
            'user_mua_ve': forms.Select(),
        }

class ComboForm(forms.ModelForm):
    class Meta:
        model = Combo
        fields = ['ten_combo', 'gia_combo']
        widgets = {
            'gia_combo': forms.NumberInput(attrs={'step': '0.01'}),
        }
        
class GheNgoiForm(forms.ModelForm):
    class Meta:
        model = GheNgoi
        fields = ['ten_ghe', 'rap_chieu', 'loai_ghe', 'gia_ve']


class BinhLuanForm(forms.ModelForm):
    class Meta:
        model = BinhLuan
        fields = ['phim', 'user_binh_luan', 'rating', 'noi_dung']
        widgets = {
            'rating': forms.NumberInput(attrs={'min': 1, 'max': 5}),
            'noi_dung': forms.Textarea(attrs={'rows': 3}),
        }



# forms.py
from django import forms
from .models import XuatChieu

class XuatChieuFormTuDong(forms.Form):
    phim = forms.ModelChoiceField(queryset=Phim.objects.all(), label="Phim")
    rap_chieu = forms.ModelChoiceField(queryset=RapChieu.objects.all(), label="Rạp chiếu")
    dinh_dang_phim = forms.ModelChoiceField(queryset=DinhDangPhim.objects.all(), label="Định dạng phim")
    ngay_chieu = forms.DateField(label="Ngày chiếu", widget=forms.DateInput(attrs={'type': 'date'}))
    
class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'email', 'subject', 'message']
        