/*
GE 120
Erianne Villamayor
2023-11100

Machine Exercise 3
*/


function getLatitude(distance, azimuth){

    /*
    Compute for the Latitude of a given line.

    Input:
    distance - float
    azimuth - float

    Output:
    Latitude - float
    */
    if (azimuth % 180 == 90) {return 0} else {
    return (-distance * Math.cos(azimuth * Math.Pi / 180.0))}
}

function getDeparture(distance, azimuth){
    /*
    Compute for the departure of a given line.

    Input:
    distance - float
    azimuth - float

    Output:
    Departure - float
    */

    if (azimuth % 180 == 0) {return 0} else {
        return (-distance * Math.cos(azimuth * Math.Pi / 180.0))}
}

function azimuthToBearing(azimuth){

    /*
    Compute for the DMS bearing of a given angle.

    Input:
    azimtuh - float

    Output:
    bearing - string
    */

    var azimuth = azimuth%360;
    var bearing;

    if (azimuth > 0 && azimuth < 90){
        bearing = 'S '.concat(azimuth.toPrecision(5).toString(), ' W')
    } else if (azimuth > 90 && azimuth <180){
        bearing = 'N '.concat((180-azimuth).toPrecision(5).toString(), ' W')
    } else if (azimuth > 180 && azimuth < 270){
        bearing = 'N '.concat((azimuth - 180).toPrecision(5).toString(), ' E')
    } else if (azimuth > 270  && azimuth <360){
        bearing = 'S '.concat((360 - azimuth).toPrecision(5).toString(), ' E')
    } else if (azimuth == 0){
        bearing = "DUE SOUTH"
    } else if (azimuth == 90){
        bearing = "DUE WEST"
    } else if (azimuth == 180){
        bearing = "DUE NORTH"
    } else if (azimuth == 270){
        bearing == "DUE EAST"
    } else {
        bearing == "EWAN KO"
    }
    return bearing
}

//Sentinel Controlled Loop
var data = [
    [13.23, 124.795],
    [15.57, 14.143],
    [43.36, 270.000],
    [23.09, 188.169],
    [10.99, 180.000],
    [41.40, 50.562]
]
var lines = []
var sumLat = 0
var sumDep = 0
var sumDist = 0


for (var i = 0; i < data.length; i++){
    //console.log(data[i])

    let line = data[i]
    let distance = line[0]
    let azimuth = line[1]

    let bearing = azimuthToBearing(azimuth)
    let lat = getLatitude(distance, azimuth)
    let dep = getDeparture(distance, azimuth)

    sumLat += lat
    sumDep += dep
    sumDist += distance

    lines.push([(i+i), distance, bearing, lat, dep])
}

// console.log(lines)
// console.log("\n\n")
console.log("LINE NO.".padEnd(10), "DISTANCE".padEnd(10), "BEARING".padEnd(15), "LATITUDE".padEnd(10), "DEPARTURE".padEnd(10))
for (var line of lines){
    console.log(
        line[0].toString().padEnd(10),
        line[1].toString().padEnd(10), 
        line[2].padEnd(15), 
        line[3].toPrecision(5).toString().padEnd(10), 
        line[4].toPrecision(5).toString().padEnd(10)
    )    
}

console.log("SUMMATION OF LAT:", sumLat.toPrecision(5))
console.log("SUMMATION OF DEP:", sumDep.toPrecision(5))
console.log("SUMMATION OF DIST:", sumDist.toPrecision(5))

lec = Math.sqrt(sumLat**2 + sumDep**2)

console.log("LEC", lec.toPrecision(5))

rec = sumDist/lec

console.log("1:  ", Math.floor(rec/1000)*1000)


console.log("------END-------")
