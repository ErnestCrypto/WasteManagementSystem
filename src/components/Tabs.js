import { StyleSheet } from "react-native";
import React from "react";
import styled from "styled-components/native";
import { secondaryColor } from "../helpers/Variables";

const Tab = ({ name }) => {
  return (
    <StyledTab activeOpacity={0.8}>
      <StyledTabText>{name}</StyledTabText>
    </StyledTab>
  );
};

const Tabs = ({ name, tabs }) => {
  return (
    <StyledTabs>
      <StyledTabsText>{name}</StyledTabsText>
      <StyledTabsView>
        {tabs.map((tab, index) => (
          <Tab name={tab} key={index} />
        ))}
      </StyledTabsView>
    </StyledTabs>
  );
};

export default Tabs;

const styles = StyleSheet.create({});

const StyledTabs = styled.View`
  flex-direction: row;
  align-items: center;
  justify-content: space-between;
`;

const StyledTabsView = styled.View`
  flex-direction: row;
  justify-content: space-evenly;
  align-items: center;
  flex: 1;
`;

const StyledTabsText = styled.Text`
  font-size: 15px;
  text-transform: capitalize;
  color: ${secondaryColor};
`;

const StyledTab = styled.TouchableOpacity`
  border-radius: 100px;
`;

const StyledTabText = styled.Text`
  font-size: 12px;
  text-transform: capitalize;
`;
