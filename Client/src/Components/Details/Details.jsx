import React from "react";

export default function Details({ data }) {
  return (
    <div>
      <h2>Details Page</h2>
      {data.details.map((item, index) => (
        <div key={index}>
          <p>Name: {item.name}</p>
          <p>Percentage: {item.percentage}</p>
        </div>
      ))}
    </div>
  );
}
