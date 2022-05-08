import { StyleSheet, Text, View } from "react-native";
import React from "react";
import styled from "styled-components";
import { SafeAreaView } from "react-native-safe-area-context";

const Dashboard = () => {
  return (
    <SafeAreaView>
      <StyledUserInfo></StyledUserInfo>
      <StyledUserDasboard></StyledUserDasboard>
      <StyledUserRecents></StyledUserRecents>
      <View></View>
    </SafeAreaView>
  );
};

export default Dashboard;

const styles = StyleSheet.create({});

const StyledUserInfo = styled.View``;

const StyledUserDasboard = styled.View``;

const StyledUserRecents = styled.View``;
