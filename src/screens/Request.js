import { StyleSheet, Text } from "react-native";
import React from "react";
import styled from "styled-components/native";
import {
  welcomeSub,
  StyledContainer,
  StyledHeader,
  StyledHeaderText,
} from "../helpers/Variables";
import { AddButton } from "../components/Buttons";
import Tabs from "../components/Tabs";

const Request = () => {
  return (
    <StyledRequest>
      <StyledWelcome>
        <StyledWelcomeText>
          <Text style={welcomeSub}>Request</Text>
        </StyledWelcomeText>
      </StyledWelcome>
      <StyledRequestNew>
        <AddButton />
      </StyledRequestNew>
      <Tabs name="all requests" tabs={["active", "success", "rejected"]} />
    </StyledRequest>
  );
};

export default Request;

const styles = StyleSheet.create({});

const StyledRequest = styled(StyledContainer)``;

const StyledWelcome = styled(StyledHeader)``;

const StyledWelcomeText = styled(StyledHeaderText)``;

const StyledRequestNew = styled.View`
  flex: 0.3;
  justify-content: center;
  align-items: center;
`;
