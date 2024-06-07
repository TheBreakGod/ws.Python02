x = int(input("กรุณาใส่ค่ากำลังไฟฟ้าของเครื่องปรับอากาศเครื่องที่ 1 (วัตต์): "))
y = int(input("กรุณาใส่ค่ากำลังไฟฟ้าของเครื่องปรับอากาศเครื่องที่ 2 (วัตต์): "))
z = int(input("กรุณาใส่ค่ากำลังไฟฟ้าของเครื่องปรับอากาศเครื่องที่ 3 (วัตต์): "))
rate_per_unit = float(input("กรุณาใส่อัตราค่าไฟฟ้าหน่วย (บาท/ยูนิต): "))
hours_per_day = 8
days_in_month = 30

total_energy_x = x * hours_per_day * days_in_month
total_energy_y = y * hours_per_day * days_in_month
total_energy_z = z * hours_per_day * days_in_month

total_energy = total_energy_x + total_energy_y + total_energy_z
total_units = total_energy / 1000
total_cost = total_units * rate_per_unit
print(f"ค่าไฟฟ้าทั้งหมดที่ต้องจ่ายเมื่อครบ 30 วัน {total_cost:.2f} บาท")
