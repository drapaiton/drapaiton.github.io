import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Container from "@material-ui/core/Container";
import Grid from "@material-ui/core/Grid";

import ChatArea from "../../components/ChatArea";

const useStyles = makeStyles((theme) => ({
  root: {
    backgroundColor: "red",
  },
  grid: {
    backgroundColor: "green",
  },
}));

const ChatContainer = () => {
  const classes = useStyles();
  return (
    <Container>
      <Grid container spacing={0}>
        <Grid item xs={4} className={classes.root}></Grid>
        <Grid item xs>
          <ChatArea />
        </Grid>
      </Grid>
    </Container>
  );
};

export default ChatContainer;
