import React from "react";
import PropTypes from "prop-types";
import { Picker } from "emoji-mart";
import "emoji-mart/css/emoji-mart.css";
import InputBase from "@material-ui/core/InputBase";
import { makeStyles } from "@material-ui/core/styles";
import IconButton from "@material-ui/core/IconButton";
import EmojiEmotionsTwoToneIcon from "@material-ui/icons/EmojiEmotionsTwoTone";

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

const TextBox = ({ message, handleChange, handleKeyDown, handleSetEmoji }) => {
  const { showEmoticons, setEmoticons } = useEmoticons();
  const classes = useStyles();

  return (
    <>
      <div className="hannah-chat__emojis">
        {showEmoticons && <Picker onSelect={(e) => handleSetEmoji(e)} />}
      </div>
      <div className="hannah-chat__container">
        <IconButton
          color="primary"
          aria-label="add to shopping cart"
          onClick={() => setEmoticons(showEmoticons)}
        >
          <EmojiEmotionsTwoToneIcon fontSize="large" />
        </IconButton>
        <InputBase
          value={message}
          onKeyDown={handleKeyDown}
          onChange={handleChange}
          className={`${classes.text} hannah-chat__input`}
          fullWidth
          placeholder="Write Something"
          inputProps={{ "aria-label": "Write Something" }}
        />
      </div>
    </>
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
