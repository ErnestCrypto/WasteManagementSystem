import { StatusBar } from "expo-status-bar";

//imports for the navigation of screens
import { createStackNavigator } from "@react-navigation/stack";
import { NavigationContainer } from "@react-navigation/native";

//imports for redux pakages and setup
import { Provider } from "react-redux";
import { createStore, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";
import allReducers from "./src/redux/redux";

//imports for screens and components
import Home from "./src/screens/Home";
import EditProfile from "./src/screens/EditProfile";
import Notification from "./src/screens/Notification";
import Payment from "./src/screens/Payment";
import Request from "./src/screens/Request";
import Settings from "./src/screens/Settings";
import Profile from "./src/screens/Profile";
import Signin from "./src/auth/Signin";
import Signup from "./src/auth/Signup";

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const store = createStore(
  allReducers,
  composeEnhancers(applyMiddleware(thunk))
);

export default function App() {
  const Stack = createStackNavigator();

  return (
    <Provider store={store}>
      <NavigationContainer>
        <Stack.Navigator
          initialRoute="Home"
          screenOptions={{ headerShown: false }}
        >
          <Stack.Screen name="Home" component={Home} />
          <Stack.Screen name="Signin" component={Signin} />
          <Stack.Screen name="Signup" component={Signup} />
        </Stack.Navigator>
      </NavigationContainer>
    </Provider>
  );
}
