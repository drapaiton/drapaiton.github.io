import React, { useState, useEffect, useRef } from "react";

const SOCKET_URL = process.env.REACT_APP_WSS_ADDRESS;

const useSocket = () => {
  const [isPaused, setPause] = useState(false);
  const [receivedMessage, setReceivedMessage] = useState(null);
  const socket = useRef(null);

  useEffect(() => {
    socket.current = new WebSocket(SOCKET_URL);
    socket.current.onopen = (data) => console.log("ws opened", data);
    socket.current.onclose = () => console.log("ws closed");

    return () => {
      socket.current.close();
    };
  }, []);

  useEffect(() => {
    if (!socket.current) return;

    socket.current.onmessage = (e) => {
      if (isPaused) return;
      const message = e.data;
      console.log("e", message);
      setReceivedMessage(message);
    };
  }, [isPaused]);

  const handleSendMessage = (message) => {
    socket.current.send(
      JSON.stringify({
        message: message,
        action: "message",
      })
    );
  };

  return { handleSendMessage, receivedMessage };
};

export default useSocket;
