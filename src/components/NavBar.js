import { View } from "react-native";
import React from "react";
import styled from "styled-components/native";
import { Link, useLocation } from "react-router-native";
import { Home, Truck, CardPos } from "iconsax-react-native";
import {
  defaultColor,
  primaryColor,
  primaryColorLight,
  secondaryColor,
} from "../helpers/Variables";

const NavBar = () => {
  const { pathname } = useLocation();

  return (
    <StyledNav>
      <StyledNavBar>
        <View>
          <Link to="/" underlayColor="transparent">
            <Home
              size="24"
              color={pathname === "/" ? primaryColor : defaultColor}
            />
          </Link>
        </View>
        <View>
          <Link to="/requests" underlayColor="transparent">
            <Truck
              size="24"
              color={pathname === "/requests" ? primaryColor : defaultColor}
            />
          </Link>
        </View>
        <View>
          <Link to="/payments" underlayColor="transparent">
            <CardPos
              size="24"
              color={pathname === "/payments" ? primaryColor : defaultColor}
            />
          </Link>
        </View>
        <View>
          <Link to="/profile" underlayColor="transparent">
            <StyledProfile active={pathname === "/payments"}></StyledProfile>
          </Link>
        </View>
      </StyledNavBar>
    </StyledNav>
  );
};

export default NavBar;

const StyledNav = styled.View`
  flex: 1;
  justify-content: center;
  align-items: center;
`;

const StyledNavBar = styled.View`
  background-color: ${primaryColorLight};
  flex-direction: row;
  width: 80%;
  padding: 15px 20px;
  justify-content: space-around;
  align-items: center;
  border-radius: 100px;
`;

const StyledProfile = styled.View`
  background: ${secondaryColor};
  width: 24px;
  height: 24px;
  border-radius: 100px;
  border: 1px solid ${(props) => (props.active ? primaryColor : defaultColor)};
`;
