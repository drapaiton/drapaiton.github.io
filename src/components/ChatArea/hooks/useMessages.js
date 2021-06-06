import { useState } from "react";

const useMessages = () => {
  const [message, setMessage] = useState("");
  const [paintEmoji, setPaintEmoji] = useState("");
  const [payload, setPayload] = useState([]);
  const [method, setMethod] = useState("POST");
  const [shot, setShot] = useState(false);

  const handleSetMessage = (message) => {
    setMessage(message);
  };

  const handleSetPaintEmoji = (e) => {
    let sym = e.unified.split("-");
    let codesArray = [];
    sym.forEach((el) => codesArray.push("0x" + el));
    let emo = String.fromCodePoint(...codesArray);
    setMessage(message + emo);
  };

  const handleSendMessage = (text, method) => {
    const messageJSON = {
      username: "hannah",
      content: text,
      message_type: "MESSAGE",
    };
    setPayload(messageJSON);
    setMethod(method);
  };

  const handleSetShot = (value) => {
    setShot(value);
  };

  return {
    shot,
    method,
    message,
    payload,
    paintEmoji,
    handleSetShot,
    handleSetMessage,
    handleSendMessage,
    handleSetPaintEmoji,
  };
};

export default useMessages;
