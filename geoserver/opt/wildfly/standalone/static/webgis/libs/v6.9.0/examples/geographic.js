"use strict";(self.webpackChunk=self.webpackChunk||[]).push([[3062],{99595:function(e,t,n){var o=n(69039),r=n(77138),i=n(77975),a=n(41376),s=n(54354),c=n(12739),l=n(70492),p=n(79847),u=n(95783),d=n(75469),w=n(42010),f=n(41372);(0,n(12810).eL)();var m=[-110,45],v=new d.Z(m),g=new a.Z({target:"map",view:new s.ZP({center:m,zoom:8}),layers:[new w.Z({source:new p.Z}),new f.Z({source:new u.Z({features:[new c.Z(v)]}),style:new o.ZP({image:new r.Z({radius:9,fill:new i.Z({color:"red"})})})})]}),Z=document.getElementById("popup"),h=new l.Z({element:Z,positioning:"bottom-center",stopEvent:!1,offset:[0,-10]});function y(e){return"\n    <table>\n      <tbody>\n        <tr><th>lon</th><td>".concat(e[0].toFixed(2),"</td></tr>\n        <tr><th>lat</th><td>").concat(e[1].toFixed(2),"</td></tr>\n      </tbody>\n    </table>")}g.addOverlay(h);var b=document.getElementById("info");g.on("moveend",(function(){var e=g.getView().getCenter();b.innerHTML=y(e)})),g.on("click",(function(e){var t=g.getFeaturesAtPixel(e.pixel)[0];if(t){var n=t.getGeometry().getCoordinates();h.setPosition(n),$(Z).popover({container:Z.parentElement,html:!0,sanitize:!1,content:y(n),placement:"top"}),$(Z).popover("show")}else $(Z).popover("dispose")})),g.on("pointermove",(function(e){g.hasFeatureAtPixel(e.pixel)?g.getViewport().style.cursor="pointer":g.getViewport().style.cursor="inherit"}))}},function(e){var t=function(t){return e(e.s=t)};t(9877),t(99595)}]);
//# sourceMappingURL=geographic.js.map