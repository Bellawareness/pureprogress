# Firebase Hosting Setup Guide
## Deploy Your Habit Tracker to a Custom Domain

---

## 📋 What You'll Need
- Your custom domain name (e.g., myhabittracker.com)
- Firebase account (you already have this)
- 15 minutes

---

## 🚀 Step 1: Install Firebase CLI

Open Terminal and run:

```bash
npm install -g firebase-tools
```

If you don't have Node.js/npm installed:
1. Download from: https://nodejs.org/
2. Install the LTS version
3. Then run the command above

---

## 🔐 Step 2: Login to Firebase

```bash
firebase login
```

This will open your browser to authenticate with your Firebase account.

---

## 📁 Step 3: Prepare Your Project Files

Create a clean folder structure:

```bash
cd /Users/elysian/Downloads/Organize
mkdir habittracker-deploy
cd habittracker-deploy
```

Copy your files into this folder:
- `index.html` (from templates folder)
- `manifest.json`
- `service-worker.js`
- `icon-192.png`
- `icon-512.png`

**IMPORTANT**: Rename `templates/index.html` to just `index.html` in the root folder.

---

## 🔧 Step 4: Initialize Firebase Hosting

In your `habittracker-deploy` folder:

```bash
firebase init hosting
```

Answer the prompts:
1. **Select a Firebase project**: Choose your existing project (the one with your authentication)
2. **What do you want to use as your public directory?** → Press Enter (use default "public")
3. **Configure as a single-page app?** → `y` (Yes)
4. **Set up automatic builds?** → `n` (No)
5. **File public/index.html already exists. Overwrite?** → `n` (No)

---

## 📦 Step 5: Move Your Files to Public Folder

```bash
# Move all your files into the public folder
mv index.html public/
mv manifest.json public/
mv service-worker.js public/
mv icon-192.png public/
mv icon-512.png public/
```

---

## 🚢 Step 6: Deploy to Firebase

```bash
firebase deploy --only hosting
```

✅ Your app is now live! Firebase will give you a URL like:
`https://your-project-name.web.app`

Test this URL to make sure everything works.

---

## 🌐 Step 7: Connect Your Custom Domain

### Option A: Domain from Namecheap/GoDaddy/etc.

1. Go to [Firebase Console](https://console.firebase.google.com)
2. Select your project
3. Click **Hosting** in left sidebar
4. Click **Add custom domain** button
5. Enter your domain: `myhabittracker.com`
6. Firebase will show you DNS records to add

**Add these DNS records at your domain registrar:**

**For root domain (myhabittracker.com):**
- Type: `A`
- Name: `@`
- Value: (IP address Firebase provides)

**For www subdomain:**
- Type: `A`
- Name: `www`
- Value: (IP address Firebase provides)

**SSL Certificate:**
Firebase automatically provisions SSL (HTTPS) - usually takes 24-48 hours.

---

### Option B: Buy Domain Through Cloudflare (Recommended)

If you haven't bought a domain yet, Cloudflare Registrar offers:
- At-cost pricing (~$10/year)
- Instant DNS updates
- Free SSL
- Better security

1. Buy domain at [Cloudflare Registrar](https://www.cloudflare.com/products/registrar/)
2. In Cloudflare DNS settings, add:
   - Type: `A`, Name: `@`, Value: (Firebase IP)
   - Type: `A`, Name: `www`, Value: (Firebase IP)
3. Set Proxy status to "DNS only" (gray cloud)
4. In Firebase Console, add your domain

---

## ✅ Step 8: Verify Everything Works

After DNS propagates (5 minutes to 48 hours), test:

1. **Visit your domain** → Should load your habit tracker
2. **Test login** → Firebase Auth should work
3. **Install PWA** → Click install prompt on mobile
4. **Test offline** → Turn off wifi, app should still load
5. **Check notifications** → Allow notifications, wait for daily reminder

---

## 🔄 Future Updates

Whenever you make changes:

```bash
# 1. Update your files in the public folder
# 2. Deploy changes
firebase deploy --only hosting

# Your site updates in ~30 seconds!
```

---

## 📊 Monitor Usage

Free tier limits (very generous):
- **Storage**: 10 GB
- **Bandwidth**: 360 MB/day (~10 GB/month)
- **Custom domains**: Unlimited

Check usage at: Firebase Console → Hosting → Usage tab

---

## 🐛 Troubleshooting

### Domain not connecting?
- Wait 24-48 hours for DNS propagation
- Use [WhatsMyDNS.net](https://whatsmydns.net) to check DNS propagation
- Make sure proxy is OFF in Cloudflare (if using)

### PWA install not showing?
- Make sure you're using HTTPS (not HTTP)
- Check that `manifest.json` and `service-worker.js` are loading
- Open DevTools → Application → Manifest to debug

### Notifications not working on iPhone?
- This is an Apple limitation - iPhone doesn't support web push notifications
- Android and Desktop will work perfectly

### Firebase Auth not working?
- Check Firebase Console → Authentication → Settings → Authorized domains
- Add your custom domain to the list

---

## 💰 Costs Summary

- **Firebase Hosting**: $0/month (free tier)
- **Firebase Auth**: $0/month (free tier)
- **Firebase Database**: $0/month (free tier, up to 1GB)
- **Custom Domain**: ~$10-12/year
- **SSL Certificate**: $0 (included)

**Total: ~$10/year** 🎉

---

## 🎯 Quick Command Reference

```bash
# Login
firebase login

# Initialize project
firebase init hosting

# Deploy
firebase deploy --only hosting

# View deployment history
firebase hosting:channel:list

# Rollback to previous version (if needed)
firebase hosting:clone SOURCE_SITE_ID:SOURCE_CHANNEL_ID TARGET_SITE_ID:live
```

---

## 📞 Need Help?

- Firebase Hosting Docs: https://firebase.google.com/docs/hosting
- Firebase Support: https://firebase.google.com/support
- Community: https://stackoverflow.com/questions/tagged/firebase-hosting

---

**You're all set! Your habit tracker will be live on your own domain with all features working perfectly.** 🚀
