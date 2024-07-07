from django.shortcuts import render, redirect
from .forms import ReviewUploadForm
import pandas as pd
from .models import Review

def upload_review(request):
    if request.method == 'POST':
        form = ReviewUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = form.cleaned_data['csv_file']
            # CSV 파일을 DataFrame으로 읽기
            df = pd.read_csv(csv_file)

            # DataFrame 순회하며 리뷰 등록
            for index, row in df.iterrows():
                review = row['Review']  # CSV 파일에 따라 필드명 수정
                rating = row['Rating']  # CSV 파일에 따라 필드명 수정
                date = row['date']  # CSV 파일에 따라 필드명 수정
                sentiment = row['감정']  # CSV 파일에 따라 필드명 수정
                # 리뷰 모델 객체 생성
                Review.objects.create(review=review, rating=rating, date=date, sentiment=sentiment)

            return redirect('review_upload:upload_success')  # 네임스페이스를 사용하여 업로드 성공 페이지로 리다이렉트
    else:
        form = ReviewUploadForm()

    return render(request, 'upload_review.html', {'form': form})

def upload_success(request):
    return render(request, 'upload_success.html')