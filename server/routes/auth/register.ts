import express from 'express';
import mongoose from 'mongoose';
import Invite from '../../models/invite.model';
import User from '../../models/user.model';
import bcrypt from 'bcryptjs';
mongoose.connect(process.env.MONGO_URI!, { useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true, useFindAndModify: false })

const router = express.Router();

router.post('/register', async (req, res) => {

})