import QtQuick 2.15
import QtQuick.Controls 2.15

Rectangle {
    width: 400
    height: 300
    color: "#ffffff"

    Rectangle {
        id: rectangle
        anchors.fill: parent

        Button {
            id: button
            text: qsTr("Press me")
            anchors.verticalCenter: parent.verticalCenter
            checkable: true
            anchors.horizontalCenter: parent.horizontalCenter

            Connections {
                target: button
                function onClicked() {
                    animation.start()
                }
            }
        }

        Text {
            id: label
            text: qsTr("Hello Sample1")
            anchors.top: button.bottom
            font.family: "Arial"
            anchors.topMargin: 45
            anchors.horizontalCenter: parent.horizontalCenter

            SequentialAnimation {
                id: animation

                ColorAnimation {
                    id: colorAnimation1
                    target: rectangle
                    property: "color"
                    to: "#2294c6"
                    from: "#ffffff"
                }

                ColorAnimation {
                    id: colorAnimation2
                    target: rectangle
                    property: "color"
                    to: "#ffffff"
                    from: "#2294c6"
                }
            }
        }

        states: [
            State {
                name: "clicked"
                when: button.checked

                PropertyChanges {
                    target: label
                    text: qsTr("Button Checked")
                }
            }
        ]
    }
}
