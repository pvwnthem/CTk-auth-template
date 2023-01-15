import express from 'express';
import invite from './routes/invite';
import crypto from 'crypto';
import bodyparser from 'body-parser';
import register from './routes/auth/register';
import login from './routes/auth/login';

const app = express();
const port = 8080; // default port to listen

// define a route handler for the default home page
app.use(bodyparser.json())
app.use(bodyparser.urlencoded({ extended: true }))

app.use(express.json())
app.use(express.urlencoded({ extended: true }))


app.use('/invite', invite )
app.use( '/auth/register', register )
app.use( '/auth/login', login )

// start the Express server
app.listen( port, () => {
    // tslint:disable-next-line:no-console
    console.log( `server started at http://localhost:${ port }` );
});

