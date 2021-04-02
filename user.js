// ==UserScript==
// @name        [HV] AutoPony Pure
// @icon
// @run-at      document-end
// @compatible  Chrome/Chromium + Tampermonkey
// @compatible  Firefox + Greasemonkey
// @version     2.1.0
// @include     https://*.org/ponytest*
// @include     https://ponytest.pages.dev/
// @include     https://test.autopony.ltd/*
// @include     http*://hentaiverse.org/*
// @include     http://alt.hentaiverse.org/*
// @include     https://e-hentai.org/news.php*
// @exclude     http*://hentaiverse.org/pages/showequip.php?*
// @exclude     http://alt.hentaiverse.org/pages/showequip.php?*
// @exclude     http*://hentaiverse.org/equip/*
// @grant       GM_addStyle
// @grant       unsafeWindow
// @grant       GM_xmlhttpRequest
// @grant       GM_download
// @run-at      document-end
// @connect     localhost
// @connect     127.0.0.1
// @connect
//
// ==/UserScript==

const API_SERVER = 'http://127.0.0.1:5001';

// ====== DO NOT EDIT THIS LINE BELOW ===== //


const showLog = (log) => {
  let logEl = document.getElementById('pre');

  if (!logEl) {
    logEl = document.createElement('pre');
    logEl.id = 'pre';
    document.body.appendChild(logEl);
  }

  logEl.textContent = logEl.textContent === '' ? log
      : `${logEl.textContent}\n${log}`;
}

async function imgOnload(img) {
  showLog('Start getting pony pictures\'s Base64 URL');
  const canvas = document.createElement('canvas');
  canvas.id = 'canvas';
  canvas.width = img.offsetWidth;
  canvas.height = img.offsetHeight;
  document.body.appendChild(canvas);
  const ctx = canvas.getContext('2d');
  ctx.drawImage(img, 0, 0);
  const base64DataUrl = canvas.toDataURL('image/jpeg', 1.0);
  const base64Data = base64DataUrl.slice(23)
  console.log('The image data has been converted');
  showLog('The image data has been converted');
  showLog('Send a request to the API');

  const img_src = document.querySelector('#riddlebot > img').src;
  GM_xmlhttpRequest({
    method: "POST",
    url: `${API_SERVER}/autopony/`,
    headers: {
      "Content-Type": "application/json"
    },
    data: JSON.stringify({
      base64Data: base64Data,
      img_src: img_src
    }),
    onload: function (response) {
      //console.log(response.responseText);
      console.log(response);
      var back = JSON.parse(response.responseText);
      if (back.code == 0) {
        result = back.return
        showLog(`Pony：${result.pony}`);
        showLog(`Answer：${result.answer}`);
        setTimeout(() => {
          const inputEL = document.getElementById('riddleanswer');
          if (inputEL) {
            inputEL.value = result.answer;
            document.getElementById('riddleform')?.submit();
          }
        }, 100)
      } else if (back.code == 1) {
        showLog(`Abnormal Permissions, Please contact the server administrator`)
      }
    },
  });
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
        showLog('Pony image loading completed！');
        imgOnload(img);
      } else {
        console.log(img.complete);
        const interval = setInterval(() => {
          console.log(img.complete);
          if (typeof img.complete !== 'undefined' && img.complete) {
            clearInterval(interval);
            showLog('Pony image loading completed！');
            imgOnload(img);
          }
        }, 100);
      }
    }, 2000)
  }
})();
