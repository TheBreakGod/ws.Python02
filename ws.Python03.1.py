def calculate_electricity_cost(power1, power2, power3, Rate):
    total_power = (power1 + power2 + power3 )*8

    total_units = total_power/1000

    total_cost = total_units * Rate
    return total_cost

power1 = int(input("กรุณาใส่กำลังไฟฟ้าของเครื่องปรับอากาศ 1 (เป็นจำนวนเต็ม) :"))
power2 = int(input("กรุณาใส่กำลังไฟฟ้าของเครื่องปรับอากาศ 2 (เป็นจำนวนเต็ม) :"))
power3 = int(input("กรุณาใส้กำลังไฟฟ้าของเครื่องปรับอากาศ 3 (เป็นจำนวนเต็ม) :"))
Rate = int(input("กรุณาใส่อัตราค่าไฟฟ้าหน่วย ()บาท/ยูนิต : "))

total_cost = calculate_electricity_cost(power1, power2, power3, Rate)*30
print("ค่าไฟทั้งหมดที่ต้องจ่ายเมื่อครบ 30 วัน คือ {:.2f} บาท".format (total_cost))
