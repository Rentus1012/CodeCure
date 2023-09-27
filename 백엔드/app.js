const express = require("express");
const app = express();
const port = 3000;

//서버 실행 완료시 터미널에서 이런 메세지가 나옴
app.listen(port,() => {
    console.log("listening on port");
});
//기본 경로이며, 가창 첫 메인이 되는 페이지임.

app.get('/',(req, res)=>
{
    res.send("Successed!");
});

//login 경로로 이동하면 login 이라는 텍스트가 뜸.

//res, req 함수를 만들어서 콜백함수를 만들수 있게 함.

app.get('/login',(req, res)=>
{
    res.send("login");
});


