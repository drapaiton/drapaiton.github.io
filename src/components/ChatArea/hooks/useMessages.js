import { useState } from "react";

const useMessages = () => {
  const [message, setMessage] = useState("");
  const [paintEmoji, setPaintEmoji] = useState("");

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

  return { message, paintEmoji, handleSetPaintEmoji, handleSetMessage };
};

export default useMessages;
