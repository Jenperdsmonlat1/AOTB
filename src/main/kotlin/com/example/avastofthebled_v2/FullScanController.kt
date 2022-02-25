package com.example.avastofthebled_v2

import javafx.event.ActionEvent
import javafx.fxml.FXML
import javafx.fxml.FXMLLoader
import javafx.scene.Node
import javafx.scene.Parent
import javafx.scene.Scene
import javafx.scene.control.Button
import javafx.scene.control.Label
import javafx.scene.control.ScrollPane
import javafx.scene.control.TextField
import javafx.scene.effect.Shadow
import javafx.scene.layout.VBox
import javafx.scene.paint.Color
import javafx.stage.Stage
import java.io.File
import java.security.MessageDigest

class FullScanController {

    @FXML
    private lateinit var btnFullScan: Button

    @FXML
    private lateinit var btnScanFile: Button

    @FXML
    private lateinit var btnSubmitMalware: Button

    @FXML
    private lateinit var btnStartScan: Button

    @FXML
    private lateinit var exitButton: Button

    @FXML
    private lateinit var inputFile: TextField

    @FXML
    private lateinit var maximizeButton: Button

    @FXML
    private lateinit var minimizeButton: Button

    @FXML
    private lateinit var scrollpane: ScrollPane

    @FXML
    private lateinit var root: VBox

    private lateinit var stage: Stage
    private lateinit var scene: Scene
    private var etat: Int = 0

    val shadow: Shadow = Shadow(10.0, Color.CYAN)

    private fun initialize(): Unit {
        btnStartScan.effect = shadow
    }

    public fun exit(e: ActionEvent): Unit {
        stage = root.scene.window as Stage
        stage.close()
    }

    public fun reduce(e: ActionEvent): Unit {
        stage = root.scene.window as Stage
        stage.isIconified = true
    }

    public fun setMax(e: ActionEvent): Unit {
        stage = root.scene.window as Stage

        var result = if (etat == 0) {
            stage.isMaximized = true
            etat = 1
        } else {
            stage.isMaximized = false
            etat = 0
        }
    }

    public fun switchToScanFile(e: ActionEvent): Unit {
        val route: Parent = FXMLLoader.load(HelloApplication::class.java.getResource("hello-view.fxml"))
        stage = ((e.source) as Node).scene.window as Stage
        scene = Scene(route)
        stage.scene = scene
        stage.show()
    }

    public fun switchToSubmitMalware(e: ActionEvent): Unit {
        val opener = Opener();
        opener.open("https://aotb.000webhostapp.com/index.php")
    }

    public fun startFullScan(e: ActionEvent): Unit {
        val analyzer = Analyzer()
        var listFiles: List<String> = ArrayList<String>()
        listFiles = analyzer.enumFile()
        val md5 = MD5Get()
        val digest: MessageDigest = MessageDigest.getInstance("MD5")
        val db = readFileLinePerLine("D:\\AOTB_V2\\hashs.txt")
    }

    public fun readFileLinePerLine(fileName: String): List<String> = File(fileName).readLines()
}
