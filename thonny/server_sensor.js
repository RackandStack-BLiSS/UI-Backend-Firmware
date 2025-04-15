const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;

// Replace with your Pi's IP address
const PI_SERVER_URL = "http://raspberrypi:5000/request_data";

app.get('/get_pi_data', async (req, res) => {
  try {
    const response = await axios.get(PI_SERVER_URL);  // Send request to Pi
    console.log("Data received from Pi:", response.data);
    res.json({ message: "Data retrieved from Pi", data: response.data });
  } catch (error) {
    console.error("Error contacting Raspberry Pi:", error.message);
    res.status(500).json({ error: "Failed to retrieve data from Raspberry Pi." });
  }
});

app.listen(PORT, () => {
  console.log(`Computer server running at http://localhost:${PORT}/get_pi_data`);
});

// const axios = require('axios');

// const url = "http://raspberrypi:5000/receive_data";  // Change to your Flask server's IP if needed
// const data = { message: "Hello from Node.js!" };

// axios.post(url, data)
//   .then(response => {
//     console.log("Response from Flask:", response.data);
//   })
//   .catch(error => {
//     console.error("Error sending request:", error);
//   });