import { StyleSheet, Text, View } from "react-native";
import React from "react";
import styled from "styled-components/native";
import { SafeAreaView } from "react-native-safe-area-context";

const Home = () => {
  return (
    <SafeAreaView>
      <View>
        <Text>This is the home page</Text>
      </View>
    </SafeAreaView>
  );
};

export default Home;
