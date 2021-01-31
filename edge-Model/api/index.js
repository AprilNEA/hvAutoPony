/* 引入express框架 */
const express = require('express');
const app = express();
/* 引入cors */
const cors = require('cors');
app.use(cors());
/* 引入body-parser */
const bodyParser = require('body-parser');
app.use(bodyParser.json());
app.use(bodyParser.urlencoded({ extended: false }));
/* 监听端口 */
app.listen(8080, () => {
    console.log('——————————服务已启动——————————');
})
app.get('/', (req, res) => {
    res.send('<p style="color:red">服务已启动</p>');
})
app.get('/api/getUserList', (req, res) => {
    
})