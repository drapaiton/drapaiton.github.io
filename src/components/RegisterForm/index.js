import React, { useState } from "react";
import PropTypes from "prop-types";
import Card from "@material-ui/core/Card";
import Button from "@material-ui/core/Button";
import TextField from "@material-ui/core/TextField";
import Typography from "@material-ui/core/Typography";
import CardContent from "@material-ui/core/CardContent";
import CardActions from "@material-ui/core/CardActions";

import "./styles.css";

const RegisterForm = () => {
  const [nickname, setNickname] = useState("");

  return (
    <div className="hannah-register__container">
      <Card className="hannah-register">
        <Typography
          className="hannah-register__registerForm"
          color="textSecondary"
          gutterBottom
        >
          Please insert your user name
        </Typography>
        <CardContent>
          <TextField
            onChange={(e) => setNickname(e.target.value)}
            id="insert_name"
            label="UserName"
          />
        </CardContent>
        <CardActions>
          <Button
            onClick={() => handleClick(nickname)}
            variant="contained"
            color="primary"
            fullWidth
          >
            Init session
          </Button>
        </CardActions>
      </Card>
    </div>
  );
};

RegisterForm.propTypes = {};

export default RegisterForm;
