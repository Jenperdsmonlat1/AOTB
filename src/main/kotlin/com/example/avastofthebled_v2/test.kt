package com.example.avastofthebled_v2

import java.io.File

fun main() {
    val db = readFileLinePerLine("D:\\AOTB_V2\\hashs.txt")
    println(db[20])
}

fun readFileLinePerLine(fileName: String): List<String> = File(fileName).readLines()
