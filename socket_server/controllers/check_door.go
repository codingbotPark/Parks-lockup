package controllers

import (
	"mundansock/models"
	"time"

	"github.com/labstack/echo/v4"
)

func CheckDoor(c echo.Context) error {

	isOpened := c.Param("id")

	switch isOpened {
	case "open":
		OpenDoor()
	case "close":
		CloseDoor()
	}
	return nil
}

func OpenDoor() {
	models.MyDoor.Isopened = true
	models.MyDoor.OpenedTime = time.Now()
	models.MyDoor.DoneTime = time.Now().Add(time.Second * 5)
}

func CloseDoor() {
	models.MyDoor.Isopened = false
	models.MyDoor.OpenedTime = time.Now()
	models.MyDoor.DoneTime = time.Now().Add(time.Second * 5)
}
