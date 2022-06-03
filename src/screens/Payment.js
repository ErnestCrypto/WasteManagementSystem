import { StyleSheet, Text, View } from "react-native";
import React from "react";
import styled from "styled-components/native";
import {
  StyledContainer,
  StyledHeader,
  StyledHeaderText,
  welcomeSub,
} from "../helpers/Variables";
import { AddButton } from "../components/Buttons";
import Tabs from "../components/Tabs";

const Payment = () => {
  return (
    <StyledPayment>
      <StyledWelcome>
        <StyledWelcomeText>
          <Text style={welcomeSub}>Payment</Text>
        </StyledWelcomeText>
      </StyledWelcome>
      <StyledPaymentNew>
        <AddButton />
      </StyledPaymentNew>
      <Tabs title="all receipts" tabs={["all", "success", "rejected"]} />
      <View
        style={{
          flex: 0.8,
          marginTop: 10,
          display: "flex",
          justifyContent: "center",
          alignItems: "center",
        }}
      >
        <Text>No requests made</Text>
      </View>
    </StyledPayment>
  );
};

export default Payment;

const styles = StyleSheet.create({});

const StyledPayment = styled(StyledContainer)``;

const StyledWelcome = styled(StyledHeader)``;

const StyledWelcomeText = styled(StyledHeaderText)``;

const StyledPaymentNew = styled.View`
  flex: 0.3;
  justify-content: center;
  align-items: center;
`;
