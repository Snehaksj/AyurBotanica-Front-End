const express = require("express");
const multer = require("multer");
// Import the cors package
const cors = require("cors");

const app = express();
const port = 3000;

// Use cors middleware to enable CORS
app.use(cors());

// Set up multer to handle multipart/form-data
const upload = multer({ dest: "uploads/" });

// Route for handling the image upload and returning the dummy prediction
app.post("/predict", upload.single("image"), (req, res) => {
  // Dummy processing (replace this with your actual image processing logic)
  // In this example, we'll just return a dummy prediction
  const dummyPrediction = [
    [0.7, "Coffee"],
    [0.6, "Beetle Leaf"],
    [0.5, "Papaya"],
    [0.2, "Aloe Vera"],
    [0.1, "Lemon"],
  ]; // Example prediction result

  // You would typically process the image here and generate your prediction

  // Return the prediction in JSON format
  res.json({ pred: dummyPrediction });
});

// Start the server
app.listen(port, () => {
  console.log(`Dummy API server listening at http://localhost:${port}`);
});
