//imports for the navigation of screens
import { createStackNavigator } from "@react-navigation/stack";
import { NavigationContainer } from "@react-navigation/native";
import { NativeRouter } from "react-router-native";

//imports for redux pakages and setup
import { Provider } from "react-redux";
import { createStore, applyMiddleware, compose } from "redux";
import thunk from "redux-thunk";
import allReducers from "./src/redux/redux";

//imports for screens and components
import Home from "./src/screens/Home";
import Dashboard from "./src/screens/Dashboard";
import Settings from "./src/screens/Settings";
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
      <NativeRouter>
        <NavigationContainer>
          <Stack.Navigator
            initialRoute="Dashboard"
            screenOptions={{ headerShown: false }}
          >
            <Stack.Screen name="Home" component={Home} />
            <Stack.Screen name="Signin" component={Signin} />
            <Stack.Screen name="Signup" component={Signup} />
            <Stack.Screen name="Dashboard" component={Dashboard} />
            <Stack.Screen name="Settings" component={Settings} />
          </Stack.Navigator>
        </NavigationContainer>
      </NativeRouter>
    </Provider>
  );
}
