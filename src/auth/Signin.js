import { StyleSheet, Text, View, TextInput } from "react-native";
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

const Signin = ({ navigation }) => {
  return (
    <SafeAreaView style={defaultViewWithoutPadding}>
      <StyledUpperHeader>
        <View>
          <Text>Keep your home clean!</Text>
          <Text>Continue to your account to keep your home clean</Text>
        </View>
        <View>
          <TextInput placeholder="Email address" />
        </View>
        <View>
          <TextInput placeholder="Password" />
        </View>
      </StyledUpperHeader>
      <StyledLowerHeader>
        <Buttons type="primary" text="sign in" />
        <Buttons
          press={() => navigation.navigate("Signup")}
          type="secondary"
          text="don't have an account?"
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
