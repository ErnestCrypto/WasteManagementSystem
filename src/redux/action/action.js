const SET_AUTH = "SET_AUTH";
const RESET_AUTH = "RESET_AUTH";

const setAuth = () => {
  return {
    type: SET_AUTH,
  };
};

const resetAuth = () => {
  return {
    type: RESET_AUTH,
  };
};
