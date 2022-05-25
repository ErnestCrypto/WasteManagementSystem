import styled from "styled-components/native";

export const appBackgroundColor = "#F5F5F5";
export const primaryColor = "#4BB35E";
export const primaryColorDark = "#0E6A41";
export const primaryColorLight = "#D7F9DE";
export const defaultColor = "#999999";
export const defaultColorLight = "#8889A0";
export const colorWhite = "#fff";
export const secondaryColor = "#171A66";

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
  paddingHorizontal: 40,
  color: primaryColor,
  textAlign: "center",
};

export const StyledUpperHeader = styled.View`
  flex: 0 0 58%;
  display: flex;
  background-color: ${primaryColor};
  justify-content: space-around;
  align-items: center;
`;

export const StyledLowerHeader = styled.View`
  flex: 1;
  display: flex;
  justify-content: space-evenly;
  align-items: center;
  position: relative;
`;

export const StyledUpperText = styled.View`
  flex: 0 0 40%;
  text-align: center;
  justify-content: space-evenly;
  align-items: center;
`;

export const StyledMainText = styled.Text`
  color: ${primaryColorDark};
  font-size: 24px;
`;

export const StyledSubText = styled.Text`
  color: ${primaryColorLight};
  font-size: 15px;
  width: 50%;
  padding: 0 20px;
`;

export const StyledInputContainer = styled.View`
  justify-content: space-evenly;
  align-items: center;
  flex: 1;
`;

export const StyledContainer = styled.View`
  position: relative;
  flex: 5;
`;

export const welcomeMain = { color: defaultColorLight, fontSize: 15 };

export const welcomeSub = {
  color: secondaryColor,
  fontSize: 22,
  fontWeight: "bold",
};

export const StyledHeader = styled.View`
  flex-direction: row;
  flex: 0 0 10%;
`;

export const StyledHeaderText = styled.View`
  flex: 0 0 70%;
  justify-content: center;
  justify-content: space-evenly;
`;
