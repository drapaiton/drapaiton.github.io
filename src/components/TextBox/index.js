import React from "react";
import PropTypes from "prop-types";
import Grid from "@material-ui/core/Grid";
import InputBase from "@material-ui/core/InputBase";
import { makeStyles } from "@material-ui/core/styles";

import "./styles.css";

const useStyles = makeStyles((theme) => ({
  text: {
    color: "white",
    position: "relative",
    zIndex: 1,
    minHeight: "20px",
    maxHeight: "100px",
    overflowX: "hidden",
    overflowY: "auto",
    fontWeight: 500,
  },
}));

const TextBox = ({ handleChange, handleKeyDown }) => {
  const classes = useStyles();
  return (
    <Grid container spacing={3} className="hannah-chat__container">
      <Grid item xs></Grid>
      <Grid item xs={11}>
        <InputBase
          onKeyDown={handleKeyDown}
          onChange={handleChange}
          className={`${classes.text} hannah-chat__input`}
          fullWidth
          placeholder="Write Something"
          inputProps={{ "aria-label": "Write Something" }}
        />
      </Grid>
    </Grid>
  );
};

TextBox.propTypes = {
  handleChange: PropTypes.func,
  handleKeyDown: PropTypes.func,
};

TextBox.defaultProps = {
  handleChange: () => {},
  handleKeyDown: () => {},
};

export default TextBox;
