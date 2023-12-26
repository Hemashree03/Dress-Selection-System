import * as React from "react";
import Box from "@mui/material/Box";
import TextField from "@mui/material/TextField";
import { makeStyles } from "@mui/styles";
import image1 from "../src/images/bg1.jpeg";
import { width } from "@mui/system";
import Gender from "./gender";
import UnstyledSelectControlled from "./sizedropdown";
import UnstyledSelectControlledPrice from "./price";
import ManuallyProvideCustomColor from "./skintone";
import { Button } from "@mui/material";

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
    height: 550,
    width: 400,
    flexDirection: "column",
    gap: 24,
  },
  rowFlex: {
    display: "flex",
    flexDirection: "row",
    gap:40,
    alignItems:'center'
  },
});

export default function InputField({next}) {
  const classes = useStyles();

  return (
    <div className={classes.mainContainer}>
      <div className={classes.form}>
        <TextField label="Name" color="primary" focused />

        <TextField label="Age" color="primary" focused />
        <Gender />
        <UnstyledSelectControlled />
        <TextField label="Fav Color" color="primary" focused />
        <UnstyledSelectControlledPrice />
        <div className={classes.rowFlex} >
          <p>Skin Tone</p>
          <ManuallyProvideCustomColor />
        </div>
        <Button variant="contained" onClick={()=>next()}>Next</Button>
      </div>
    </div>
  );
}
