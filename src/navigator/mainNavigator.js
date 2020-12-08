import { createAppContainer } from 'react-navigation';
import { createStackNavigator } from 'react-navigation-stack';
import {createDrawerNavigator} from 'react-navigation-drawer';

import SplashScreen from "../features/SplashScreen";
import SideMenu from './sideMenu';
//@BlueprintImportInsertion
import UserProfile183236Navigator from '../features/UserProfile183236/navigator';
import Tutorial183235Navigator from '../features/Tutorial183235/navigator';
import NotificationList183207Navigator from '../features/NotificationList183207/navigator';
import Settings183206Navigator from '../features/Settings183206/navigator';
import Settings183198Navigator from '../features/Settings183198/navigator';
import UserProfile183196Navigator from '../features/UserProfile183196/navigator';

/**
 * new navigators can be imported here
 */

const AppNavigator = {

    //@BlueprintNavigationInsertion
UserProfile183236: { screen: UserProfile183236Navigator },
Tutorial183235: { screen: Tutorial183235Navigator },
NotificationList183207: { screen: NotificationList183207Navigator },
Settings183206: { screen: Settings183206Navigator },
Settings183198: { screen: Settings183198Navigator },
UserProfile183196: { screen: UserProfile183196Navigator },

    /** new navigators can be added here */
    SplashScreen: {
      screen: SplashScreen
    }
};

const DrawerAppNavigator = createDrawerNavigator(
  {
    ...AppNavigator,
  },
  {
    contentComponent: SideMenu
  },
);

const AppContainer = createAppContainer(DrawerAppNavigator);

export default AppContainer;
