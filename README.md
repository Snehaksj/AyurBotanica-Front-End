# AyurBotanica - Identification of medicinal plants

## Description

AyurBotanica is a comprehensive project aimed at leveraging Deep learning algorithms to identify medicianl plants. It uses EfficientNetV2 architecture along with transfer learning to identify th plants. This repository only focusses on the front end aspect and teh backend required for displaying the necessary components. To check the model and preprocessing of image sent to the model (backend API) click [here](https://github.com/CrypticFate5/AyurBotanica)

## Technological Stack

### Backend

- **Framework**: Flask (Python)
- **Database**: MongoDB
- **API Development**: REST API
- (the uploading part contains a dummy API, the real API endpoint is in [this](https://github.com/CrypticFate5/AyurBotanica) repository

### Frontend

- **Framework**: React.js set up using Vite
- **Styling**: CSS Modules
- **Data Fetching**: Axios

## How to run the project

Check out both our repositories and clone the necessary elements

**Frontend**

```bash
cd Client
npm install
npm run dev
```

**Backend**

```bash
cd FlaskServer
python app.py
```
