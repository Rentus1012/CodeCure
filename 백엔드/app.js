const express = require("express");
const app = express();
const port = 3000;

//���� ���� �Ϸ�� �͹̳ο��� �̷� �޼����� ����
app.listen(port,() => {
    console.log("listening on port");
});
//�⺻ ����̸�, ��â ù ������ �Ǵ� ��������.

app.get('/',(req, res)=>
{
    res.send("Successed!");
});

//login ��η� �̵��ϸ� login �̶�� �ؽ�Ʈ�� ��.

//res, req �Լ��� ���� �ݹ��Լ��� ����� �ְ� ��.

app.get('/login',(req, res)=>
{
    res.send("login");
});


