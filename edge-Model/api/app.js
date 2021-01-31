//var express = require("express");
//var app = express();
var http = require('http');
const cors = require('cors');
const tfjs =  require('@tensorflowjs/tfjs')
const tfjs =  require('@tensorflow/tfjs-automl')


http.createServer(function (request, response) {

    // 发送 HTTP 头部 
    // HTTP 状态值: 200 : OK
    // 内容类型: text/plain
    response.writeHead(200, {'Content-Type': 'text/plain'});
    
    // 发送响应数据 "Hello World"
    response.end('Hello World\n');
    run();
}).listen(8888);

// 终端打印如下信息
console.log('Server running at http://127.0.0.1:8888/');

async function run() {
    const model = await tf.automl.loadImageClassification('../tf-js/20210130-1000/model.json');
    const image = document.getElementById('daisy');
    const predictions = await model.classify(image);
    console.log(predictions);
    // Show the resulting object on the page.
    const pre = document.createElement('pre');
    pre.textContent = JSON.stringify(predictions, null, 2);
    document.body.append(pre);
}

