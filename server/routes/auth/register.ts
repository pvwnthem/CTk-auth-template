import express from 'express';
import mongoose from 'mongoose';
import Invite from '../../models/invite.model';
import User from '../../models/user.model';
import bcrypt from 'bcryptjs';
mongoose.connect(process.env.MONGO_URI!)

const router = express.Router();
router.post('/', async (req: any, res: any) => {
    try {
    const { username, password, invite, hwid } = req.body
    console.log(req.body)
    if (!username || !password || !invite) {
    return res.status(400).send('Missing username, password or invite')
    }
    const inviteCode = await Invite.findOne({ invite: invite })
    if (!inviteCode) {
    return res.status(400).send('Invalid invite code')
    }

    const user = await User.create({
    username: username,
    password: bcrypt.hashSync(password, 10),
    invitedwith: invite,
    hwid: hwid
    })
    await Invite.findOneAndDelete({ invite: invite })
    res.status(200).send(user)
    
    
    } catch (err) {
    console.log(err)
    res.status(400).send(err)
    }
    })

export default router;
