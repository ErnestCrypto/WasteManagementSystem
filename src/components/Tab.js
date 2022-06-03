import { StyleSheet } from "react-native";
import React, { useState } from "react";
import styled from "styled-components/native";
import { colorWhite, defaultColor, primaryColor } from "../helpers/Variables";

const Tab = ({ name }) => {
  const [active, setActive] = useState(false);

  return (
    <StyledTab
      activeOpacity={0.8}
      onPress={() => setActive(!active)}
      style={[
        active
          ? {
              backgroundColor: primaryColor,
              paddingHorizontal: 12,
              paddingVertical: 8,
            }
          : null,
        {
          shadowColor: defaultColor,
          shadowOffset: {
            width: 0,
            height: 2,
          },
          shadowOpacity: 0.23,
          shadowRadius: 2.62,
          elevation: 4,
          borderRadius: 50,
        },
      ]}
    >
      <StyledTabText style={{ color: active ? colorWhite : defaultColor }}>
        {name}
      </StyledTabText>
    </StyledTab>
  );
};

export default Tab;

const styles = StyleSheet.create({});

const StyledTab = styled.TouchableOpacity`
  background-color: ${colorWhite};
  justify-content: center;
  align-items: center;
  padding: 5px 12px;
`;

const StyledTabText = styled.Text`
  font-size: 12px;
  text-transform: capitalize;
`;
