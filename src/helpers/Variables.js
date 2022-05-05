import styled from "styled-components/native";

export const appBackgroundColor = "#F5F5F5";
export const primaryColor = "#4BB35E";
export const primaryColorLight = "#D7F9DE";
export const defaultColor = "#999999";
export const colorWhite = "#fff";

export const defaultView = {
  flex: 1,
  backgroundColor: appBackgroundColor,
  paddingHorizontal: 20,
};

export const defaultViewWithoutPadding = {
  flex: 1,
  backgroundColor: appBackgroundColor,
};

export const textLower = {
  paddingHorizontal: 30,
  color: primaryColor,
  textAlign: "center",
};

export const StyledUpperHeader = styled.View`
  flex: 0 0 58%;
  display: flex;
  background-color: ${primaryColor};
  justify-content: space-evenly;
  align-items: center;
`;

export const StyledLowerHeader = styled.View`
  flex: 1;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  position: relative;
`;
