// import SecondWave from "../components/Canvas/SecondWave/SecondWave"
import DiagonalWave from "../components/Canvas/DiagonalWave/DiagonalWave"
import Wave from "../components/Canvas/Wave/Wave"
import SecondWave from "../components/Canvas/SecondWave/SecondWave"
import Rain from "../components/Canvas/Rain/Rain"
import { useState, useEffect, useRef } from "react"
// import someImg from "../assets/calmwave.png"
import NightSky from "../components/Canvas/NightSky/NightSky"
import Earth from "../components/Canvas/Earth/Earth"
import SecondNightSky from "../components/Canvas/SecondNightSky/SecondNightsky"
import { useCustomWidthHeight } from "../hooks/custom/useCustomWidthHeight"
import Modal from "../components/UI/Modal"
import CategoryForm from "../components/UI/CategoryForm/CategoryForm"
// import { useSearchParams } from "react-router-dom"
import test from "../utils/test"
import axios from "axios"
import styles from "./TestPage.module.css"
import { useClasses } from "../hooks/custom/useClasses"
import SkyWithWave from "../components/Canvas/SkyWithWave/SkyWithWave"

function TestPage() {
  // const [searchParams] = useSearchParams()
  // const AccessToken = searchParams.get("AccessToken")
  // const RefreshToken = searchParams.get("RefreshToken")
  // const userid = searchParams.get("userid")
  // console.log(">>>>>>>>", AccessToken)
  // console.log("<<<<<<<<", RefreshToken)
  // console.log(userid, "여기가 유저 아이디에용")
  const [canvasWidth, setCanvasWidth] = useState(0)
  const [canvasHeight, setCanvasHeight] = useState(0)
  const canvRef = useRef(null)
  const [togglehover, toggleselect, classes] = useClasses(styles, "test")
  /* eslint-disable */
  useEffect(
    function () {
      setCanvasHeight(window.innerHeight)
      setCanvasWidth(window.innerWidth)
    },
    [window.innerHeight, window.innerWidth]
  )
  const { width, height } = useCustomWidthHeight(canvRef)
  const [isModal, setIsModal] = useState(true)
  const toggleModal = function () {
    setIsModal((val) => !val)
  }
  axios.defaults.headers.asdf = "asdfadsf"
  // const [isHi, setIsHi] = useState(false)
  // const toggleHi = function () {
  //   setIsHi((val) => !val)
  // }
  return (
    <>
      <Modal toggleIsOpen={toggleModal} isOpen={isModal}>
        <CategoryForm
          // data={{ title: "수정", description: "기존 값" }}
          isOpen={isModal}
        />
      </Modal>
      <div
        className={classes}
        onClick={toggleselect}
        onMouseEnter={togglehover}
        onMouseLeave={togglehover}
      >
        useClasses Test Well~~~~~
      </div>
      <div onClick={toggleModal}>모달 토글</div>
      <div onClick={test}>테스트</div>
      {/* <div onClick={toggleHi}>하이 토글</div> */}
      <div style={{ display: "none" }}>
        {/* <img src={someImg} id={`test-logo`} /> */}
      </div>
      <SkyWithWave
        canvasWidth={canvasWidth}
        canvasHeight={canvasHeight}
        background={`rgba(0, 0, 0, 1)`}
      />
      <SecondNightSky
        canvasWidth={canvasWidth}
        canvasHeight={canvasHeight}
        background={`rgba(32, 38, 38, 1) `}
      />
      <Earth
        canvasWidth={canvasWidth}
        canvasHeight={canvasHeight}
        background={`rgba(32, 38, 38, 1) `}
      />
      <NightSky
        canvasWidth={canvasWidth}
        canvasHeight={canvasHeight}
        background={`rgba(32, 38, 38, 1) `}
      />
      <Rain
        canvasWidth={canvasWidth}
        canvasHeight={canvasHeight}
        background={`rgba(29, 88, 164, 0.66)`}
      />
      <DiagonalWave
        canvasWidth={canvasWidth}
        canvasHeight={canvasHeight}
        leftColor={`rgba(255, 255, 255, 1)`}
        rightColor={`rgba(29, 88, 164, 0.66)`}
      />
      <SecondWave
        canvasWidth={canvasWidth}
        canvasHeight={canvasHeight}
        background={`rgba(255, 255, 255, 1)`}
        FstColor={`rgba(76, 230, 184, 0.88)`}
        SndColor={`rgba(153, 214, 234, 0.7)`}
        TrdColor={`rgba(29, 88, 164, 0.66)`}
        innerColor={`rgb(168, 138, 255)`}
      />
      <Wave
        canvasHeight={canvasHeight}
        canvasWidth={canvasWidth}
        background={`rgba(31, 31, 36)`}
      />
      <div ref={canvRef}>can i get size?</div>
    </>
  )
}

export default TestPage
