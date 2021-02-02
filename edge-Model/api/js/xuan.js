// ==UserScript==
// @name         HV Auto Pony
// @author       mc, Megumin
// @namespace    mingxiansen
// @version      1.6.9.dev1
// @description  Calculate pony riddle automatically
// @match        http*://hentaiverse.org/*
// @match        http*://hentaiverse.org/isekai/*
// @match        http://alt.hentaiverse.org/*
// @compatible   Firefox + Greasemonkey
// @compatible   Chrome/Chromium + Tampermonkey
// @run-at       document-end
// @grant        none
// ==/UserScript==

if (getElem('#navbar') || !getElem('#riddlemaster')) {
    return;
}
var host;
var getLocation = document.location.href;
if (getLocation.match('https://')) {
    host = 'https://47.100.63.75';
} else if (getLocation.match('http://')) {
    host = 'http://47.100.63.75';
}

//Redefine append function
Object.prototype.appends = function(element) {
    this.insertAdjacentHTML('beforeend', element);
};

(function() {
    //Catch pony image
    //e.g. *hentaiverse.org/riddlemaster?uid=xxxx&v=yyyy
    var img = getElem('img[src*="hentaiverse.org/isekai/riddlemaster?"]');
    if (img && img.src.length > 0) {
        getElem('div[id="riddlemid"]').appends('<p>Picture detected, uploading ...</p>');
        //Get img url
        var img_src = img.src;
        var param_str = img_src.split('?')[1];
        var reg = new RegExp("uid=([a-zA-Z0-9]+)&v=([a-zA-Z0-9]+)");
        var param = param_str.match(reg);
        var uid = param[1]
        var v_code = param[2]
        //Sending uid and v_code to the server for saving
        var xhr = new XMLHttpRequest();
        xhr.open('get', img_src, true);
        xhr.responseType = 'blob';
        xhr.onload = function() {
            if (this.status == 200) {
                //getElem('div[id="riddlemid"]').append('<p>Get picture successfully</p>')
                var blob_data = this.response;
                var fd = new FormData();
                fd.set('uid', uid);
                fd.set('v_code', v_code);
                fd.set('img', blob_data, uid + '-' + v_code + '.jpg');
                //Post image
                var send_url = host + '/index.php?act=pony_answer';
                postImage(send_url, function(response_tfx) {
                    if (response_tfx.status == 'success') {
                        if (response_tfx.is_chocie) {
                            getElem('div[id="riddlemid"]').appends('<p>Got answer :' + response_tfx.answer + '</p>');
                            var input_text = getElem('input[id="riddleanswer"]');
                            if (input_text.value == '') { input_text.value = response_tfx.answer }
                            getElem('div[id="riddlemid"]').appends('<p>Submit automatically after 3 seconds</p>');
                            setTimeout(function() {
                                getElem('#riddleanswer+img').click();
                            }, 2000 + Math.random() * 1000);
                        } else {
                            getElem('div[id="riddlemid"]').appends('<p>Cannot detect image, no answer :' + response_tfx.answer + '</p>');
                        }
                    } else {
                        getElem('div[id="riddlemid"]').appends('<p>Get response rejected, error :' + response_tfx.reason + '</p>')
                    }
                }, fd);
            } else {
                getElem('div[id="riddlemid"]').appends('<p>Failed to get image</p>')
            }
        };
        xhr.send();
    }
})();

//Get element
function getElem(ele, mode, parent) {
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

//Post
function postImage(href, func, parm) {
    var xhr = new window.XMLHttpRequest();
    xhr.open(parm ? 'POST' : 'GET', href);
    xhr.onerror = function(xhr, status, error) {
        getElem('div[id="riddlemid"]').appends('<p>An error occurred while getting the answer, program stopped</p>');
        getElem('div[id="riddlemid"]').appends(xhr);
        getElem('div[id="riddlemid"]').appends(status);
        getElem('div[id="riddlemid"]').appends(error);
    }
    xhr.onload = function(e) {
        if (e.target.status >= 200 && e.target.status < 400 && typeof func === 'function') {
            var data = e.target.response;
            data = (typeof data == 'string') ? JSON.parse(data) : data;
            func(data, e);
        }
        xhr = null;
    }
    xhr.send(parm);
}

//Report info in console
function reportInfo(vars, showType = false) {
    if (showType === true) console.log(typeof vars);
    console.log(vars);
}
