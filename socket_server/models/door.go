package models

import "time"

type door struct {
	Isopened   bool
	Limit      int
	OpenedTime time.Time
	DoneTime   time.Time
}

var MyDoor door

const limit = 5

func init() {
	MyDoor = door{Isopened: false, Limit: limit, OpenedTime: time.Now(), DoneTime: time.Now().Add(time.Second * 5)}
}
