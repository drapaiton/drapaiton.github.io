import React from "react";
import ReactDOM from "react-dom";
import App from "./components/App.js";

import MessagesState from "./context/messages/MessagesState";

ReactDOM.render(
  <MessagesState>
    <App />
  </MessagesState>,
  document.getElementById("root")
);
