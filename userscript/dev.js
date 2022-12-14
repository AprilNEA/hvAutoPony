// ==UserScript==
// @name        AutoPony Pro
// @run-at      document-end
// @compatible  Chrome/Chromium + Tampermonkey
// @compatible  Firefox + Greasemonkey
// @version     1.0.1
// @include     https://*.org/ponytest*
// @include     http*://hentaiverse.org/*
// @include     http://alt.hentaiverse.org/*
// @exclude     http*://hentaiverse.org/pages/showequip.php?*
// @exclude     http://alt.hentaiverse.org/*pages/showequip.php?*
// @exclude     http*://hentaiverse.org/*equip/*
// @grant       GM_addStyle
// @grant       GM_xmlhttpRequest
// @grant       GM_download
// @grant       unsafeWindow
// @connect     localhost
// @connect     127.0.0.1

// ==/UserScript==

const API_SERVER = '127.0.0.1';

// ====== DO NOT EDIT THIS LINE BELOW ===== //

const showLog = (log) => {
  let logEl = document.getElementById('pre');

  if (!logEl) {
    logEl = document.createElement('pre');
    logEl.id = 'pre';
    document.body.appendChild(logEl);
  }

  logEl.textContent = logEl.textContent === '' ? log : `${logEl.textContent}\n${log}`;
}

async function imgOnload(img) {
  showLog('开始获取小马图片 Base64 URL');
  const canvas = document.createElement('canvas');
  canvas.id = 'canvas';
  canvas.width = img.offsetWidth;
  canvas.height = img.offsetHeight;
  document.body.appendChild(canvas);
  const ctx = canvas.getContext('2d');
  ctx.drawImage(img, 0, 0);

  const base64DataUrl = canvas.toDataURL('image/jpeg', 1.0);
  const base64Data = base64DataUrl.slice(23)
  //console.log(base64Data);
  console.log('图片数据已经转换完成');

  showLog('小马图片 Base64 URL 获取成功！');
  showLog('向 API 发送请求');

  GM_xmlhttpRequest({
    method: "POST",
    url: `http://${API_SERVER}/pony/api/post/${Uid}/`,
    headers: {
        "Content-Type": "application/json"
        },
    data: JSON.stringify({
        base64: base64Data,
        pass: Password
      }),
    onload: function(response){
        //console.log(response.responseText);
        console.log(response);
        var back = JSON.parse(response.responseText);
        back = back.return[0]
        const rp = back.answer
        //console.log(back);
        console.log(rp);
        if (rp=="A"||rp=="B"||rp=="C"){
            gE('#riddleanswer').value=rp
            gE('#riddleanswer+img').click()
        }else {
            showLog('服务器出错');
        }
        showLog(`您的小马总数：${back.timesall}`);
        showLog(`本次已用小马：${back.time}`)
        showLog(`您的小马剩余：${back.timesleft}`)
        showLog(`判断小马为：${back.pony}`);
        showLog(`判断小马用时：${back.time_pony}`);
        //showLog(`服务器用时：${back.time}`);
        showLog(`判断答案为：${back.answer}`);
    },
  });
}

function gE (ele, mode, parent) {
    if (typeof ele === 'object') {
      return ele
    } else if (mode === undefined && parent === undefined) {
      return (isNaN(ele * 1)) ? document.querySelector(ele) : document.getElementById(ele)
    } else if (mode === 'all') {
      return (parent === undefined) ? document.querySelectorAll(ele) : parent.querySelectorAll(ele)
    } else if (typeof mode === 'object' && parent === undefined) {
      return mode.querySelector(ele)
    }
  }
(async () => {
  if (document.getElementById('riddlecounter')) {
    GM_addStyle(`
    #pre {
      position: fixed;
      top: 0;
      width: 255px;
      text-align: left;
      padding: 10px;
      background: rgba(1,1,1,0.08);
    }
    #canvas {
      display: none;
    }
    `);

    const img = document.querySelector('#riddlebot > img');

    setTimeout(() => {
      if (typeof img.complete !== 'undefined' && img.complete) {
        showLog('检测到小马图片加载完成！');
        imgOnload(img);
      } else {
        console.log(img.complete);
        const interval = setInterval(() => {
          console.log(img.complete);
          if (typeof img.complete !== 'undefined' && img.complete) {
            clearInterval(interval);
            showLog('检测到小马图片加载完成！');
            imgOnload(img);
          }
        }, 100);
      }
    }, 500)
  }
})();
