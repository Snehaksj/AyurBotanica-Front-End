import styles from "./Page_css/About.module.css";
import Navbar from "../Components/NavigationBar/Navbar.jsx";
import Banner from "../Components/Banner/Banner.jsx";
export default function About() {
  return (
    <div className={styles.about}>
      <Navbar />
      <Banner></Banner>
    </div>
  );
}
