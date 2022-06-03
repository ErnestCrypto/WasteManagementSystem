import { StyleSheet } from "react-native";
import React, { useState } from "react";
import styled from "styled-components/native";
import { secondaryColor } from "../helpers/Variables";
import Tab from "./Tab";

const Tabs = ({ title, tabs }) => {
  return (
    <StyledTabs>
      <StyledTabsText>{title}</StyledTabsText>
      <StyledTabsView>
        {tabs.map((tab, index) => (
          <Tab key={index} name={tab} />
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
  flex: 0.4;
`;
