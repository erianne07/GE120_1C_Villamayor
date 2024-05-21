import React from 'react'
import { Image } from 'expo-image';
import {Picker} from '@react-native-picker/picker';
import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View, Button, TextInput } from 'react-native';


export default function App() {

  const [outputValue, setOuputValue] = React.useState('---');
  const [inputValue, setInputValue] = React.useState('Place Value Here...');
  const [inputCase, setInputCase] = React.useState("Select Case");
  
  const blurhash =
  '|rF?hV%2WCj[ayj[a|j[az_NaeWBj@ayfRayfQfQM{M|azj[azf6fQfQfQIpWXofj[ayj[j[fQayWCoeoeaya}j[ayfQa{oLj?j[WVj[ayayj[fQoff7azayj[ayj[j[ayofayayayj[fQj[ayayj[ayfjj[j[ayjuayj[';

  
  function convertValue(value){
      /*
      Compute for the DMS bearing of a given angle.

      Input:
      azimtuh - float

      Output:
      bearing - string
      */
      if (inputCase == "1") {
          var degrees = Math.floor(value)
          var minutes = Math.floor((value-degrees)*60)
          var seconds = Math.round((value-degrees-(minutes/60))*3600)
          
          var output = degrees.toString().concat("-", minutes.toString(),"-", seconds.toString())
          setOuputValue(output)
      }
      else {
        var elements = value.split("-")
        var output = parseFloat(elements[0])+ parseFloat(elements[1]/60) + parseFloat(elements[2]/3600)
        setOuputValue(output)
      }
  }
  return (
    <View style={styles.box}>
      <View style={styles.pike}>
        <Text style={styles.titleText}>WELCOME TO DMS-DD CONVERTER!</Text>
      </View>

      <View style={styles.keyleth}>
        <View style={styles.keyleth1}>
          <Text>Input Case</Text>
          <Picker
            selectedValue={inputCase}
            onValueChange={(itemValue, itemIndex) =>
              setInputCase(itemValue)
            }>
            <Picker.Item label="DD to DMS" value="1" />
            <Picker.Item label="DMS to DD" value="2" />
          </Picker>
        </View>

        <View style={styles.keyleth2}>
        <TextInput
        style={styles.input}
        onChangeText={setInputValue}
        value={inputValue}
        />
          <Button
            title="Convert"
            onPress={() => convertValue(inputValue)}
          />   
        </View>
      </View>


      <View style={styles.vex}>
        <Text style={styles.titleText}>Output:</Text>
        <Text style={styles.titleText}>{outputValue}</Text>
      </View>
      
      <View style={styles.percy}>
        <Image
          style={styles.image}
          source="https://cdn.pixabay.com/photo/2024/02/28/07/42/european-shorthair-8601492_1280.jpg"
          placeholder={{ blurhash }}
          contentFit="cover"
          transition={1000}
        />
      
      </View>

    </View>
  );
}

const styles = StyleSheet.create({
  box: {
    flex: 1,
    backgroundColor: '#22311d',
    alignItems: 'center',
    justifyContent: 'center',
  },
  percy: {
    width: '100%',
    height: '20%',
    backgroundColor: '#92C7CF',
    alignItems: 'center',
    justifyContent: 'center'
  },
  keyleth: {
    width: '100%',
    height: '30%',
    backgroundColor: '#64CCC5',
    alignItems: 'center',
    justifyContent: 'center'
  },
  keyleth1: {
   flexDirection:'column',
   width: '100%',
   height: '50%',
   backgroundColor: '#D9EDEE'
  },
  keyleth2: {
    flex: 1,
    width: '100%',
    height: '50%',
    backgroundColor: '#AAD7D9'
   },
  vex: {
    width: '100%',
    height: '30%',
    backgroundColor: '#A6CFD1',
    alignItems: 'center',
    justifyContent: 'center'
  },
  pike: {
    width: '100%',
    height: '20%',
    backgroundColor: '#F7FBFC',
    alignItems: 'center',
    justifyContent: 'center'
  },
  titleText: {
    fontSize: 24,
    fontWeight: '600',
  },
  Image: {
    flex: 1,
    width: '100%',
    backgroundColor: '#0553',
  },
  input: {
    height: '50%',
    width: '70%',
    fontSize: 24,
    color: 'black',
  },
});
