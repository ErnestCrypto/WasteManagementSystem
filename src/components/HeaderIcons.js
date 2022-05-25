import React from "react";
import styled from "styled-components/native";
import { Link } from "react-router-native";
import { Notification, Setting2 } from "iconsax-react-native";
import { defaultColor } from "../helpers/Variables";

const HeaderIcons = () => {
  return (
    <StyledIcons>
      <Link to>
        <Notification size="24" color={defaultColor} />
      </Link>
      <Link>
        <Setting2 size="24" color={defaultColor} />
      </Link>
    </StyledIcons>
  );
};

export default HeaderIcons;

const StyledIcons = styled.View`
  position: absolute;
  top: 12%;
  right: 10%;
  flex-direction: row;
  align-items: center;
  justify-content: space-evenly;
  flex: 1;
`;
