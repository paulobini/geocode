"use strict";(self.webpackChunk=self.webpackChunk||[]).push([[4570],{33562:function(t,e,n){var o=n(41376),r=n(42010),i=n(54354),a=n(46583),c=n(31998),s=n(32275);function u(t){return(u="function"==typeof Symbol&&"symbol"==typeof Symbol.iterator?function(t){return typeof t}:function(t){return t&&"function"==typeof Symbol&&t.constructor===Symbol&&t!==Symbol.prototype?"symbol":typeof t})(t)}function f(t,e){for(var n=0;n<e.length;n++){var o=e[n];o.enumerable=o.enumerable||!1,o.configurable=!0,"value"in o&&(o.writable=!0),Object.defineProperty(t,o.key,o)}}function l(t,e){return(l=Object.setPrototypeOf||function(t,e){return t.__proto__=e,t})(t,e)}function p(t){var e=function(){if("undefined"==typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"==typeof Proxy)return!0;try{return Boolean.prototype.valueOf.call(Reflect.construct(Boolean,[],(function(){}))),!0}catch(t){return!1}}();return function(){var n,o=y(t);if(e){var r=y(this).constructor;n=Reflect.construct(o,arguments,r)}else n=o.apply(this,arguments);return h(this,n)}}function h(t,e){if(e&&("object"===u(e)||"function"==typeof e))return e;if(void 0!==e)throw new TypeError("Derived constructors may only return object or undefined");return function(t){if(void 0===t)throw new ReferenceError("this hasn't been initialised - super() hasn't been called");return t}(t)}function y(t){return(y=Object.setPrototypeOf?Object.getPrototypeOf:function(t){return t.__proto__||Object.getPrototypeOf(t)})(t)}var m=function(t){!function(t,e){if("function"!=typeof e&&null!==e)throw new TypeError("Super expression must either be null or a function");t.prototype=Object.create(e&&e.prototype,{constructor:{value:t,writable:!0,configurable:!0}}),e&&l(t,e)}(i,t);var e,n,o,r=p(i);function i(t){var e;return function(t,e){if(!(t instanceof e))throw new TypeError("Cannot call a class as a function")}(this,i),(e=r.call(this,{attributions:t.attributions,cacheSize:t.cacheSize,crossOrigin:t.crossOrigin,maxZoom:void 0!==t.maxZoom?t.maxZoom:18,minZoom:t.minZoom,projection:t.projection,transition:t.transition,wrapX:t.wrapX,zDirection:t.zDirection})).account_=t.account,e.mapId_=t.map||"",e.config_=t.config||{},e.templateCache_={},e.initializeMap_(),e}return e=i,(n=[{key:"getConfig",value:function(){return this.config_}},{key:"updateConfig",value:function(t){(0,s.f0)(this.config_,t),this.initializeMap_()}},{key:"setConfig",value:function(t){this.config_=t||{},this.initializeMap_()}},{key:"initializeMap_",value:function(){var t=JSON.stringify(this.config_);if(this.templateCache_[t])this.applyTemplate_(this.templateCache_[t]);else{var e="https://"+this.account_+".carto.com/api/v1/map";this.mapId_&&(e+="/named/"+this.mapId_);var n=new XMLHttpRequest;n.addEventListener("load",this.handleInitResponse_.bind(this,t)),n.addEventListener("error",this.handleInitError_.bind(this)),n.open("POST",e),n.setRequestHeader("Content-type","application/json"),n.send(JSON.stringify(this.config_))}}},{key:"handleInitResponse_",value:function(t,e){var n=e.target;if(!n.status||n.status>=200&&n.status<300){var o;try{o=JSON.parse(n.responseText)}catch(t){return void this.setState(a.Z.ERROR)}this.applyTemplate_(o),this.templateCache_[t]=o,this.setState(a.Z.READY)}else this.setState(a.Z.ERROR)}},{key:"handleInitError_",value:function(t){this.setState(a.Z.ERROR)}},{key:"applyTemplate_",value:function(t){var e="https://"+t.cdn_url.https+"/"+this.account_+"/api/v1/map/"+t.layergroupid+"/{z}/{x}/{y}.png";this.setUrl(e)}}])&&f(e.prototype,n),o&&f(e,o),i}(c.Z),_=n(79847),v={layers:[{type:"cartodb",options:{cartocss_version:"2.1.1",cartocss:"#layer { polygon-fill: #F00; }",sql:"select * from european_countries_e where area > 0"}}]},d=new m({account:"documentation",config:v});new o.Z({layers:[new r.Z({source:new _.Z}),new r.Z({source:d})],target:"map",view:new i.ZP({center:[0,0],zoom:2})});document.getElementById("country-area").addEventListener("change",(function(){var t;t=this.value,v.layers[0].options.sql="select * from european_countries_e where area > "+t,d.setConfig(v)}))}},function(t){var e=function(e){return t(t.s=e)};e(9877),e(33562)}]);
//# sourceMappingURL=cartodb.js.map