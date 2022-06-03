import { StyleSheet, Text, View, TouchableOpacity, Image } from "react-native";
import React from "react";
import styled from "styled-components/native";
import {
  primaryColor,
  StyledContainer,
  StyledHeader,
  StyledHeaderText,
  welcomeSub,
} from "../helpers/Variables";
import { ArrowCircleUp, Clock, Diamonds, Location } from "iconsax-react-native";
import ProfilePic from "../assets/images/profile-pic.jpg";

const Profile = () => {
  return (
    <StyledProfile>
      <StyledWelcome>
        <StyledWelcomeText>
          <Text style={welcomeSub}>Profile</Text>
        </StyledWelcomeText>
      </StyledWelcome>
      <View>
        <View>
          <View>
            <Image
              style={{
                width: 100,
                height: 100,
                borderRadius: 100,
                borderWidth: 2,
                borderColor: primaryColor,
              }}
              source={ProfilePic}
            />
          </View>
          <View>
            <Text>nana yaw yeboah</Text>
          </View>
          <View>
            <View>
              <Location size="24" color={primaryColor} />
              <Text>adenta</Text>
            </View>
            <View>
              <Clock size="24" color={primaryColor} />
              <Text>wednesday</Text>
            </View>
            <View>
              <Diamonds size="24" color={primaryColor} />
              <Text>basic</Text>
            </View>
          </View>
          <View>
            <TouchableOpacity activeOpacity={0.95}>
              <Text>edit profile</Text>
            </TouchableOpacity>
          </View>
        </View>
        <View>
          <View>
            <Text>subscription</Text>
          </View>
          <View>
            <View>
              <View>
                <View>
                  <Text>current plan</Text>
                  <Text>basic</Text>
                </View>
                <View>
                  <Text>duration</Text>
                  <Text>june-july</Text>
                </View>
              </View>
              <View>
                <View>
                  <Text>duration</Text>
                  <Text>duration</Text>
                </View>
                <View>
                  <Text>june - july</Text>
                </View>
              </View>
            </View>
          </View>
          <View>
            <TouchableOpacity>
              <Text>
                upgrade
                <ArrowCircleUp size="32" color={primaryColor} />
              </Text>
            </TouchableOpacity>
          </View>
        </View>
      </View>
    </StyledProfile>
  );
};

export default Profile;

const styles = StyleSheet.create({});

const StyledProfile = styled(StyledContainer)``;

const StyledWelcome = styled(StyledHeader)``;

const StyledWelcomeText = styled(StyledHeaderText)``;
