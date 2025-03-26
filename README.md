# Dự đoán Nghỉ việc Nhân viên - IBM HR Analytics

## 📝 Mô tả
Dự án này nhằm xây dựng một mô hình Hồi quy Logistic để dự đoán khả năng nghỉ việc của nhân viên dựa trên các đặc điểm nhân khẩu học, tài chính và công việc. Mô hình sẽ giúp doanh nghiệp xác định các yếu tố quan trọng ảnh hưởng đến sự nghỉ việc và đưa ra các chiến lược giữ chân nhân sự hiệu quả.

## 🎯 Mục tiêu
- Phát triển mô hình dự báo chính xác khả năng nghỉ việc của nhân viên
- Hỗ trợ doanh nghiệp trong việc đưa ra các chiến lược giữ chân nhân sự
- So sánh hiệu suất giữa mô hình cơ bản và mô hình được tối ưu hóa

## 📊 Dữ liệu
- **Nguồn:** [IBM HR Analytics Employee Attrition & Performance](https://www.kaggle.com/datasets/pavansubhasht/ibm-hr-analytics-attrition-dataset/data)
- **Kích thước:** 1,471 mẫu
- **Số đặc trưng:** 35 biến đầu vào

## 🛠️ Công nghệ sử dụng
- Python 3.x
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn

## 📋 Cấu trúc dự án
```
├── data/                   # Thư mục chứa dữ liệu
│   └── HR-Employee-Attrition.csv
├── notebook/              # Jupyter notebooks
│   └── MAI391_SE194127_final_project.ipynb
├── LICENSE                # Giấy phép MIT
└── README.md             # Tài liệu hướng dẫn
```

## 🚀 Cách sử dụng
1. Clone repository:
```bash
git clone [repository-url]
```

2. Cài đặt các thư viện cần thiết:
```bash
pip install -r requirements.txt
```

3. Mở và chạy notebook:
   - Mở file `notebook/MAI391_SE194127_final_project.ipynb`
   - Chạy các cell theo thứ tự

## 📈 Kết quả
### So sánh hiệu suất mô hình
| Chỉ số | Mô hình cơ bản | Mô hình GridSearchCV |
|--------|----------------|---------------------|
| Accuracy | 72.11% | 68.71% |
| Precision | 26% | 24% |
| Recall | 59% | 64% |
| F1-Score | 36% | 35% |

### Đặc trưng quan trọng nhất
1. OverTime (0.903)
2. YearsAtCompany (0.814)
3. TotalWorkingYears (0.776)
4. YearsInCurrentRole (0.773)
5. YearsWithCurrManager (0.520)

## 🤝 Đóng góp
Mọi đóng góp đều được chào đón! Vui lòng:
1. Fork dự án
2. Tạo branch mới (`git checkout -b feature/AmazingFeature`)
3. Commit thay đổi (`git commit -m 'Add some AmazingFeature'`)
4. Push lên branch (`git push origin feature/AmazingFeature`)
5. Mở Pull Request

## 📄 License
Dự án này được phân phối dưới giấy phép MIT. Xem `LICENSE` để biết thêm thông tin.

## 👥 Tác giả
- Le Nguyen Gia Hung

## 🙏 Cảm ơn
- IBM HR Analytics Dataset
- Kaggle Community
- Scikit-learn Documentation
