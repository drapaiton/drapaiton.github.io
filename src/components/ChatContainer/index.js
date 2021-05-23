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
    <Container fluid>
      <Grid container spacing={3}>
        <Grid item xs={4} className={classes.root}></Grid>
        <Grid item xs className={classes.grid}>
          <ChatArea />
        </Grid>
      </Grid>
    </Container>
  );
};

export default ChatContainer;
