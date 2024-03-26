// Importing necessary modules from k6
import http from 'k6/http'; // Importing HTTP module for making HTTP requests
import { sleep } from 'k6'; // Importing sleep function for adding delays

// Options configuration for k6 test
export let options = {
    vus: 20,         // Number of virtual users to simulate
    duration: '10s',    // Duration of the test (1 minute)
};

// Main function representing the test scenario
export default function () {
    // Making an HTTP GET request to the specified URL
    http.get('http://localhost/reader');
    
    // Adding a sleep delay of 1 second
    sleep(1);
}