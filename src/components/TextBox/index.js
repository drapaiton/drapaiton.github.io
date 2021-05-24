import React from "react";
import PropTypes from "prop-types";
import Grid from "@material-ui/core/Grid";
import InputBase from "@material-ui/core/InputBase";
import { makeStyles } from "@material-ui/core/styles";
import EmojiPicker from "emoji-picker-react";
import InsertEmoticonIcon from "@material-ui/icons/InsertEmoticon";
import SpeedDial from "../../containers/SpeedDial";

import "./styles.css";
import useEmoticons from "./hooks/useEmoticons";

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

const TextBox = ({ handleChange, handleKeyDown, handleEmojiClick }) => {
  const { showEmoticons, setEmoticons } = useEmoticons();
  const classes = useStyles();

  return (
    <Grid container className="hannah-chat__container">
      <Grid item xs={1}>
        {(!showEmoticons && <SpeedDial />) || (
          <EmojiPicker onEmojiClick={handleEmojiClick} />
        )}
      </Grid>
      <Grid item xs>
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
  handleEmojiClick: PropTypes.func,
};

TextBox.defaultProps = {
  handleChange: () => {},
  handleKeyDown: () => {},
  handleEmojiClick: () => {},
};

export default TextBox;
