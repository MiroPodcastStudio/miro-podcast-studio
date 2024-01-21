# Miro Podcast Studio

This app creates podcasts using AI from your mindmaps. Your creactivity is limitless as miro canvas.

# 📒 Table of Contents

- [Associated Video](#video)
- [Included Features](#features)
- [Tools and Technologies](#tools)
- [Prerequisites](#prerequisites)
- [Run the app locally](#run)
- [Folder Structure](#folder)
- [Contributing](#contributing)
- [License](#license)

# 📹 Associated Video <a name="video"></a>

Watch the video below for a demo, code walkthrough, and to learn how to set up the app.

[![Build an AI Image Generator app with Next.js and Miro](https://img.youtube.com/vi/i0mOEhUJBrE/0.jpg)](https://youtu.be/i0mOEhUJBrE)


# ✅ Prerequisites <a name="prerequisites"></a>

- You have a [Miro account](https://miro.com/signup/).
- You're [signed in to Miro](https://miro.com/login/).
- Your Miro account has a [Developer team](https://developers.miro.com/docs/create-a-developer-team).
- Your development environment includes [Node.js 14.13](https://nodejs.org/en/download) or a later version.
- All examples use `npm` as a package manager and `npx` as a package runner.
- And ready Backend Application

# 🏃🏽‍♂️ Run the app locally <a name="run"></a>

2. Run `npm install` to install dependencies.
3. Run `npm start` to start developing. \
   Your URL should be similar to this example:
   ```
   http://localhost:3000
   ```
4. Open the [app manifest editor](https://developers.miro.com/docs/manually-create-an-app#step-2-configure-your-app-in-miro) by clicking **Edit in Manifest**. \
   In the app manifest editor, configure the app as follows and then `click save`.

```yaml
appName: Miro Podcast Studio
sdkVersion: SDK_V2
sdkUri: http://localhost:3000
scopes:
  - boards:read
  - boards:write
```

> ⚠️ We recommend to install your app on a [developer team](https://developers.miro.com/docs/create-a-developer-team) while you are developing or testing apps.⚠️

6. Go to your developer team, and open your boards.
7. Click on the plus icon from the bottom section of your left sidebar. If you hover over it, it will say `More apps`.
8. Search for your app `Miro Podcast Studio` or whatever you chose to name it. Click on your app to use it, as shown in the video below. <b>In the video we search for a different app, but the process is the same regardless of the app.</b>


# 🫱🏻‍🫲🏽 Contributing <a name="contributing"></a>

We welcome contributions to the Miro Podcast Studio app. Please contact us at 
[enescanguven@gmail.com](mailto:enescanguven@gmail.com) if you are interested in contributing.

# 🪪 License <a name="license"></a>

[MIT License](https://github.com/enescanguven/miro-podcast-studio/LICENSE).
