"use strict";(self.webpackChunk=self.webpackChunk||[]).push([[350],{42786:function(e,t,n){var r=n(12739),a=n(5265),o=n(41376),i=n(14703),s=n(95783),f=n(54354),h=n(69039),u=n(720),l=n(42010),c=n(41372),g=n(31250),w=new l.Z({source:new i.Z({layer:"toner"})}),d=new o.Z({layers:[w],target:"map",view:new f.ZP({center:[0,0],zoom:2})}),m=new h.ZP({stroke:new u.Z({color:"#EAE911",width:2})}),v=new s.Z({wrapX:!1,attributions:'Flight data by <a href="https://openflights.org/data.html">OpenFlights</a>,',loader:function(){fetch("data/openflights/flights.json").then((function(e){return e.json()})).then((function(e){for(var t=e.flights,n=0;n<t.length;n++){var o=t[n],i=o[0],s=o[1],f=new arc.GreatCircle({x:i[1],y:i[0]},{x:s[1],y:s[0]}).Arc(100,{offset:10});if(1===f.geometries.length){var h=new a.Z(f.geometries[0].coords);h.transform("EPSG:4326","EPSG:3857"),p(new r.Z({geometry:h,finished:!1}),50*n)}}w.on("postrender",Z)}))}}),y=new c.Z({source:v,style:function(e){return e.get("finished")?m:null}});d.addLayer(y);function Z(e){var t=(0,g.u3)(e),n=e.frameState;t.setStyle(m);for(var r=v.getFeatures(),o=0;o<r.length;o++){var i=r[o];if(!i.get("finished")){var s=i.getGeometry().getCoordinates(),f=.1*(n.time-i.get("start"));f>=s.length&&i.set("finished",!0);var h=Math.min(f,s.length),u=new a.Z(s.slice(0,h));t.drawGeometry(u)}}d.render()}function p(e,t){window.setTimeout((function(){e.set("start",Date.now()),v.addFeature(e)}),t)}}},function(e){var t=function(t){return e(e.s=t)};t(9877),t(42786)}]);
//# sourceMappingURL=flight-animation.js.map