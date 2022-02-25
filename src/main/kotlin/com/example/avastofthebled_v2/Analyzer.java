package com.example.avastofthebled_v2;

import java.io.File;
import java.util.ArrayList;
import java.util.List;

public class Analyzer {

    public List<String> enumFile() {
        File[] files = new File("C:\\").listFiles();
        List<String> results = new ArrayList<String>();

        for (File file: files) {
            if (file.isFile()) {
                results.add(file.getAbsolutePath());
            }
        }

        return results;
    }
}
