"use strict";(self.webpackChunk=self.webpackChunk||[]).push([[6348],{88551:function(e,n,o){var r=o(41376),t=o(79847),s=o(42010),a=o(54354),c=new Blob(['var e=self;e.onmessage=function(s){console.log("version worker received message:",s.data),e.postMessage("version: ".concat("latest"))};'],{type:"application/javascript"}),i=URL.createObjectURL(c);var v=new r.Z({layers:[new s.Z({source:new t.Z})],target:"map",view:new a.ZP({center:[0,0],zoom:2})}),u=new Worker(i);u.addEventListener("error",(function(e){console.error("worker error",e)})),u.addEventListener("message",(function(e){console.log("message from worker:",e.data)})),v.on("moveend",(function(e){var n=e.frameState.viewState;u.postMessage({zoom:n.zoom,center:n.center})}))}},function(e){var n=function(n){return e(e.s=n)};n(9877),n(88551)}]);
//# sourceMappingURL=worker.js.map