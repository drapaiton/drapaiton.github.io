import React from "react";
import { makeStyles } from "@material-ui/core/styles";

import RegisterForm from "../components/RegisterForm";
import ChatContainer from "../components/ChatContainer";

import useStorage from "../hooks/useStorage";

const useStyles = makeStyles((theme) => ({
  outer: {
    display: "table",
    position: "absolute",
    top: 0,
    left: 0,
    height: "100%",
    width: "100%",
  },
  middle: {
    display: "table-cell",
    verticalAlign: "middle",
  },
  inner: {
    marginLeft: "auto",
    marginRight: "auto",
  },
}));

const App = () => {
  const { storage, setUserName, checkUserName, setLocalstorage } = useStorage();

  const onHandleClick = (value) => {
    setLocalstorage(value);
  };

  const renderOption = () => {
    if (storage) {
      return <ChatContainer />;
    }
    return <RegisterForm handleClick={(e) => onHandleClick(e)} />;
  };

  const classes = useStyles();
  return (
    <div className={classes.outer}>
      <div className={classes.middle}>
        <div className={classes.inner}>{renderOption()}</div>
      </div>
    </div>
  );
};

export default App;
