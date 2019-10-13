/**
 * @license
 * Copyright (c) 2014, 2019, Oracle and/or its affiliates.
 * The Universal Permissive License (UPL), Version 1.0
 */
define(["ojs/ojlogger"],function(e){"use strict";var t=function(){};return t.getThemeName=function(){return(t.parseJSONFromFontFamily("oj-theme-json")||{}).name},t.getThemeTargetPlatform=function(){return(t.parseJSONFromFontFamily("oj-theme-json")||{}).targetPlatform},t.clearCache=function(){this._cache=null},t.parseJSONFromFontFamily=function(t){null==this._cache&&(this._cache={},this._null_cache_value={},this._headfontstring=window.getComputedStyle(document.head).getPropertyValue("font-family"));var r=this._cache[t];if(r===this._null_cache_value)return null;if(null!=r)return r;var n=document.createElement("meta");n.className=t,document.head.appendChild(n);var a=window.getComputedStyle(n).getPropertyValue("font-family");if(null!=a)if(a===this._headfontstring)e.warn("parseJSONFromFontFamily: When the selector ",t," is applied the font-family read off the dom element is ",a,". The parent dom elment has the same font-family value."," This is interpreted to mean that no value was sent down for selector ",t,". Null will be returned.");else{var o=a.replace(/^['"]+|\s+|\\|(;\s?})+|['"]$/g,"");if(o)try{r=JSON.parse(o)}catch(a){var l=o.indexOf(","),i=!1;if(l>-1){o=o.substring(l+2);try{r=JSON.parse(o),i=!0}catch(e){}}if(!1===i)throw e.error("Error parsing json for selector "+t+".\nString being parsed is "+o+". Error is:\n",a),document.head.removeChild(n),a}}return document.head.removeChild(n),this._cache[t]=null==r?this._null_cache_value:r,r},t});