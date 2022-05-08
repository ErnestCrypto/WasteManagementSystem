import { StyleSheet, Text, View } from "react-native";
import React from "react";
import styled from "styled-components/native";
import { colorWhite } from "../helpers/Variables";

const Input = ({ placeholder }) => {
  return (
    <StyledInputContainer>
      <InputField placeholder={placeholder} />
    </StyledInputContainer>
  );
};

export default Input;

const StyledInputContainer = styled.View``;

const InputField = styled.TextInput`
  background-color: ${colorWhite};
  width: 280px;
  padding: 15px 30px;
  border-radius: 10px;
`;
