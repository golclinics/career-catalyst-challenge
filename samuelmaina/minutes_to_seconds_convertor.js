
const assert= require('assert');
const multiplier= 60;

//The upperlimit must be divided by multiplier since the function is returning the 
//minutes*multiplier.if the upperlimit is just the max value then multiplying  it by multiplier
//would cause an overflow.
const upperLimit= Number.MAX_VALUE/multiplier;

//assuming that the minutes that can be converted in the real world are
//only non-negative.
const lowerLimit=0;


function minutesToSecondsConverter(minutes){
    if(typeof minutes !== 'number') throw new Error("Minutes must be numeric.");
    if(!(minutes>=lowerLimit && minutes<=upperLimit)){
        throw new Error("Minutes must be non-negative and must be less than or equal to " + upperLimit);
    }
    return minutes* multiplier;
}


//should throw for non-numeric inputs
const nonNumeric= '5';
let expectedError= "Minutes must be numeric.";


assert.throws(()=>{
    minutesToSecondsConverter(nonNumeric);
},constructErrorObjectFromMessage(expectedError));



//Applying Boundary value analysis Testing

const deltaValue=Number.EPSILON;

//test to see that it throw when minutes are lower than lowerlimit.
expectedError= "Minutes must be non-negative and must be less than or equal to " + upperLimit;
assert.throws(()=>{
    minutesToSecondsConverter(lowerLimit-deltaValue);
},constructErrorObjectFromMessage(expectedError));



//should not throw exactly at lowerLimit 
assert.doesNotThrow(()=>{
    minutesToSecondsConverter(lowerLimit);
});


//should not throw exactly at UpperLimit
assert.doesNotThrow(()=>{
    minutesToSecondsConverter(upperLimit);
});


//should throw when upper limit is exceeded.
assert.throws(()=>{
    minutesToSecondsConverter(upperLimit + deltaValue);
},constructErrorObjectFromMessage (expectedError));



//had to construct the function since , the interpreter is complaining that 
//the error message and the Error are the same.
function constructErrorObjectFromMessage(msg){
    return new Error(msg);
}