import React, { useContext } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";

import TextBox from "../TextBox";
import ChatZone from "../ChatZone";
import ChatInformation from "../ChatInformation";
import MessageContext from "../../context/messages/MessagesContext";

import "./styles.css";
import useMessages from "./hooks/useMessages";

const POST_URL = process.env.REACT_APP_MESSAGES_POST;

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
    message,
    handleSetMessage,
    paintEmoji,
    handleSetPaintEmoji,
  } = useMessages();
  const { sendMessage, pushMessage } = useContext(MessageContext);
  const classes = useStyles();

  const onHandleChange = (event) => {
    event.preventDefault();
    handleSetMessage(event.target.value);
  };

  const onHandleKeyDown = (event) => {
    const messageJSON = {
      username: "hannah",
      content: message,
      message_type: "MESSAGE",
    };
    if (event.keyCode === 13) {
      pushMessage(message);
      fetch(POST_URL, {
        method: "POST",
        mode: "no-cors",
        cache: "no-cache",
        credentials: "same-origin",
        headers: {
          "Content-Type": "application/json",
        },
        redirect: "follow",
        referrerPolicy: "no-referrer",
        body: JSON.stringify({ body: messageJSON }),
      })
        .then((response) => response)
        .then((payload) => {
          console.log(payload.json());
        });
      //sendMessage(messageJSON, "POST", POST_URL);
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
