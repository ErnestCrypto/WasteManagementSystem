const initState = { isLoggedIn: false, userId: null };

const authReducer = (state = initState, action) => {
  switch (action.type) {
    case "SET_AUTH":
      return { ...state, isLoggedIn: true };
    case "RESET_AUTH":
      return { ...state, isLoggedIn: false };
    default:
      return { ...state };
  }
};

export default authReducer;
