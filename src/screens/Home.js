import { StyleSheet, Text, View, Image } from "react-native";
import React from "react";
import styled from "styled-components/native";
import { SafeAreaView } from "react-native-safe-area-context";
import {
  defaultViewWithoutPadding,
  StyledLowerHeader,
  StyledUpperHeader,
  textLower,
} from "../helpers/Variables";
import Buttons from "../components/Buttons";

const Home = ({ navigation }) => {
  return (
    <SafeAreaView
      style={[defaultViewWithoutPadding, { display: "flex", padding: 0 }]}
    >
      <StyledUpperHeader>
        <Image source={require("../assets/images/Recycling-image.png")} />
      </StyledUpperHeader>
      <StyledLowerHeader>
        <Image
          style={{ position: "absolute", top: -20, left: "25%", zIndex: 10 }}
          source={require("../assets/images/wastify-logo.png")}
        />
        <Buttons
          press={() => navigation.navigate("Signin")}
          text="get started"
          type="primary"
        />
        <Text style={textLower}>
          We can all assist to recycle and reduce global warming if we work
          together. Waste disposal is critical to our environment's well-being.
        </Text>
      </StyledLowerHeader>
    </SafeAreaView>
  );
};

export default Home;
