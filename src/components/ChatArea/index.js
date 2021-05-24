import React, { useContext } from "react";
import { makeStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";

import TextBox from "../TextBox";
import ChatZone from "../ChatZone";
import ChatInformation from "../ChatInformation";
import MessageContext from "../../context/messages/MessagesContext";

import useMessages from "./hooks/useMessages";

const useStyles = makeStyles((theme) => ({
  title: {
    height: "50px",
  },
  body: {
    height: "600px",
  },
  footer: {},
}));

const ChatArea = () => {
  const { message, handleSetMessage } = useMessages();
  const { sendMessage } = useContext(MessageContext);
  const classes = useStyles();

  const onHandleChange = (event) => {
    event.preventDefault();
    handleSetMessage(event.target.value);
  };

  const onHandleKeyDown = (event) => {
    if (event.keyCode === 13) {
      handleSetMessage("");
      sendMessage(message);
    }
  };

  const onHandleEmojiClick = (event) => {};

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
      <Grid item className={classes.body}>
        <ChatZone />
      </Grid>
      <Grid item className={classes.footer}>
        <TextBox
          handleChange={(e) => onHandleChange(e)}
          handleKeyDown={(e) => onHandleKeyDown(e)}
          handleEmojiClick={(e) => onHandleEmojiClick(e)}
        />
      </Grid>
    </Grid>
  );
};

export default ChatArea;
