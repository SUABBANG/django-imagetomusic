from django.http import HttpResponse
from django.shortcuts import render

from uploadapp.models import upload_csv_to_database

def upload_csv(request):
    if request.method == 'POST' and request.FILES['csv_file']:
        csv_file = request.FILES['csv_file']
        # 업로드된 CSV 파일을 임시로 저장
        with open('temp.csv', 'wb') as temp_csv:
            for chunk in csv_file.chunks():
                temp_csv.write(chunk)
        # 데이터베이스에 CSV 파일 내용 저장
        upload_csv_to_database('temp.csv')
        return HttpResponse("upload success")
    return HttpResponse("upload fail")

# 로직에 사용 함수들


