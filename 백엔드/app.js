const express = require('express');
const app = express();
const port = 3000; //���� ��Ʈ ��ȣ

app.get('/', (req, res) =>{
    res.send('Hello world!');
});


//���� ���� �Լ�

app.listen(port, () => {
    console.log('������ ����˴ϴ�. http://localhost:{port}');
});


