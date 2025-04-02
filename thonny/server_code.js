const express = require('express');
const axios = require('axios');

const app = express();
const PORT = 3000;
const FLASK_SERVER = "http://raspberrypi:5000/video_feed";  // Change to Flask's IP

app.get('/stream', async (req, res) => {
    try {
        const response = await axios({
            method: 'get',
            url: FLASK_SERVER,
            responseType: 'stream'
        });

        res.setHeader('Content-Type', 'multipart/x-mixed-replace; boundary=frame');
        response.data.pipe(res);  // Pipe Flask stream to client

    } catch (error) {
        console.error("Error fetching video stream:", error);
        res.status(500).send("Error fetching video stream.");
    }
});

app.listen(PORT, () => console.log(`Node.js server running on http://localhost:${PORT}/stream`));



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

// // server.js (Node.js backend)
// const express = require('express');
// const axios = require('axios');
// const app = express();
// const port = 5000;
// // This will be the data to send to the Raspberry Pi
// const dataToSend = { message: "Hello, Raspberry Pi!" };
// app.get('/send-data', async (req, res) => {
//   try {
//     // Send the data to Raspberry Pi using a POST request
//     const raspberryPiUrl = 'http://raspberrypi:5000/receive_data'; // Change to your Raspberry Pi IP
//     const response = await axios.post(raspberryPiUrl, dataToSend);
//     res.status(200).send('Data sent to Raspberry Pi!');
//   } catch (error) {
//     res.status(500).send('Failed to send data to Raspberry Pi.');
//   }
// });
// app.listen(port, () => {
//   console.log(`Node.js server running at http://localhost:${port}`);
// });