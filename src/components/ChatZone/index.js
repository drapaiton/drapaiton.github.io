import React, { useContext, useEffect } from "react";

import Dialog from "../../containers/Dialog";
import MessagesContext from "../../context/messages/MessagesContext";

import "./styles.css";

const dialogMessage = (message, index) => {
  const { type, body } = message;

  if (type === "sent") {
    return (
      <div className="hannah-chatzone__sent">
        <Dialog key={`key-${index}`} message={body} />
      </div>
    );
  }

  return (
    <div className="hannah-chatzone__received">
      <Dialog key={`key-${index}`} message={body} />
    </div>
  );
};

const ChatZone = () => {
  const { listMessages } = useContext(MessagesContext);

  useEffect(() => {
    let messageBody = document.getElementsByClassName(
      "hannah-chatarea__container"
    )[0];
    messageBody.scrollTop = messageBody.scrollHeight - messageBody.clientHeight;
  }, [listMessages]);

  return (
    <div className="hannah-chatzone">
      {listMessages.map((item, index) => dialogMessage(item, index))}
    </div>
  );
};

export default ChatZone;
