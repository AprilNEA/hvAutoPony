// ==UserScript==
// @name         Horse_support_isekai
// @description  Just collect pony pictures.
// @include      http*://hentaiverse.org/*
// @include      http://alt.hentaiverse.org/*
// @compatible   Firefox + Greasemonkey
// @compatible   Chrome/Chromium + Tampermonkey
// @compatible   Android + Firefox + Usi/Tampermonkey
// @compatible   Other + Bookmarklet
// @grant        unsafeWindow
// @grant        GM_xmlhttpRequest
// @run-at       document-end
// @connect      vm24.prave.men
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
    var uuid="18ed40fb-4491-4083-b0e3-2cf16d3fbc55"
    var aaaa = document.getElementById("riddlebot").getElementsByTagName("img")[0].getAttribute("src")
	if(aaaa.search("isekai")!=-1){aaaa=aaaa+'_isekai'}
    var cccc=aaaa.split("?")
    var urla='http://vm24.prave.men/'+uuid+'/'+cccc[1]
    GM_xmlhttpRequest ( {
        method:     "GET",
        url:        urla,
        onload:     function (response) {
            var rp=response.responseText
            if (rp=="A"||rp=="B"||rp=="C"){
                gE('#riddleanswer').value=rp
                gE('#riddleanswer+img').click()
            }
        }
    } )
}