import express from 'express';
import invite from './routes/invite';
import crypto from 'crypto';

const app = express();
const port = 8080; // default port to listen

// define a route handler for the default home page

app.use(express.json())
app.use(express.urlencoded({ extended: true }))


app.use('/invite', invite )


// start the Express server
app.listen( port, () => {
    // tslint:disable-next-line:no-console
    console.log( `server started at http://localhost:${ port }` );
});

