//function that takes integer minutes as a parameter//
function myFunction(minutes) {
  //only integer values are passed here//
  if (Number.isInteger(minutes)) {
    return minutes * 60;
  }
}

module.exports = myFunction;
