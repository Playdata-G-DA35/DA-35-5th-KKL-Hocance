from django.shortcuts import render
import matplotlib.pyplot as plt
from io import BytesIO
import base64

import pandas as pd
from datetime import datetime
from .forms import DateRangeForm

def rating_chart(request):
    if request.method == 'POST':
        form = DateRangeForm(request.POST)
        if form.is_valid():
            start_date = form.cleaned_data['start_date']
            end_date = form.cleaned_data['end_date']
        else:
            # 폼이 유효하지 않으면 기본 날짜 범위 설정
            start_date = datetime(2024, 1, 1)
            end_date = datetime(2024, 6, 30)
    else:
        form = DateRangeForm()
        start_date = datetime(2024, 1, 1)
        end_date = datetime(2024, 6, 30)

    # new_data.csv 파일에서 데이터 읽어오기
    try:
        review_df = pd.read_csv("dataset/new_data.csv")
    except FileNotFoundError:
        review_df = pd.DataFrame()  # 파일이 없는 경우 빈 데이터프레임 생성

    # 날짜별 평균 평점 계산
    if not review_df.empty:
        review_df['date'] = pd.to_datetime(review_df['date'])

        # start_date와 end_date를 datetime으로 변환
        start_date = pd.to_datetime(start_date)
        end_date = pd.to_datetime(end_date)

        mask = (review_df['date'] >= start_date) & (review_df['date'] <= end_date)
        filtered_df = review_df.loc[mask]
        daily_avg_rating = filtered_df.groupby('date')['Rating'].mean().reset_index()

        # 일자별 리뷰 평균 꺽은선 그래프화
        plt.figure(figsize=(14, 7))
        plt.plot(daily_avg_rating['date'], daily_avg_rating['Rating'], marker='o', linestyle='-', color='b')
        plt.title('Daily Average Hotel Ratings')
        plt.xlabel('Date')
        plt.ylabel('Average Rating')
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # 그래프 이미지를 BytesIO에 저장하여 base64로 인코딩
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        avg_rating_graph = base64.b64encode(image_png).decode('utf-8')
        plt.close()

        # 긍정 및 부정 리뷰 수 계산
        daily_sentiment = filtered_df.groupby(['date', '감정']).size().unstack(fill_value=0).reset_index()
        daily_sentiment = daily_sentiment.fillna(0)

        # 긍정 및 부정 리뷰 수를 스택된 막대 그래프로 그리기
        plt.figure(figsize=(14, 7))
        plt.bar(daily_sentiment['date'], daily_sentiment['Positive'], label='Positive Reviews', color='g')
        plt.bar(daily_sentiment['date'], daily_sentiment['Negative'], bottom=daily_sentiment['Positive'], label='Negative Reviews', color='r')

        plt.title('Daily Positive and Negative Hotel Reviews Count')
        plt.xlabel('Date')
        plt.ylabel('Number of Reviews')
        plt.legend()
        plt.grid(True)
        plt.xticks(rotation=45)
        plt.tight_layout()

        # 그래프 이미지를 BytesIO에 저장하여 base64로 인코딩
        buffer = BytesIO()
        plt.savefig(buffer, format='png')
        buffer.seek(0)
        image_png = buffer.getvalue()
        buffer.close()

        review_count_graph = base64.b64encode(image_png).decode('utf-8')
        plt.close()

    else:
        avg_rating_graph = None
        review_count_graph = None

    return render(request, 'chart.html', {
        'form': form,
        'avg_rating_graph': avg_rating_graph,
        'review_count_graph': review_count_graph
    })
