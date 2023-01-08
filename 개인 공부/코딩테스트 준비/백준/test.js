const input = require("fs")
  .readFileSync("example.txt")
  .toString()
  .trim()
  .split(/\s/);

console.log(input);
