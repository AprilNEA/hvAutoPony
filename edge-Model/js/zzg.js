// ==UserScript==
// @name         Horse_Xuan
// @description  Just collect pony pictures.
// @include      http*://hentaiverse.org/*
// @include      http://alt.hentaiverse.org/*
// @include      http*://ponytest.sukeycz.com/*
// @include      https://suka.js.org/ponytest/
// @compatible   Firefox + Greasemonkey
// @compatible   Chrome/Chromium + Tampermonkey
// @compatible   Android + Firefox + Usi/Tampermonkey
// @compatible   Other + Bookmarklet
// @grant        unsafeWindow
// @grant        GM_xmlhttpRequest
// @grant        GM_download
// @run-at       document-end
// @connect      localhost
// @connect      127.0.0.1
// ==/UserScript==
/* eslint-disable camelcase */

(function init () {
    if (gE('#riddlebot')) {
      autoanswer()
    }
  })()
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

  function autoanswer (){
    setTimeout(function(){console.log('等待');}, 10000);
    const img = document.querySelector('#riddlebot > img');
    const canvas = document.createElement('canvas');
    canvas.id = 'canvas';
    document.body.appendChild(canvas);
    const ctx = canvas.getContext('2d');
    ctx.drawImage(img, 0, 0);
    const base64DataUrl = canvas.toDataURL('image/jpeg', 1.0);
    const base64Data = base64DataUrl.slice(23)
    console.log(base64Data);
    
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
            //console.log(response.responseText);
            console.log(response);
        },

    });
  }