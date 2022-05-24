import { Text } from "react-native";
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

const Signup = ({ navigation }) => {
  return (
    <SafeAreaView style={defaultViewWithoutPadding}>
      <StyledUpperHeader>
        <StyledUpperText>
          <StyledMainText>Let's get you started!</StyledMainText>
          <StyledSubText>
            To become a member, first create an account
          </StyledSubText>
        </StyledUpperText>
        <StyledInputContainer>
          <Input placeholder="Username" />
          <Input placeholder="Email address" />
          <Input placeholder="Password" />
          <Input placeholder="Confirm Password" />
        </StyledInputContainer>
      </StyledUpperHeader>
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
