import styles from "./Floatingimage.module.css";
export default function Floatingimage() {
  return (
    <div className={styles.Floatingimage}>
      <div className={styles.blurimg}></div>
      <img src="/fimg.png" alt="" />
      
    </div>
  );
}
