const initState = { isLoggedIn: false, userId: null };

const authReducer = (state = initState, action) => {
  switch (action.type) {
    case "SET_AUTH":
      return { ...state, isLoggedIn: true, userId: action.data };
    case "RESET_AUTH":
      return { ...initialState };
    default:
      return { ...state };
  }
};

export default authReducer;
