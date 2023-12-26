import * as React from 'react';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import Button from '@mui/material/Button';
import { Box, Stack } from '@mui/system';
import { Typography } from '@mui/material';

// Augment the palette to include an ochre color

// Update the Button's color options to include an ochre option


const theme = createTheme({
  palette: {
    ochre: {
      main: '#E3D026',
      light: '#E9DB5D',
      dark: '#A29415',
      contrastText: '#242105',
    },
  },
});

export default function Dresscolor() {
  return (
    <ThemeProvider theme={theme}>
      <Stack gap={8} alignItems="center">
        <Stack direction="row" gap={4}>
          <Stack alignItems="center">
            <Typography variant="body2">Pink</Typography>
            <Box sx={{ bgcolor: 'pink', width: 40, height: 40 ,borderRadius:50 }} />
          </Stack>
          <Stack alignItems="center">
            <Typography variant="body2">Blue</Typography>
            <Box sx={{ bgcolor: 'skyblue', width: 40, height:40 ,borderRadius:50 }} />
          </Stack>
          <Stack alignItems="center">
            <Typography variant="body2">Red</Typography>
            <Box sx={{ bgcolor: 'red', width: 40, height: 40 ,borderRadius:50 }} />
          </Stack>
        </Stack>
      </Stack>
    </ThemeProvider>
  );
}
