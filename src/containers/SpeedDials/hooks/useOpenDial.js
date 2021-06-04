import { useState } from "react";

const useOpenDial = () => {
  const [open, setOpen] = useState(false);

  function handleOpen(value) {
    setOpen(value);
  }

  return {
    open,
    handleOpen,
  };
};

export default useOpenDial;
