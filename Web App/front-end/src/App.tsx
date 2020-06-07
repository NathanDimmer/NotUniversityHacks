import React from "react";
import "./App.css";
import {
  AppBar,
  Toolbar,
  IconButton,
  Typography,
  Button,
  Box,
} from "@material-ui/core";
import { ResponsiveLine } from "nivo";

const App = ({}) => {
  let data = [
    {
      id: "Sink 1",
      data: [
        { x: "0:00", y: 2 },
        { x: "1:00", y: 1 },
        { x: "2:00", y: 2 },
        { x: "3:00", y: 3 },
        { x: "4:00", y: 1 },
        { x: "5:00", y: 15 },
        { x: "6:00", y: 13 },
        { x: "7:00", y: 9 },
        { x: "8:00", y: 11 },
        { x: "9:00", y: 7 },
        { x: "10:00", y: 6 },
        { x: "11:00", y: 8 },
        { x: "12:00", y: 16 },
        { x: "13:00", y: 8 },
        { x: "14:00", y: 6 },
        { x: "15:00", y: 5 },
        { x: "16:00", y: 7 },
        { x: "17:00", y: 6 },
        { x: "18:00", y: 13 },
        { x: "19:00", y: 10 },
        { x: "20:00", y: 6 },
        { x: "21:00", y: 12 },
        { x: "22:00", y: 3 },
        { x: "23:00", y: 1 },
        { x: "24:00", y: 2 },
      ],
    },
  ];

  return (
    <div className="App">
      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6">Smart Faucet</Typography>
        </Toolbar>
      </AppBar>
      <Box style={{ height: "75vh", marginTop: "10vh" }}>
        <ResponsiveLine
          data={data}
          margin={{ top: 50, right: 110, bottom: 50, left: 60 }}
          xScale={{ type: "linear" }}
          yScale={{
            type: "linear",
            min: "auto",
            max: "auto",
            stacked: true,
            reverse: false,
          }}
          axisTop={null}
          axisRight={null}
          axisBottom={{
            orient: "bottom",
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "Time of Day",
            legendOffset: 36,
            legendPosition: "middle",
          }}
          axisLeft={{
            orient: "left",
            tickSize: 5,
            tickPadding: 5,
            tickRotation: 0,
            legend: "Water Use",
            legendOffset: -40,
            legendPosition: "middle",
          }}
          colors={{ scheme: "paired" }}
          lineWidth={5}
          pointSize={10}
          pointColor={{ theme: "background" }}
          pointBorderWidth={2}
          pointBorderColor={{ from: "serieColor" }}
          pointLabel="y"
          pointLabelYOffset={-12}
          enableArea={true}
          useMesh={true}
          legends={[
            {
              anchor: "bottom-right",
              direction: "column",
              justify: false,
              translateX: 100,
              translateY: 0,
              itemsSpacing: 0,
              itemDirection: "left-to-right",
              itemWidth: 80,
              itemHeight: 20,
              itemOpacity: 0.75,
              symbolSize: 12,
              symbolShape: "circle",
              symbolBorderColor: "rgba(0, 0, 0, .5)",
              effects: [
                {
                  on: "hover",
                  style: {
                    itemBackground: "rgba(0, 0, 0, .03)",
                    itemOpacity: 1,
                  },
                },
              ],
            },
          ]}
        />
      </Box>
    </div>
  );
};

export default App;
