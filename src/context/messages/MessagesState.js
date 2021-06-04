import React, { useReducer, useEffect } from "react";
import PropTypes from "prop-types";

import MessageContext from "./MessagesContext";
import useSocket from "../../hooks/useSocket";

import MessagesReducer from "./MessagesReducer";
import { PUSH_MESSAGE } from "./constants";

const MessagesState = ({ children }) => {
  const { handleSendMessage, receivedMessage } = useSocket();

  const initialState = {
    messages: [],
  };

  const [state, dispatch] = useReducer(MessagesReducer, initialState);

  useEffect(() => {
    if (receivedMessage) {
      dispatch({
        type: PUSH_MESSAGE,
        payload: { type: "received", body: receivedMessage },
      });
    }
  }, [receivedMessage]);

  const pushMessage = (message) => {
    dispatch({
      type: PUSH_MESSAGE,
      payload: { type: "sent", body: message },
    });
  };

  return (
    <MessageContext.Provider
      value={{
        sendMessage: handleSendMessage,
        receivedMessage: receivedMessage,
        pushMessage: pushMessage,
        listMessages: state.messages,
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
