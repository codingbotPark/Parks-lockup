import axios from "axios";
import { useEffect, useState } from "react";
import { styled, keyframes } from "styled-components";
// import doorimg from "./door.png";

function App() {
  const DoorContainer = styled.div`
    position: absolute;
    bottom: 10vh;
    left: 50%;
    transform: translateX(-50%);
    background: #fff;
    z-index: 5;
    clip: rect(-5vh, auto, 100vh, auto);
    perspective: 100vw;
  `;

  // const DoorMain = styled.img`
  //   transform: ${(props) =>
  //     props.imgstate ? "perspective(100vw) rotateY(-80deg)" : ""};
  //   transition-timing-function: ease;
  // `;

  const Container = styled.div`
    width: 100%;
    height: 100vh;
  `;

  const openAnimation = keyframes`
  0% {
    transform: rotateY(0deg);
  }
  100% {
    transform: rotateY(90deg);
  }
`;

  const closeAnimation = keyframes`
  0% {
    transform: rotateY(90deg);    
  }
  100% {
    transform: rotateY(0deg);
  }
`;

  // 문 스타일드 컴포넌트 정의
  const Door = styled.img`
    width: 400px;
    height: 800px;
    background-color: #ccc;
    transform-origin: left center;
    animation: ${(props) =>
        props.doorstate === "열림" ? openAnimation : closeAnimation}
      1s linear forwards;
  `;

  const [door, setDoor] = useState("닫힘"); // false는 opened, true는 closed

  // const decoder = new TextDecoder("utf-8");

  useEffect(() => {
    let socket = new WebSocket("ws://10.255.255.136:5050/ws");

    socket.onopen = function (e) {
      alert("[open] 커넥션이 만들어졌습니다.");
      alert("데이터를 서버에 전송해봅시다.");
      socket.send("My name is kijun");
    };

    socket.onmessage = function (event) {
      // alert(`[message] 서버로부터 전송받은 데이터: ${event.data}`);
      // const res = decoder.decode(event.data);
      const res = event.data;
      const temp = res === "true" ? true : false;
      if (temp) {
        setDoor("열림");
        console.log("열림");
      } else {
        setDoor("닫힘");
        console.log("닫힘");
      }
    };

    socket.onclose = function (event) {
      if (event.wasClean) {
        alert(
          `[close] 커넥션이 정상적으로 종료되었습니다 (code=${event.code} reason=${event.reason})`
        );
      } else {
        // 장애가 있으면 event.code 1006
        alert("[close] 커넥션이 죽었습니다.");
      }
    };

    socket.onerror = function (error) {
      alert(`[error]`);
    };
  }, []);

  useEffect(() => {
    console.log("확인", door);
  }, [door]);

  function openDoor() {
    axios.get("http://10.255.255.136:5050/door/open");
  }

  return (
    <Container>
      <DoorContainer>
        {/* <DoorMain
          src="https://marshallku.github.io/css-3d-door/door.png"
          onClick={() => setDoor((prev) => !prev)}
          imgstate={door}
        ></DoorMain> */}
        <Door
          src="https://marshallku.github.io/css-3d-door/door.png"
          doorstate={door}
        />
        <div onClick={() => openDoor()}>열림</div>
        <div onClick={() => setDoor("닫힘")}>닫힘</div>
      </DoorContainer>
    </Container>
  );
}

export default App;
