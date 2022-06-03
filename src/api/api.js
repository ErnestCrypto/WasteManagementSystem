import axios from "axios";

const baseUrl = "https://wastemanagementsystem.herokuapp.com/";

export const getUserId = async (email, password) => {
  return await axios(`${baseUrl}user/auth`, {
    data: { email, password },
  });
};
