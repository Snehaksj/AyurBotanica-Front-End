import React from "react";
import styles from "./Card.module.css";
import { Link } from "react-router-dom";

export default function Card({ data, match }) {
  const { plant_names } = data;
  const { plant_match } = match;

  const getImageSrc = (name) => {
    return `/${name.replace(/\s+/g, "_")}.jpg`;
  };

  const centerIndex = Math.floor(plant_names.length / 2);

  return (
    <div className={styles.card}>
      {plant_names.map((name, index) => {
        const isCenterCard = index === centerIndex;
        const isMiddleCard = Math.abs(index - centerIndex) === 1;
        const cardClass = isCenterCard
          ? styles.centerCard
          : isMiddleCard
          ? styles.middleCard
          : styles.carditems;

        return (
          <Link to={`/Plant/${name}`} key={index} className={cardClass}>
            <img src={getImageSrc(name)} alt={name} />
            <p className={styles.caption}>
              {name}
              <br />
              {plant_match[index]}%
            </p>
          </Link>
        );
      })}
    </div>
  );
}
