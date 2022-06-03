const SET_AUTH = "SET_AUTH";
const RESET_AUTH = "RESET_AUTH";

const setAuth = (data) => {
  return {
    type: SET_AUTH,
    payload: data,
  };
};

const resetAuth = () => {
  return {
    type: RESET_AUTH,
  };
};
