package main

import (
	"mundansock/controllers"

	"github.com/labstack/echo/v4"
	"github.com/labstack/echo/v4/middleware"
)

func main() {

	app := echo.New()

	app.Use(middleware.Logger())
	app.Use(middleware.CORS())
	app.Use(middleware.Recover())

	app.GET("/door/:id", controllers.CheckDoor)
	app.GET("/ws", controllers.Socket)

	app.Logger.Fatal(app.Start(":5050"))
}
