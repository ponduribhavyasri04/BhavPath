from flask import Flask

app = Flask(__name__)

@app.route('/')
def welcome():
    return """
<!DOCTYPE html>
<html>
<head>
<title>BhavPath</title>
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{height:100vh;width:100vw;overflow:hidden;background:#000;display:flex;align-items:center;justify-content:center;position:relative;font-family:sans-serif}
.g1{position:absolute;width:600px;height:600px;background:#6a00ff;filter:blur(100px);border-radius:50%;top:-150px;left:-150px;opacity:.8}
.g2{position:absolute;width:700px;height:700px;background:#ff006a;filter:blur(100px);border-radius:50%;bottom:-200px;right:-150px;opacity:.7}
.main{text-align:center;z-index:10;color:#fff}
.main h1{font-size:90px;font-weight:900;background:linear-gradient(90deg,#fff,#a78bfa);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.box{margin-top:30px;padding:25px 50px;border-radius:20px;background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.2);backdrop-filter:blur(20px);box-shadow:0 0 60px #ff006a66;display:inline-block}
.box h2{font-size:42px;background:linear-gradient(90deg,#fde047,#ff006a);-webkit-background-clip:text;-webkit-text-fill-color:transparent;font-weight:900}
.btn{margin-top:40px;padding:16px 55px;border:none;border-radius:50px;background:linear-gradient(90deg,#6a00ff,#ff006a);color:#fff;font-size:18px;font-weight:700;cursor:pointer}
</style>
</head>
<body>
<div class="g1"></div>
<div class="g2"></div>
<div class="main">
<h1>Welcome to BhavPath</h1>
<div class="box"><h2>What is Your Placement Story..??</h2></div><br>
<button class="btn">Start Your Journey →</button>
</div>
</body>
</html>
    """

if __name__ == '__main__':
    app.run(debug=True)
