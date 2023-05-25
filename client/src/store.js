import { configureStore } from "@reduxjs/toolkit";
import thunk from 'redux-thunk';
import rootReducer from './reducers';

const middleware = [thunk];

const preloadedState = {

};

const store = configureStore({
    reducer: rootReducer,
    middleware: middleware,
    devTools: process.env.NODE_ENV !== 'production',
    preloadedState,
});

export default store;