import { useState } from "react";

const useMessages = () => {
  const [message, setMessage] = useState("");

  const handleSetMessage = (message) => {
    setMessage(message);
  };

  return { message, handleSetMessage };
};

export default useMessages;
