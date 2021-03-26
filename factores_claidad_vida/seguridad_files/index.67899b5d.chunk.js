(window["webpackJsonp"] = window["webpackJsonp"] || []).push([[1],{

/***/ 100:
/***/ (function(module, exports, __webpack_require__) {

module.exports = __webpack_require__(142);


/***/ }),

/***/ 142:
/***/ (function(module, __webpack_exports__, __webpack_require__) {

"use strict";
// ESM COMPAT FLAG
__webpack_require__.r(__webpack_exports__);

// EXTERNAL MODULE: ./node_modules/react/index.js
var react = __webpack_require__(0);
var react_default = /*#__PURE__*/__webpack_require__.n(react);

// EXTERNAL MODULE: ./node_modules/react-dom/index.js
var react_dom = __webpack_require__(15);
var react_dom_default = /*#__PURE__*/__webpack_require__.n(react_dom);

// EXTERNAL MODULE: ./node_modules/@datawheel/tesseract-explorer/dist/explorer.esm.js
var explorer_esm = __webpack_require__(53);

// EXTERNAL MODULE: ./node_modules/react-redux/es/index.js + 23 modules
var es = __webpack_require__(17);

// EXTERNAL MODULE: ./node_modules/redux/es/redux.js
var redux = __webpack_require__(41);

// EXTERNAL MODULE: ./node_modules/normalize.css/normalize.css
var normalize = __webpack_require__(136);

// EXTERNAL MODULE: ./node_modules/@blueprintjs/icons/lib/css/blueprint-icons.css
var blueprint_icons = __webpack_require__(137);

// EXTERNAL MODULE: ./node_modules/@blueprintjs/core/lib/css/blueprint.css
var blueprint = __webpack_require__(138);

// EXTERNAL MODULE: ./node_modules/@blueprintjs/select/lib/css/blueprint-select.css
var blueprint_select = __webpack_require__(139);

// EXTERNAL MODULE: ./node_modules/@blueprintjs/table/lib/css/table.css
var table = __webpack_require__(140);

// EXTERNAL MODULE: ./node_modules/@datawheel/tesseract-explorer/dist/explorer.css
var explorer = __webpack_require__(141);

// CONCATENATED MODULE: ./App.js
function _typeof(obj) { if (typeof Symbol === "function" && typeof Symbol.iterator === "symbol") { _typeof = function _typeof(obj) { return typeof obj; }; } else { _typeof = function _typeof(obj) { return obj && typeof Symbol === "function" && obj.constructor === Symbol && obj !== Symbol.prototype ? "symbol" : typeof obj; }; } return _typeof(obj); }











var composeEnhancers = (typeof window === "undefined" ? "undefined" : _typeof(window)) === "object" && window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ ? window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ : redux["c" /* compose */];
var enhancers = composeEnhancers(Object(redux["a" /* applyMiddleware */])(explorer_esm["c" /* olapMiddleware */], explorer_esm["d" /* permalinkMiddleware */]));
var store = Object(redux["d" /* createStore */])(explorer_esm["b" /* explorerReducer */], null, enhancers);

function App(props) {
  return react_default.a.createElement(es["a" /* Provider */], {
    store: store
  }, react_default.a.createElement(explorer_esm["a" /* Explorer */], {
    src: props.serverUrl,
    title: props.appTitle,
    locale: ["en", "es"]
  }));
}

/* harmony default export */ var App_0 = (App);
// CONCATENATED MODULE: ./index.js



react_dom_default.a.render(Object(react["createElement"])(App_0, {
  serverUrl: "https://api.datamexico.org/tesseract/",
  appTitle: "DataMexico API Explorer"
}), document.getElementById("app"));

/***/ })

},[[100,2,0]]]);
//# sourceMappingURL=index.67899b5d.chunk.js.map