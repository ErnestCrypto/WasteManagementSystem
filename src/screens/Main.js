import { StyleSheet, Text, View } from "react-native";
import React from "react";
import styled from "styled-components/native";
import { Location, Clock, Diamonds } from "iconsax-react-native";
import {
  welcomeMain,
  welcomeSub,
  secondaryColor,
  primaryColor,
  colorWhite,
  StyledContainer,
  StyledHeader,
  StyledHeaderText,
} from "../helpers/Variables";

const Main = () => {
  return (
    <StyledMain>
      <StyledWelcome>
        <StyledWelcomeText>
          <Text style={welcomeMain}>Hi, Nana Yaw</Text>
          <Text style={welcomeSub}>Welcome back!</Text>
        </StyledWelcomeText>
      </StyledWelcome>
      <StyledUserLocation>
        <View style={styles.location}>
          <Location size="16" color={secondaryColor} />
          <Text style={styles.locationText}>22 amankani avenue</Text>
        </View>
      </StyledUserLocation>
      <StyledUserData>
        <View style={styles.userData}>
          <StyledTitle>
            <Text
              style={[
                styles.userDataText,
                { fontSize: 18, textTransform: "capitalize" },
              ]}
            >
              next pickup
            </Text>
          </StyledTitle>
          <StyledDays>
            <Text
              style={[
                styles.userDataText,
                { fontSize: 60, fontWeight: "bold" },
              ]}
            >
              3 days
            </Text>
          </StyledDays>
          <StyledAddons>
            <View style={styles.addons}>
              <View style={styles.iconHolder}>
                <Location size="24" color={primaryColor} />
              </View>
              <Text style={[styles.userDataText]}>Adenta</Text>
            </View>
            <View style={styles.addons}>
              <View style={styles.iconHolder}>
                <Clock size="24" color={primaryColor} />
              </View>
              <Text style={[styles.userDataText]}>Morning</Text>
            </View>
            <View style={styles.addons}>
              <View style={styles.iconHolder}>
                <Diamonds size="24" color={primaryColor} />
              </View>
              <Text style={[styles.userDataText]}>Basic</Text>
            </View>
          </StyledAddons>
        </View>
      </StyledUserData>
      <StyledActivity>
        <StyledActivityHeader>
          <Text style={styles.recentText}>recent activities</Text>
        </StyledActivityHeader>
        <StyledActivityData>
          <Text>No recent activities</Text>
        </StyledActivityData>
      </StyledActivity>
    </StyledMain>
  );
};

export default Main;

const styles = StyleSheet.create({
  location: {
    flexDirection: "row",
    justifyContent: "space-evenly",
    width: "45%",
  },
  locationText: {
    color: secondaryColor,
  },

  userData: {
    backgroundColor: primaryColor,
    width: "100%",
    height: "80%",
    borderRadius: 10,
    overflow: "hidden",
  },
  userDataText: {
    color: colorWhite,
  },
  iconHolder: {
    backgroundColor: colorWhite,
    justifyContent: "center",
    alignItems: "center",
    width: 50,
    height: 50,
    borderRadius: 50,
  },
  addons: {
    justifyContent: "space-around",
    alignItems: "center",
  },
  recentText: {
    color: secondaryColor,
    textTransform: "capitalize",
    fontSize: 18,
  },
});

const StyledMain = styled(StyledContainer)``;

const StyledWelcome = styled(StyledHeader)``;

const StyledWelcomeText = styled(StyledHeaderText)``;

const StyledUserLocation = styled.View`
  flex: 0 0 10%;
  flex-direction: row;
  align-items: center;
`;

const StyledUserData = styled.View`
  flex: 0 0 45%;
  justify-content: center;
  align-items: center;
`;

const StyledTitle = styled.View`
  flex: 0 0 20%;
  justify-content: center;
  align-items: center;
`;

const StyledDays = styled.View`
  flex: 0 0 35%;
  justify-content: center;
  align-items: center;
`;

const StyledAddons = styled.View`
  flex: 1;
  flex-direction: row;
  justify-content: space-around;
  align-items: center;
`;

const StyledActivity = styled.View`
  flex: 1;
`;

const StyledActivityHeader = styled.View`
  flex: 0 0 12%;
`;

const StyledActivityData = styled.View`
  flex: 1;
  justify-content: space-evenly;
  align-items: center;
`;
