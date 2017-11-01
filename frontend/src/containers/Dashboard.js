import React from 'react'


import Header from '../components/Header';
import LogViewContainer from '../components/LogView/log-view-container'


export default class Dashboard extends React.Component {


    render() {
        return (
            <div>
                <Header />
                <LogViewContainer/>
            </div>
        )
    }
}