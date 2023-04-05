import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import App from './App';

interface IRoute {
  path: string;
  component: () => JSX.Element;
  match?: 'full' | 'partial';
}

const routes: IRoute[] = [
  {
    path: '/',
    component: App,
    match: 'full',
  },
];

class AppRouter extends React.Component {
  render() {
    return (
      <Router>
        <Routes>
            {routes.map((route: IRoute) => (
            <Route
                key={route.path}
                path={route.path}
                element={<route.component />}
            />
            ))}
        </Routes>

      </Router>
    );
  }
}

export default AppRouter;