import { StyleSheet, Text } from "react-native";
import React from "react";
import { SafeAreaView } from "react-native-safe-area-context";
import {
  defaultViewWithoutPadding,
  StyledInputContainer,
  StyledLowerHeader,
  StyledMainText,
  StyledSubText,
  StyledUpperHeader,
  StyledUpperText,
  textLower,
} from "../helpers/Variables";
import Buttons from "../components/Buttons";
import Input from "../components/Input";

const Signin = ({ navigation }) => {
  return (
    <SafeAreaView style={defaultViewWithoutPadding}>
      <StyledUpperHeader>
        <StyledUpperText>
          <StyledMainText>Let's keep your home clean!</StyledMainText>
          <StyledSubText>
            Continue to your account to keep your home clean
          </StyledSubText>
        </StyledUpperText>
        <StyledInputContainer>
          <Input placeholder="Email address" />
          <Input placeholder="Password" />
        </StyledInputContainer>
      </StyledUpperHeader>
      <StyledLowerHeader>
        <Buttons
          type="primary"
          text="sign in"
          press={() => navigation.navigate("Dashboard")}
        />
        <Buttons
          type="secondary"
          text="don't have an account?"
          press={() => navigation.navigate("Signup")}
        />
        <Text style={textLower}>
          We can all assist to recycle and reduce global warming if we work
          together. Waste disposal is critical to our environment's well-being.
        </Text>
      </StyledLowerHeader>
    </SafeAreaView>
  );
};

export default Signin;

const styles = StyleSheet.create({});
