import React from 'react';
import './header.css';

import {OfficeMenu} from '../../menu/OfficeMenu';

export const Header = () => {
    return(
        <div>
            <h1>HEADER</h1>
            <OfficeMenu/>
        </div>
    )
}