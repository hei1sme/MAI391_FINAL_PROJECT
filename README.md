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
### Thư viện chính
- **Xử lý dữ liệu:** Pandas, NumPy
- **Học máy:** Scikit-learn
- **Trực quan hóa:** Matplotlib, Seaborn
- **Thống kê:** SciPy, Statsmodels

### Các công cụ cụ thể
- **Tiền xử lý dữ liệu:**
  - StandardScaler: Chuẩn hóa dữ liệu
  - LabelEncoder: Mã hóa biến phân loại
  - SMOTE: Cân bằng dữ liệu
  - Variance Inflation Factor: Kiểm tra đa cộng tuyến

- **Mô hình hóa:**
  - LogisticRegression: Mô hình chính
  - GridSearchCV: Tối ưu hóa siêu tham số
  - train_test_split: Chia tập dữ liệu

- **Đánh giá mô hình:**
  - classification_report: Báo cáo phân loại
  - confusion_matrix: Ma trận nhầm lẫn
  - accuracy_score: Độ chính xác
  - roc_curve, auc: Đường cong ROC

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

## 📄 License
Dự án này được phân phối dưới giấy phép MIT. Xem `LICENSE` để biết thêm thông tin.

## 👥 Tác giả
- Le Nguyen Gia Hung

## 🙏 Cảm ơn
- IBM HR Analytics Dataset
- Kaggle Community
- Scikit-learn Documentation