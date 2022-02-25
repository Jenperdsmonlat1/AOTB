package com.example.avastofthebled_v2

import javafx.event.ActionEvent
import javafx.fxml.FXML
import javafx.fxml.FXMLLoader
import javafx.scene.Node
import javafx.scene.Parent
import javafx.scene.Scene
import javafx.scene.control.Button
import javafx.scene.control.TextField
import javafx.scene.effect.Shadow
import javafx.scene.layout.VBox
import javafx.scene.paint.Color
import javafx.stage.FileChooser
import javafx.stage.Stage
import javafx.scene.control.Alert
import javafx.scene.control.Alert.AlertType
import java.io.File
import java.security.MessageDigest
import com.example.avastofthebled_v2.MD5Get

class HelloController {

    @FXML
    private lateinit var btnFullScan: Button

    @FXML
    private lateinit var btnScanFile: Button

    @FXML
    private lateinit var btnSubmitMalware: Button

    @FXML
    private lateinit var btnValid: Button

    @FXML
    private lateinit var exitButton: Button

    @FXML
    private lateinit var inputFile: TextField

    @FXML
    private lateinit var maximizeButton: Button

    @FXML
    private lateinit var minimizeButton: Button

    @FXML
    private lateinit var root: VBox

    private lateinit var stage: Stage
    private lateinit var scene: Scene
    private var etat: Int = 0

    val shadow: Shadow = Shadow(10.0, Color.CYAN)
    val chooser: FileChooser = FileChooser()

    private fun initialize(): Unit {
        btnValid.effect = shadow
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

    public fun switchToFullScan(e: ActionEvent): Unit {
        val route: Parent = FXMLLoader.load(HelloApplication::class.java.getResource("full-scan.fxml"))
        stage = ((e.source) as Node).scene.window as Stage
        scene = Scene(route)
        stage.scene = scene
        stage.show()
    }

    public fun switchToSubmitMalware(e: ActionEvent): Unit {
        val opener = Opener();
        opener.open("https://aotb.000webhostapp.com/index.php")
    }

    public fun startScan(e: ActionEvent): Unit {
        try {
            stage = root.scene.window as Stage
            val file: File?= chooser.showOpenDialog(stage)
            inputFile.text = file?.absolutePath

            val digest: MessageDigest = MessageDigest.getInstance("MD5")
            val md5 = MD5Get()
            val hash: String = md5.checksum(digest, file)
            println(hash)
            val db = readFileLinePerLine("D:\\AOTB_V2\\hashs.txt")
            for (hashs in db) {

                println(hashs)
                val result = if (hash == hashs) {
                    val alert: Alert = Alert(AlertType.WARNING)
                    alert.title = "Virus détecté."
                    alert.headerText = "Une menace a été détecté."
                    alert.contentText = "Le fichier analysé est potentiellement infecté."
                    alert.show()
                    break
                } else {
                    null
                }
            }
            val noalert: Alert = Alert(AlertType.INFORMATION)
            noalert.title = "Aucuns virus."
            noalert.headerText = "Aucune menace détecté."
            noalert.contentText = "Le fichier analysé semble sûr. Nous vous conseillons de réaliser une analyse approfondi."
            noalert.show()
        } catch (e: Exception) {
            println("Une erreur est survenue.")
            val erralert: Alert = Alert(AlertType.ERROR)
            erralert.title = "Erreur"
            erralert.headerText = "Impossible d'ouvrir le fichier."
            erralert.contentText = "Une erreur est survenu lors de la lecture du fichier."
            erralert.show()
        }
    }

    public fun readFileLinePerLine(fileName: String): List<String> = File(fileName).readLines()
}