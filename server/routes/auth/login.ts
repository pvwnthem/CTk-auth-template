import express from 'express';
import mongoose from 'mongoose';
import Invite from '../../models/invite.model';
import User from '../../models/user.model';
import bcrypt from 'bcryptjs';
import jwt from 'jsonwebtoken';
mongoose.connect(process.env.MONGO_URI!)

const router = express.Router();
router.post("/", async (req, res) => {
    try {
    const { username, password } = req.body;
    if (!username || !password) {
    return res.status(400).send("Missing username or password");
    }
    const user = await User.findOne({ username }) as any;
    if (!user) {
    return res.status(400).send("Invalid username or password");
    }
    const isValidPassword = bcrypt.compareSync(password, user.password);
    if (!isValidPassword) {
    return res.status(400).send("Invalid username or password");
    }
    const token = jwt.sign({ id: user._id }, process.env.JWT_SECRET!);
    res.status(200).send({ token });
    } catch (err) {
    res.status(500).send(err);
    }
    });