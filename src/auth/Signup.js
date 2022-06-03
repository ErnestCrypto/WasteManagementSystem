import { Text, KeyboardAvoidingView } from "react-native";
import React from "react";
import styled from "styled-components/native";
import { SafeAreaView } from "react-native-safe-area-context";
import {
  colorWhite,
  defaultColor,
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
        <KeyboardAvoidingView style={{ flex: 1 }} behavior="padding">
          <StyledInputContainer>
            <InputField
              placeholderColor={defaultColor}
              placeholder="Username"
            />
            <InputField
              placeholderColor={defaultColor}
              keyboardType="email-address"
              placeholder="Email address"
            />
            <InputField
              placeholderColor={defaultColor}
              secureTextEntry={true}
              placeholder="Password"
            />
            <InputField
              placeholderColor={defaultColor}
              secureTextEntry={true}
              placeholder="Confirm Password"
            />
          </StyledInputContainer>
        </KeyboardAvoidingView>
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

const InputField = styled.TextInput`
  background-color: ${colorWhite};
  width: 280px;
  padding: 15px 30px;
  border-radius: 10px;
`;
