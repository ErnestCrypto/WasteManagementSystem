import React from "react";
import { SafeAreaView } from "react-native-safe-area-context";

import { Routes, Route } from "react-router-native";
import { defaultView } from "../helpers/Variables";

import Request from "./Request";
import Payment from "./Payment";
import Profile from "./Profile";
import Main from "./Main";
import NavBar from "../components/NavBar";

const Dashboard = () => {
  return (
    <SafeAreaView style={defaultView}>
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
