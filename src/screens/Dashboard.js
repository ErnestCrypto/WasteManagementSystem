import React from "react";
import { SafeAreaView } from "react-native-safe-area-context";

import { Routes, Route } from "react-router-native";
import { defaultView } from "../helpers/Variables";

import Request from "./Request";
import Payment from "./Payment";
import Profile from "./Profile";
import Main from "./Main";
import NavBar from "../components/NavBar";
import HeaderIcons from "../components/HeaderIcons";

const Dashboard = ({ navigation }) => {
  return (
    <SafeAreaView style={defaultView}>
      <HeaderIcons />
      <Routes>
        <Route path="/" element={<Main />} />
        <Route path="/requests" element={<Request />} />
        <Route path="/payments" element={<Payment />} />
        <Route path="/profile" element={<Profile />} />
      </Routes>
      <NavBar />
    </SafeAreaView>
  );
};

export default Dashboard;
