"use strict";(self.webpackChunk=self.webpackChunk||[]).push([[1695],{18515:function(e,n,t){var o,c=t(61038),u=t(41376),r=t(54354),a=t(79847),i=t(95783),s=t(42010),w=t(41372),d=new s.Z({source:new a.Z}),f=new i.Z({wrapX:!1}),l=new w.Z({source:f}),m=new u.Z({layers:[d,l],target:"map",view:new r.ZP({center:[-11e6,46e5],zoom:4})}),v=document.getElementById("type");function p(){"None"!==v.value&&(o=new c.ZP({source:f,type:v.value}),m.addInteraction(o))}v.onchange=function(){m.removeInteraction(o),p()},document.getElementById("undo").addEventListener("click",(function(){o.removeLastPoint()})),p()}},function(e){var n=function(n){return e(e.s=n)};n(9877),n(18515)}]);
//# sourceMappingURL=draw-features.js.map