package com.example.avastofthebled_v2;

import java.awt.Desktop;
import java.io.IOException;
import java.net.URI;

public class Opener {

    public void open(String url) {
        try {
            Desktop desk = Desktop.getDesktop();
            desk.browse(URI.create(url));
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
