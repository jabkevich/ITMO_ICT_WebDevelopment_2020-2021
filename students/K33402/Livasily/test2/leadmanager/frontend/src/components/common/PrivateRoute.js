import React, {Component} from 'react';
import PropTypes from 'prop-types';
import {Route, Redirect} from 'react-router-dom'
import {connect} from "react-redux"

const PrivateRoute = ({component: Component, auth, ...rest}) => (
    <Route
        {...rest}
        render={props => {
            if(auth.isLoading){
                return <h2>Loadin...</h2>
            }else if(!auth.isAuthenticated){
                return <Redirect to={"/Login"}/>
            }else{
                return <Component {...props}/>
            }
        }}
    />
)

const mapStateToProps = state => ({
    auth: state.auth
})

export default connect(mapStateToProps)(PrivateRoute);