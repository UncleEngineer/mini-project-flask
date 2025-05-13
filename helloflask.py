from flask import Flask

app = Flask(__name__)

html = '''
<!DOCTYPE html>
<html lang="en">
<head>
  <title>Home - Loongshop</title>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>
</head>
<body>

<div class="container-fluid p-5 bg-primary text-white text-center">
  <h1>Uncle Shop</h1>
  <p>ร้านลุงวิศวกร สอนคำนวณ ขายทุกอย่างที่ลุงมี</p> 
</div>
  
<div class="container mt-5">
  <div class="row">
    <div class="col-sm-4">
      <h3>มอเตอร์ไซค์</h3>
      <p>มอเตอร์ไซค์ลุง นำเข้าจากต่างประเทศ ใช้งานค่อนข้างดี</p>
      <p>มีรถมอเตอร์ไซค์ไฟฟ้าด้วย</p>
    </div>
    <div class="col-sm-4">
      <h3>รถยนต์</h3>
      <p>รถยนต์ลุง นำเข้าจากต่างประเทศ ใช้งานค่อนข้างดี</p>
      <p>มีรถยนต์ไฟฟ้าเทสล่าขายด้วย นำเข้าจาก USA โดยตรง</p>
    </div>
    <div class="col-sm-4">
      <h3>รถไถ</h3>        
      <p>ลุงขายรถไถด้วย สามารถนำไปใช้ในการเกษตรได้ดี</p>
      <p>รถไถลุงส่วนใหญ่นำเข้าจากญี่ปุ่น ใช้งานดี</p>
    </div>
  </div>
</div>

</body>
</html>

'''

@app.route('/')
def home():
    return html

if __name__ == '__main__':
    app.run(debug=True)