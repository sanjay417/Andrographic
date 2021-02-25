import React from 'react';
import PropTypes from 'prop-types';
import { makeStyles } from '@material-ui/core/styles';
import Tabs from '@material-ui/core/Tabs';
import Tab from '@material-ui/core/Tab';
import Typography from '@material-ui/core/Typography';
import Box from '@material-ui/core/Box';
import {CategoryView, DevPermissionView, GenrePermissionView, GenreSystemActionsView, GenrePermissionCategoryView} from "./index";

function TabPanel(props) {
    const { children, value, index, ...other } = props;

    return (
        <Typography
            component="div"
            role="tabpanel"
            hidden={value !== index}
            id={`vertical-tabpanel-${index}`}
            aria-labelledby={`vertical-tab-${index}`}
            {...other}
        >
            <Box p={3}>{children}</Box>
        </Typography>
    );
}

TabPanel.propTypes = {
    children: PropTypes.node,
    index: PropTypes.any.isRequired,
    value: PropTypes.any.isRequired,
};

function a11yProps(index) {
    return {
        id: `vertical-tab-${index}`,
        'aria-controls': `vertical-tabpanel-${index}`,
    };
}

const useStyles = makeStyles(theme => ({
    root: {
        flexGrow: 1,
        backgroundColor: theme.palette.background.paper,
        display: 'flex',
        height: '50%',
        width: '100%',
        minHeight: '50em',
        minWidth: '50em'
    },
    tabs: {
        borderRight: `1px solid ${theme.palette.divider}`,
        height: '50em',
        width: '15em'
    },

    panels:{
        width: "100%"
    }
}));

export default function GenreTabs() {
    const classes = useStyles();
    const [value, setValue] = React.useState(0);
    const [multi, setMulti] = React.useState();
    const [flow, setFlow] = React.useState("");

    const handleChange = (event, newValue, developers) => {
        if(developers){
            setMulti(developers)
            setFlow("drill");
        }
        setValue(newValue);
    };

    const onChangeFlow = (flowName) =>{
        setFlow(flowName);
    }


    return (
        <div className={classes.root}>
            <Tabs
                orientation="vertical"
                variant="scrollable"
                value={value}
                onChange={handleChange}
                aria-label="Vertical tabs example"
                className={classes.tabs}
            >
                <Tab label="Application Genre" {...a11yProps(0)} />
                <Tab label="Permission" {...a11yProps(1)} />
                <Tab label="System Action" {...a11yProps(2)} />
                <Tab label="Permission Category" {...a11yProps(3)} />
            </Tabs>
            <TabPanel value={value} index={0} className={classes.panels}>
                <CategoryView />
            </TabPanel>
            <TabPanel value={value} index={1} className={classes.panels}>
                <GenrePermissionView />
            </TabPanel>
            <TabPanel value={value} index={2} className={classes.panels}>
                <GenreSystemActionsView/>
            </TabPanel>
            <TabPanel value={value} index={3} className={classes.panels}>
                <GenrePermissionCategoryView />
            </TabPanel>
        </div>
    );
}
