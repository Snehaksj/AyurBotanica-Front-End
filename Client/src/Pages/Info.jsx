import React from "react";
import { useParams } from "react-router-dom";
import Background from "../Components/Background/Background";
import Navbar from "../Components/NavigationBar/Navbar";
import Details from "../Components/Details/Details"; // Import Details component

export default function Info() {
  const {
    name1,
    percentage1,
    name2,
    percentage2,
    name3,
    percentage3,
    name4,
    percentage4,
    name5,
    percentage5,
  } = useParams();

  // Create an object containing the parameters
  const data = {
    details: [
      { name: name1, percentage: percentage1 },
      { name: name2, percentage: percentage2 },
      { name: name3, percentage: percentage3 },
      { name: name4, percentage: percentage4 },
      { name: name5, percentage: percentage5 },
    ],
  };

  return (
    <Background>
      <Navbar />
      <Details data={data} />
    </Background>
  );
}
