FROM python:3.10

# Tạo thư mục làm việc
WORKDIR /app

# Copy mã nguồn và cài đặt thư viện
COPY . .

RUN pip install --no-cache-dir -r requirements.txt

# Hiện thông báo
CMD echo "App running! Truy cập tại: http://localhost:8000" && \
    uvicorn app.main:app --host 0.0.0.0 --port 8000
