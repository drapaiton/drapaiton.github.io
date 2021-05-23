import React, { useState, useEffect, useRef } from "react";

const SOCKET_URL = process.env.REACT_APP_WSS_ADDRESS;

const useSocket = () => {
  const [isPaused, setPause] = useState(false);
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
      const message = JSON.parse(e.data);
      console.log("e", message);
    };
  }, [isPaused]);

  return null;
};

export default useSocket;
