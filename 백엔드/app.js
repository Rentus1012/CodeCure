const express = require("express");
const app = express();
const port = 3000;


app.listen(port,() => {
    console.log("listening on port");
});

app.get('/',(req, res)=>
{
    res.send("Successed!");
});


app.get('/login',(req, res)=>
{
    res.send("login Screen");
});