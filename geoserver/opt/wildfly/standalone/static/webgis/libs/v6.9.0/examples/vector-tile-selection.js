"use strict";(self.webpackChunk=self.webpackChunk||[]).push([[3857],{92004:function(e,n,t){var r=t(8768),o=t(41376),c=t(14197),i=t(28083),l=t(54354),a=t(69039),s=t(720),u=t(77975),g={},v=new a.ZP({stroke:new s.Z({color:"gray",width:1}),fill:new u.Z({color:"rgba(20,20,20,0.9)"})}),w=new a.ZP({stroke:new s.Z({color:"rgba(200,20,20,0.8)",width:2}),fill:new u.Z({color:"rgba(200,20,20,0.4)"})}),f=new c.Z({declutter:!0,source:new i.Z({maxZoom:15,format:new r.Z({idProperty:"iso_a3"}),url:"https://ahocevar.com/geoserver/gwc/service/tms/1.0.0/ne:ne_10m_admin_0_countries@EPSG%3A900913@pbf/{z}/{x}/{-y}.pbf"}),style:v}),d=new o.Z({layers:[f],target:"map",view:new l.ZP({center:[0,0],zoom:2,multiWorld:!0})}),m=new c.Z({map:d,renderMode:"vector",source:f.getSource(),style:function(e){if(e.getId()in g)return w}}),p=document.getElementById("type");d.on(["click","pointermove"],(function(e){"singleselect-hover"===p.value&&"pointermove"!==e.type||"singleselect-hover"!==p.value&&"pointermove"===e.type||f.getFeatures(e.pixel).then((function(e){if(!e.length)return g={},void m.changed();var n=e[0];if(n){var t=n.getId();0===p.value.indexOf("singleselect")&&(g={}),g[t]=n,m.changed()}}))}))}},function(e){var n=function(n){return e(e.s=n)};n(9877),n(92004)}]);
//# sourceMappingURL=vector-tile-selection.js.map