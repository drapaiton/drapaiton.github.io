import { useEffect, useLayoutEffect, useState } from "react";

const useEmoticons = () => {
  const [showEmoticons, setShowEmoticons] = useState(false);

  const setEmoticons = (value) => {
    setShowEmoticons(!value);
  };

  return {
    showEmoticons,
    setEmoticons,
  };
};

export default useEmoticons;
