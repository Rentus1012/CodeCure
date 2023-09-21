const express = require('express');
const app = express();
const port = 3000; //서버 포트 번호

app.get('/', (req, res) =>{
    res.send('Hello world!');
});


//서버 실행 함수

app.listen(port, () => {
    console.log('서버가 실행됩니다. http://localhost:{port}');
});


