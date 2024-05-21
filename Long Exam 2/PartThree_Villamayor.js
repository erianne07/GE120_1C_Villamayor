import React from 'react'
import {Picker} from '@react-native-picker/picker';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';


export default function App() {

  const [outputValue, setOuputValue] = React.useState('---');
  const [inputValue, setInputValue] = React.useState('Place Value Here...');
  const [inputCase, setInputCase] = React.useState("Select Case");
  
/*
Given the following specifications for this design, what React Native components do you suggest are needed to develop this app?
- given the designs specifications, I think the React Native components that is best to use to develop this app are picker, for the change in azimuth to bearing
and vice versa, TextInput, so that you will be able to input the values that you will be requiring, button to initialize the conversion of azimuth to bearing and 
vice versa.
*/
  
  function convertValue(value){
    /*
    Compute for the DMS bearing of a given angle.

    Input:
    azimtuh - float

    Output:
    bearing - string
    */
    if (inputCase == "1") {
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
if (inputCase == "1") {
    var degrees = Math.floor(value)
    var minutes = Math.floor((value-degrees)*60)
    var seconds = Math.round((value-degrees-(minutes/60))*3600)
   
    
    var output = degrees.toString().concat("-", minutes.toString(),"-", seconds.toString())%360
    setOuputValue(output)
}
else {
  var elements = value.split("-")
  var output = parseFloat(elements[0])+ parseFloat(elements[1]/60) + parseFloat(elements[2]/3600)
  setOuputValue(output)
}(
    <View style={styles.box}>
      <View style={styles.sherly}>
        <Text style={styles.titleText}>WELCOME TO AZIMUTH TO BEARING CONVERTER!</Text>
      </View>

      <View style={styles.albert}>
        <View style={styles.albert1}>
          <Text>Input Case</Text>
          <Picker
            selectedValue={inputCase}
            onValueChange={(itemValue, itemIndex) =>
              setInputCase(itemValue)
            }>
            <Picker.Item label="Azimuth to Bearing" value="1" />
            <Picker.Item label="Bearing to Azimuth" value="2" />
          </Picker>
        </View>

        <View style={styles.albert2}>
        <TextInput
        style={styles.input}
        onChangeText={setInputValue}
        value={inputValue}
        />
          <Button
            title="Convert"
            onPress={() => convertToBearing(inputValue)}
          />   
        </View>
      </View>


      <View style={styles.liam}>
        <Text style={styles.titleText}>Output:</Text>
        <Text style={styles.titleText}>{outputValue}</Text>
      </View>
      
      <View style={styles.louis}>
      
      
      </View>

    </View>
    );
}
}

const styles = StyleSheet.create({
  box: {
    flex: 1,
    backgroundColor: '#22311d',
    alignItems: 'center',
    justifyContent: 'center',
  },
  louis: {
    width: '100%',
    height: '20%',
    alignItems: 'center',
    justifyContent: 'center'
  },
  albert: {
    width: '100%',
    height: '30%',
    alignItems: 'center',
    justifyContent: 'center'
  },
  albert1: {
   flexDirection:'column',
   width: '100%',
   height: '50%',
  },
  albert2: {
    flex: 1,
    width: '100%',
    height: '50%',
   },
  liam: {
    width: '100%',
    height: '30%',
    alignItems: 'center',
    justifyContent: 'center'
  },
  sherly: {
    width: '100%',
    height: '20%',
    alignItems: 'center',
    justifyContent: 'center'
  },
  titleText: {
    fontSize: 24,
    fontWeight: '600',
  },
  input: {
    height: '50%',
    width: '70%',
    fontSize: 24,
    color: 'black',
  },
});
