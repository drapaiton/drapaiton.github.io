import React from "react";
import PropTypes from "prop-types";
import SpeedDial from "@material-ui/lab/SpeedDial";
import SpeedDialIcon from "@material-ui/lab/SpeedDialIcon";
import SpeedDialAction from "@material-ui/lab/SpeedDialAction";
import FileCopyIcon from "@material-ui/icons/FileCopyOutlined";
import SaveIcon from "@material-ui/icons/Save";
import PrintIcon from "@material-ui/icons/Print";
import ShareIcon from "@material-ui/icons/Share";
import FavoriteIcon from "@material-ui/icons/Favorite";

import useOpenDial from "./hooks/useOpenDial";

const actions = [
  { icon: <FileCopyIcon />, name: "Copy" },
  { icon: <SaveIcon />, name: "Save" },
  { icon: <PrintIcon />, name: "Print" },
  { icon: <ShareIcon />, name: "Share" },
  { icon: <FavoriteIcon />, name: "Like" },
];

const SpeedDials = ({ onHandleOpen }) => {
  const { open, handleOpen } = useOpenDial();

  const setHandleOpenDial = (value) => {
    handleOpen(value);
    onHandleOpen(open);
  };

  return (
    <SpeedDial
      ariaLabel="SpeedDial example"
      icon={<SpeedDialIcon />}
      onClick={() => setHandleOpenDial(!open)}
      open={open}
      direction="right"
    >
      {actions.map((action) => (
        <SpeedDialAction
          key={action.name}
          icon={action.icon}
          tooltipTitle={action.name}
          onClick={() => setHandleOpenDial(false)}
        />
      ))}
    </SpeedDial>
  );
};

SpeedDial.propTypes = {
  onHandleOpen: PropTypes.func,
};

SpeedDial.defaultProps = {
  onHandleOpen: () => {},
};

export default SpeedDials;
