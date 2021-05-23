import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";

import ChatInformation from "../ChatInformation";
import ChatZone from "../ChatZone";
import TextBox from "../TextBox";

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
  const classes = useStyles();

  const onHandleChange = (event) => {
    event.preventDefault();
    console.log("Enter is pressed!", event);
  };

  const onHandleKeyDown = (event) => {
    console.log(event.keyCode);
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
      <Grid item className={classes.body}>
        <ChatZone />
      </Grid>
      <Grid item className={classes.footer}>
        <TextBox
          handleChange={(e) => onHandleChange(e)}
          handleKeyDown={(e) => onHandleKeyDown(e)}
        />
      </Grid>
    </Grid>
  );
};

export default ChatArea;
