import React, { useContext } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";

import TextBox from "../TextBox";
import ChatZone from "../ChatZone";
import ChatInformation from "../ChatInformation";
import MessageContext from "../../context/messages/MessagesContext";

import "./styles.css";
import useMessages from "./hooks/useMessages";
import useFetch from "./hooks/useFetch";

const useStyles = makeStyles((theme) => ({
  title: {
    height: "50px",
  },
  body: {
    height: "600px",
    overflowY: "scroll",
    overflowX: "hidden",
    scrollbarColor: "thistle white",
    scrollbarWidth: "thin",
    //transform: "rotate(180deg)",
  },
  footer: {},
}));

const ChatArea = () => {
  const {
    shot,
    method,
    payload,
    message,
    paintEmoji,
    handleSetShot,
    handleSetMessage,
    handleSendMessage,
    handleSetPaintEmoji,
  } = useMessages();

  const POST_URL = shot && process.env.REACT_APP_MESSAGES_POST;

  const { sendMessage, pushMessage } = useContext(MessageContext);
  const { data } = useFetch(payload, method, POST_URL);
  console.log("data-------", data);

  const classes = useStyles();

  const onHandleChange = (event) => {
    event.preventDefault();
    handleSetMessage(event.target.value);
  };

  const onHandleKeyDown = (event) => {
    if (event.keyCode === 13) {
      handleSendMessage(message, "POST");
      pushMessage(message);
      handleSetShot(true);
      handleSetMessage("");
    }
  };

  return (
    <Grid
      container
      direction="column"
      justify="space-between"
      alignItems="stretch"
    >
      <Grid item className={classes.title}>
        <ChatInformation />
      </Grid>
      <Grid item className={`${classes.body} hannah-chatarea__container`}>
        <ChatZone />
      </Grid>
      <Grid item className={classes.footer}>
        <TextBox
          handleSetEmoji={handleSetPaintEmoji}
          message={message}
          inputValue={message}
          handleChange={(e) => onHandleChange(e)}
          handleKeyDown={(e) => onHandleKeyDown(e)}
        />
      </Grid>
    </Grid>
  );
};

export default ChatArea;
