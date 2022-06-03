import { Text, KeyboardAvoidingView } from "react-native";
import React, { useState } from "react";
import { SafeAreaView } from "react-native-safe-area-context";
import {
  defaultColor,
  defaultViewWithoutPadding,
  StyledInputContainer,
  StyledLowerHeader,
  StyledMainText,
  StyledSubText,
  StyledUpperHeader,
  StyledUpperText,
  textLower,
  colorWhite,
} from "../helpers/Variables";
import Buttons from "../components/Buttons";
import { useDispatch } from "react-redux";
import { getUserId } from "../api/api";
import styled from "styled-components/native";

const Signin = ({ navigation }) => {
  const [email, setEmail] = useState();
  const [password, setPassword] = useState();
  const dispatch = useDispatch();

  const handleLogin = () => {
    console.log(email, password);

    if (!(email && password)) {
      return alert("Fill all credentials to continue");
    }

    getUserId(email, password)
      .then((user) => console.log(user))
      .catch((err) => console.log(err));
  };

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
          <KeyboardAvoidingView
            style={{
              flex: 1,
              justifyContent: "space-evenly",
              alignSelf: "center",
            }}
          >
            <InputField
              type="email"
              placeholderColor={defaultColor}
              placeholder="Email address"
              onChangeText={(text) => setEmail(text)}
            />
            <InputField
              secureTextEntry={true}
              type="password"
              placeholderColor={defaultColor}
              placeholder="Password"
              onChangeText={(text) => setPassword(text)}
            />
          </KeyboardAvoidingView>
        </StyledInputContainer>
      </StyledUpperHeader>
      <StyledLowerHeader>
        <Buttons type="primary" text="sign in" press={handleLogin} />
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

const InputField = styled.TextInput`
  background-color: ${colorWhite};
  width: 280px;
  padding: 15px 30px;
  border-radius: 10px;
`;
