import { StyleSheet } from "react-native";
import React from "react";
import styled from "styled-components/native";
import { colorWhite, defaultColor, primaryColor } from "../helpers/Variables";
import { AddSquare } from "iconsax-react-native";

const Buttons = ({ type, text, press }) => {
  return (
    <StyledButton onPress={press} activeOpacity={0.9} type={type}>
      <StyledText type={type}>{text}</StyledText>
    </StyledButton>
  );
};

export const AddButton = () => {
  return (
    <StyledAddButton activeOpacity={0.9}>
      <StyledAddText>new</StyledAddText>
      <AddSquare size="24" color={colorWhite} />
    </StyledAddButton>
  );
};

export default Buttons;

const StyledButton = styled.TouchableOpacity`
  width: 260px;
  justify-content: center;
  align-items: center;
  padding: 15px 40px;
  background-color: ${({ type }) =>
    type === "primary" ? primaryColor : colorWhite};
  border-radius: 5px;
`;

const StyledText = styled.Text`
  text-transform: ${({ type }) =>
    type === "primary" ? "uppercase" : "capitalize"};
  font-weight: ${({ type }) => (type === "primary" ? "700" : "300")};
  font-size: ${({ type }) => (type === "primary" ? "20px" : "14px")};
  color: ${({ type }) => (type === "primary" ? colorWhite : defaultColor)};
`;

const StyledAddButton = styled.TouchableOpacity`
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
  width: 120px;
  background-color: ${primaryColor};
  padding: 12px 25px;
  border-radius: 10px;
`;

const StyledAddText = styled.Text`
  color: ${colorWhite};
  text-transform: capitalize;
  font-size: 18px;
`;
