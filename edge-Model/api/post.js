var http = require('http');
var querystring = require('querystring');
const tfjs =  require('@tensorflowjs/tfjs')
const tfjs =  require('@tensorflow/tfjs-automl')

var postHTML = 
  '<html><head><meta charset="utf-8"><title>AutoPony</title></head>' +
  '<body>' +
  '<form method="post">' +
  '<p>请提交小马图</p><input type="file" name="pony">' +
  '<input type="submit">' +
  '</form>' +
  '</body></html>';

async function autoPony(image) {
    const model = await tf.automl.loadImageClassification('../tf-js/20210130-1000/model.json');
    //const image = document.getElementById('daisy');
    const predictions = await model.classify(image);
    console.log(predictions);
    // Show the resulting object on the page.
    //const pre = document.createElement('pre');
    pre.textContent = JSON.stringify(predictions, null, 2);
    //document.body.append(pre);
    return pre
}

http.createServer(function (req, res) {
  var body = "";
  req.on('data', function (chunk) {
    body += chunk;
  });
  req.on('end', function () {
    // 解析参数
    body = querystring.parse(body);
    // 设置响应头部信息及编码
    res.writeHead(200, {'Content-Type': 'text/html; charset=utf8'});
    
    if(body.pony) { // 输出提交的数据
        answer = autoPony(body.pony)
        res.write("小马图：" + body.pony);
        res.write("小马图结果：" + answer);
        res.write("<br>");
        
    } else {  // 输出表单
        res.write(postHTML);
    }
    res.end();
  });
}).listen(3000);