# Dự án Quản lý Bệnh nhân
## Cấu trúc thư mục

```
Patient/
├── app/
│   ├── main.py              
│   ├── database.py         
│   ├── schemas.py           
│   ├── routers/             
│   └── templates/           
├── ansible/                 # Triển khai tự động
│   ├── inventory
│   └── playbook.yml
├── docker-compose.yml
├── dockerfile
├── requirements.txt
├── README.md
```

---

## Cài đặt Docker

### Trên **Windows**
1. Tải & cài Docker Desktop: https://www.docker.com/products/docker-desktop
2. Mở Docker Desktop và bật WSL integration nếu dùng WSL

### Trên **Ubuntu Linux**
```bash
sudo apt update
sudo apt install -y docker.io docker-compose
```

Kiểm tra cài thành công:
```bash
docker --version
docker compose version  # hoặc: docker-compose --version
```

---

##  Cách chạy dự án với Docker

###  Dùng cho cả Windows & Linux:

```bash
# Di chuyển vào thư mục dự án
cd Patient

# Chạy dự án (Windows PowerShell hoặc Ubuntu terminal)
docker compose up --build
```

Sau đó mở trình duyệt tại: http://localhost:8000

---

## Triển khai từ xa bằng Ansible (Linux server)

> Yêu cầu máy chủ có SSH và quyền `sudo`

### 1. Cài Ansible (chạy trên máy của bạn)

```bash
sudo apt update
sudo apt install -y ansible
```

### 2. Chạy playbook

```bash
cd Patient-management/ansible
ansible-playbook -i inventory playbook.yml
```

>  Đảm bảo `inventory` có đúng IP/host server bạn muốn triển khai.

---

## Kiểm thử thủ công không dùng Docker (tuỳ chọn)

```bash
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Mở: http://127.0.0.1:8000

---

## Định hướng phát triển
- [x] Tìm kiếm bệnh nhân
- [x] Giao diện Bootstrap
- [x] Sửa & xóa bệnh nhân
- [x] Docker hóa toàn bộ hệ thống
- [x] Triển khai tự động bằng Ansible
- [ ] Thống kê bệnh nhân theo tháng
- [ ] Phân quyền đăng nhập (admin / bác sĩ)
