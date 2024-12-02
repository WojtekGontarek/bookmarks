const siteUrl = '//127.0.0.1:8000/';
const styleUrl = siteUrl + 'static/css/bookmarklet.css';
const minWidth = 250
const minHeight = 250

var head = document.getElementsByTagName('head')[0];
var link = document.createElement("link");
link.rel = "stylesheet";
link.type = "text/css";