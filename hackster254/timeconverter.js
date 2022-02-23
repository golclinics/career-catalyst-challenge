function myFunction(minutes) {
    if (Number.isInteger(minutes)) {
        var seconds = minutes * 60
        //console.log(seconds)
        return seconds;
    }
    return 'Enter an integer'


}
console.log(myFunction(4))
