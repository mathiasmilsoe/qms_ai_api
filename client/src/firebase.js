import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore } from "firebase/firestore";

const firebaseConfig = {
    apiKey: "AIzaSyDXazvFz2H4QR9lEYQ_izF_ivn8t10wln8",
    authDomain: "lumidocs.firebaseapp.com",
    projectId: "lumidocs",
    storageBucket: "lumidocs.appspot.com",
    messagingSenderId: "604372223021",
    appId: "1:604372223021:web:5bec7f7a7860e58adbe4a4",
    measurementId: "G-XBCB22JZJ7"
};

const app = initializeApp(firebaseConfig);

export const auth = getAuth(app);
export const db = getFirestore(app);