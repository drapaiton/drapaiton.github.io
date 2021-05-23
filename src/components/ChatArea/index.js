import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";

const useStyles = makeStyles((theme) => ({
  title: {
    height: "50px",
  },
  body: {
    height: "600px",
  },
  footer: {
    height: "50px",
  },
}));

const ChatArea = () => {
  const classes = useStyles();
  return (
    <Grid
      container
      direction="column"
      justify="space-between"
      alignItems="stretch"
    >
      <Grid item className={classes.title}>
        uno
      </Grid>
      <Grid item className={classes.body}>
        dos
      </Grid>
      <Grid item className={classes.footer}>
        tres
      </Grid>
    </Grid>
  );
};

export default ChatArea;
