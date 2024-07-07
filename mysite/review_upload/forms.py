# review_app/forms.py
# 리뷰를 입력하는 폼
# 파일 업로드와 관련된 기능으 FieldField를 사용하여 처리

from django import forms

class ReviewUploadForm(forms.Form):
    csv_file = forms.FileField()
