import React from "react";
import PropTypes from "prop-types";

import MessageContext from "./MessagesContext";
import useSocket from "../../hooks/useSocket";

const MessagesState = ({ children }) => {
  const { handleSendMessage } = useSocket();

  const receiveMessage = () => {};

  return (
    <MessageContext.Provider
      value={{
        sendMessage: handleSendMessage,
        receiveMessage: receiveMessage,
      }}
    >
      {children}
    </MessageContext.Provider>
  );
};

MessagesState.propTypes = {
  children: PropTypes.node,
};

export default MessagesState;
