#!/usr/bin/node
const request = require('request');
request(process.argv[2], function (error, response, body) {
  if (error) console.log(error);
  else if (response.statusCode === 200) {
    const films = JSON.parse(body).results;
    let count = 0;
    for (const film in films) {
      const characters = films[film].characters;
      for (const char in characters) {
        if (characters[char].includes('18')) {
          count++;
        }
      }
    }
    console.log(count);
  }
});
