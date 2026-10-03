ho_ten = input("Nhập họ tên:")
nam_sinh = int(input("Nhập năm sinh:"))
nganh_hoc = input("Nhập ngành học:")

tuoi = 2026 - nam_sinh

print("=== THÔNG TIN SINH VIÊN ===")
print("Sinh viên:", ho_ten)
print("Ngành học:", nganh_hoc)
print("Tuổi:", tuoi)



#BÀI 2

a = float(input("nhập chiều dài cạnh a:"))
b = float(input("nhập chiều dài cạnh b:"))

chu_vi = (a + b) * 2
dien_tich = a * b

print("Chu vi hình chữ nhật =", chu_vi)
print("Diện tích hình chữ nhật =", dien_tich)

#BÀI 3
C = float(input("Nhập C°:"))

F = (C * 1.8) + 32

print("Nhiệt độ F =", round(F, 1))


