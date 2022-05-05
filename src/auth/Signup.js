import { StyleSheet, Text, View } from "react-native";
import React from "react";
import { SafeAreaView } from "react-native-safe-area-context";
import styled from "styled-components/native";
import {
  defaultViewWithoutPadding,
  StyledLowerHeader,
  StyledUpperHeader,
  textLower,
} from "../helpers/Variables";
import Buttons from "../components/Buttons";

const Signup = ({ navigation }) => {
  return (
    <SafeAreaView style={defaultViewWithoutPadding}>
      <StyledUpperHeader></StyledUpperHeader>
      <StyledLowerHeader>
        <Buttons type="primary" text="create account" />
        <Buttons
          press={() => navigation.navigate("Signin")}
          type="secondary"
          text="Already joined? Continue"
        />
        <Text style={textLower}>
          We can all assist to recycle and reduce global warming if we work
          together. Waste disposal is critical to our environment's well-being.
        </Text>
      </StyledLowerHeader>
    </SafeAreaView>
  );
};

export default Signup;

const styles = StyleSheet.create({});
