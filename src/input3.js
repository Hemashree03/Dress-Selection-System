import * as React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import { makeStyles } from "@mui/styles";
import image1 from "../src/images/bg1.jpeg";
import { width } from "@mui/system";
import Gender from "./gender";
import UnstyledSelectControlled from "./sizedropdown";
import ManuallyProvideCustomColor from "./skintone";
import { Button } from "@mui/material";
import DressType from "./dresstype";

const useStyles = makeStyles({
  mainContainer: {
    backgroundImage: `url(${image1})`,
    backgroundRepeat: "none",
    backgroundPosition: "center",
    height: "100vh",
    width: "100%",
    display: "flex",
    alignItems: "center",
    position: "relative",
    justifyContent: "center",
  },
  form: {
    padding: 40,
    backgroundColor: "white",
    display: "flex",
    justifyContent: "center",
    height: 150,
    width: 400,
    flexDirection: "column",
    gap: 24,
  },
  rowFlex: {
    display: "flex",
    flexDirection: "row",
    gap: 40,
    alignItems: "center",
  },
  rowFlexButton:{
    display: "flex",
    flexDirection: "row",
    justifyContent:'space-between',
    alignItems:'center'
  }
});

export default function InputField3({ next,back }) {
  const classes = useStyles();

  return (
    <div className={classes.mainContainer}>
      <div className={classes.form}>
             <DressType />
        <div className={classes.rowFlexButton}>
          <Button variant="contained" onClick={() => back()}>
            Back
          </Button>
          <Button variant="contained" onClick={() => next()}>
            Finish
          </Button>
        </div>
      </div>
    </div>
  );
}
