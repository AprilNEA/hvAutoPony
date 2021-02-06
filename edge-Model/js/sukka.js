// ==UserScript==
// @name        [HV] Fuck Pony
// @description Why join the navy if you can be a pirate?
// @icon        https://cdn.jsdelivr.net/npm/hvautoattack@0.0.0/assets/Setting.png
// @run-at      document-end
// @compatible  Chrome/Chromium + Tampermonkey
// @compatible  Firefox + Greasemonkey
// @version     0.0.0
// @include     https://*.org/ponytest*
// @include     http*://hentaiverse.org/*
// @include     http://alt.hentaiverse.org/*
// @include     https://e-hentai.org/news.php*
// @exclude     http*://hentaiverse.org/pages/showequip.php?*
// @exclude     http://alt.hentaiverse.org/pages/showequip.php?*
// @exclude     http*://hentaiverse.org/equip/*
// @grant       GM_addStyle
// ==/UserScript==

const API_SERVER = '';

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

  showLog('小马图片 Base64 URL 获取成功！');
  showLog('向 API 发送请求');
  
  GM_xmlhttpRequest({
    method: "POST",
    url: "http://127.0.0.1:5000/api",
    headers: {
        "Content-Type": "application/json"
        },
    data: JSON.stringify({
        base64: base64Data
      }),
    onload: function(response){
        var rp=response.responseText
          if (rp=="A"||rp=="B"||rp=="C"){
              gE('#riddleanswer').value=rp
              gE('#riddleanswer+img').click()
          }
        //console.log("请求成功");
        resp ={
          "answer" : response.responseText,
          "code" : '0'
        } 
        //console.log(response.responseText);
        console.log(response);
    },
  });

  if (resp.code === 0 && resp.answer) {
    showLog(`获取到答案为：${resp.answer}`);
    showLog(`服务器用时：${resp.time}`);

    setTimeout(() => {
      const inputEl = document.getElementById('riddleanswer');
      if (inputEl) {
        inputEl.value = resp.answer;
        document.querySelector('#riddleanswer+img')?.click();
      }
    }, 100);
  } else {
    showLog('服务器出错！');
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
    const newImg = document.createElement('img')
    newImg.src =  img.src
    newImg.onload = imgOnload(newImg);
    document.body.appendChild(newImg);

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
    }, 5000)
  }
})();
