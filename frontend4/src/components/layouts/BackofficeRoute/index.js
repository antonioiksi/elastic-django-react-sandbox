import React from 'react'
import {Route} from 'react-router-dom'
import {Header} from "../Header";
import {AuthRequired} from "../../auth/AuthRequired";


export const BackofficeRoute =  ({component:Component, ...rest}) => {
    return (
        <Route {...rest} render={matchProps => (
            <div className="BackofficeLayout">
                <AuthRequired/>
                <Header/>
                <div className="Header">Header</div>
                <Component {...matchProps}/>
                <div className="Footer">Footer</div>
            </div>
        )}/>
    )
}
