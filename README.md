# IT-Test---SCG-question1
ลง python3 และ pip3
set project
ติดตั้ง lib ที่เกี่ยวข้อง
1. pip3 install requirements.txt
เข้าไปในโฟเดอร์ postgresql
2. cd postgresql
รันคำสั่ง docker-compose เพื่อจำลอง database 
3. docker-compose -f docker-compose.local-database.yml up
ออกจากโฟเดอร์ postgresql
5. cd ../
รัน migrate เพื่อ สร้าง Table ใน database 
7. python3 manage.py migrate
Strat Project
8. python manage.py runserver

NOTE :
หน้าขายสินค้า
http://127.0.0.1:8000/
หน้าแสดงยอดการขาย
http://127.0.0.1:8000/dashboard/
