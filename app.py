<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>BhavPath</title>
<link href="https://fonts.googleapis.com/css2?family=Outfit:wght@900&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{height:100vh;width:100vw;overflow:hidden;background:#000;display:flex;align-items:center;justify-content:center;position:relative;font-family:'Outfit',sans-serif}
.bg{position:absolute;border-radius:50%;filter:blur(90px);opacity:.8}
.b1{width:700px;height:700px;background:radial-gradient(#6a00ff,#6a00ff00);top:-200px;left:-200px;animation:m1 8s infinite alternate}
.b2{width:800px;height:800px;background:radial-gradient(#ff006a,#ff006a00);bottom:-250px;right:-200px;animation:m2 8s infinite alternate}
@keyframes m1{to{transform:translate(100px,100px)}}
@keyframes m2{to{transform:translate(-100px,-80px)}}
.main{text-align:center;z-index:10}
h1{font-size:110px;font-weight:900;letter-spacing:-3px;background:linear-gradient(180deg,#fff 30%,#a78bfa 100%);-webkit-background-clip:text;-webkit-text-fill-color:transparent;filter:drop-shadow(0 0 40px #a78bfa88)}
.story{margin-top:30px;padding:28px 65px;border-radius:24px;background:rgba(255,255,255,0.07);border:1px solid rgba(255,255,255,0.15);backdrop-filter:blur(20px);box-shadow:0 0 80px #f472b680, inset 0 0 20px #ffffff22;display:inline-block;animation:pulse 2s infinite alternate}
@keyframes pulse{from{box-shadow:0 0 40px #f472b660} to{box-shadow:0 0 90px #f472b6aa}}
.story h2{font-size:48px;font-weight:900;background:linear-gradient(90deg,#fde047,#fb923c,#f472b6);-webkit-background-clip:text;-webkit-text-fill-color:transparent}
.btn{margin-top:60px;padding:20px 70px;border:none;border-radius:100px;background:linear-gradient(90deg,#7c3aed,#ec4899);color:#fff;font-size:22px;font-weight:800;cursor:pointer;box-shadow:0 10px 40px #7c3aed88;transition:.3s}
.btn:hover{transform:scale(1.08) translateY(-3px);box-shadow:0 20px 50px #ec489988}
</style>
</head>
<body>
<div class="bg b1"></div>
<div class="bg b2"></div>
<div class="main">
<h1>Welcome to BhavPath</h1>
<div class="story"><h2>What is Your Placement Story..??</h2></div><br>
<button class="btn">Start Your Journey →</button>
</div>
</body>
</html>
