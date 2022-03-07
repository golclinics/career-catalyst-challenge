const convert = (minutes) => {
  if (typeof minutes !== 'number') {
    return 'Provide a valid number';
  }
  return minutes * 60;
}

console.log(convert(5)); // 300

console.log(convert(3)); // 180

console.log(convert(2)); // 120
console.log(convert(true)); // Provide a valid number

console.log(convert('5')); // Provide a valid number
