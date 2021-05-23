import React from "react";
import { makeStyles } from "@material-ui/core/styles";

import ChatContainer from "../components/ChatContainer";

import useSocket from "./hooks/useSocket";
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
  useSocket();

  const classes = useStyles();
  return (
    <div className={classes.outer}>
      <div className={classes.middle}>
        <div className={classes.inner}>
          <ChatContainer />
        </div>
      </div>
    </div>
  );
};

export default App;
