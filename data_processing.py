import pandas as pd

# Đọc dữ liệu từ file CSV
df = pd.read_csv("StudentsPerformance.csv")

# Thông tin dữ liệu
print("Thông tin dữ liệu:")
print(df.info())

# Thống kê mô tả (chỉ áp dụng cho các cột số như điểm thi)
print("\nThống kê mô tả:")
print(df.describe())

# Lọc học sinh có điểm Toán > 80
print("\nHọc sinh có điểm Toán > 80:")
print(df[df["math score"] > 80])

# Tính điểm trung bình 3 môn cho mỗi học sinh
df["average score"] = df[["math score", "reading score", "writing score"]].mean(axis=1)
print("\n5 học sinh đầu tiên với điểm trung bình:")
print(df[["gender", "math score", "reading score", "writing score", "average score"]].head(5))

# Tính điểm trung bình theo giới tính
print("\nĐiểm trung bình theo giới tính:")
print(df.groupby("gender")[["math score", "reading score", "writing score", "average score"]].mean())
