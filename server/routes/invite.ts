import express from 'express';
import mongoose from 'mongoose';
import Invite from '../models/invite.model';

mongoose.connect(process.env.MONGO_URI!, { useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true, useFindAndModify: false })

const router = express.Router();





export default router;