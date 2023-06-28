package controllers

import (
	"mundansock/models"
	"net/http"
	"strconv"
	"time"

	"github.com/gorilla/websocket"
	"github.com/labstack/echo/v4"
)

var upgrader = websocket.Upgrader{
	ReadBufferSize:  1024,
	WriteBufferSize: 1024,
}

func Socket(c echo.Context) error {

	upgrader.CheckOrigin = func(r *http.Request) bool {
		return true
	}

	ws, err := upgrader.Upgrade(c.Response(), c.Request(), nil)
	if err != nil {
		return err
	}

	defer ws.Close()

	for {

		/*if time.Now().After(models.MyDoor.DoneTime) {
			print
		}*/

		err := ws.WriteMessage(websocket.TextMessage, []byte(strconv.FormatBool(models.MyDoor.Isopened)))
		if err != nil {
			c.Logger().Error(err)
		}

		time.Sleep(time.Second)
	}
}
