import express from 'express';
import mongoose from 'mongoose';
import Invite from '../models/invite.model';

mongoose.connect(process.env.MONGO_URI!, { useNewUrlParser: true, useUnifiedTopology: true, useCreateIndex: true, useFindAndModify: false })

const router = express.Router();

router.get('/validate', async (req, res) => {
    const invite = req.query.invite
    if (!invite) {
        res.status(400).send('No invite code provided')
    }
    const inviteCode = await Invite.findOne({ invite: invite })
    if (!inviteCode) {
        res.status(400).send('Invalid invite code')
    }
    res.status(200).send('Valid invite code')
})










export default router;