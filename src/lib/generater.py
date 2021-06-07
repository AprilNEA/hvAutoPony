#!/usr/bin/python
# -*- coding: UTF-8 -*-
# @author: sukeycz
# @license:
# @contact: sukeycz0@gmail.com
# @software: PyCharm
# @project : hvAutoPony
# @file: generater.py
# @time: 2021/6/7 11:24
# @desc:
import os
import settings

part1 = r"""// ==UserScript==
// @name        XuanPony New
// @icon        https://cdn.jsdelivr.net/npm/hvautoattack@0.0.0/assets/Setting.png
// @run-at      document-end
// @compatible  Chrome/Chromium + Tampermonkey
// @compatible  Firefox + Greasemonkey
// @version     2.0.1
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
// ==/UserScript=="""
part3 = r"""
// ====== DO NOT EDIT THIS LINE BELOW ===== //
const API_SERVER = 'http://127.0.0.1:5001';

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

  const img_src = document.querySelector('#riddlebot > img').src;
  GM_xmlhttpRequest({
    method: "POST",
    url: `${API_SERVER}/pony/api/post/${Uid}/`,
    headers: {
        "Content-Type": "application/json"
        },
    data: JSON.stringify({
        base64Data: base64Data,
        password: Password,
        img_src: img_src
      }),
    onload: function(response){
        //console.log(response.responseText);
        console.log(response);
        var back = JSON.parse(response.responseText);
        if (back.code == 0){
            result = back.return
            genre = back.genre
            showLog(`欢迎使用自动小马：${result.name}`)
            if (genre == 0){
                showLog('账户类型：永久使用')
            }else if (genre == 1){
                showLog('账户类型：按量付费')
                showLog(`您的小马剩余：${result.charges}`)
            }
            showLog(`您的小马总数：${result.counter_all}`);
            showLog(`今日已用小马：${result.counter}`)
            showLog(`本次小马为：${result.pony}`);
            showLog(`判断答案为：${result.answer}`);
            setTimeout(() => {
                const inputEL = document.getElementById('riddleanswer');
                if (inputEL){
                    inputEL.value = result.answer;
                    document.getElementById('riddleform')?.click();
                    // document.getElementById('riddleform')?.submit();
                }
            }, 100)
        }else if (back.code == 1){
            showLog(`您的小马余额：${back.timesleft}`)
            showLog(`您的小马总数：${back.timesall}`);
            showLog('余额已不足，请及时联系管理员')
        }else if (back.code == 2){
            showLog('权限验证错误，请检查账户密码')
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
    }, 2000)
  }
})();"""

def generete_script(uid,password):
    filename = f"{settings.RootDirectory}/userscript/generate/{uid}.txt"
    if os.path.exists(filename):
        return filename
    else:
        part2 = f"""\n\nconst Uid = '{uid}'\nconst Password ='{password}'\n"""
        try:
            with open(filename, 'a+', encoding='utf-8') as f:
                f.write(part1+part2+part3)
            return filename
        except IOError as err:
            print("文件处理错误:" + str(err))
            return False




